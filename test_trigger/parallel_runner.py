import re
import shlex
import subprocess
import sys
import time
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path, PurePath
from time import sleep

import yaml

import config.globalparameter as gl
from src.helper.log import Logger

with open(gl.test_set_path, encoding="UTF-8") as f:
    TEST_SET = yaml.safe_load(f)

with open(gl.test_runtime_path, encoding="UTF-8") as f:
    TEST_RUNTIME = yaml.safe_load(f)

COMBO_TEST_SET = ("RESET_DB", "WH_COMBO")
POSIX_OS = ("linux", "darwin")


class TestResultType(Enum):
    PASS = "Pass"
    FAIL = "Fail"
    TERMINATED = "Terminated"


class TestCase:
    """
    TestCase is a set of "Feature" in BDD,
    which store infos such as name of testcase, file path of the executed feature files, etc.
    """

    def __init__(self, test_name: str, timeout_ratio: float, file_path: str = ""):
        self.name: str = test_name
        self.file_path: str = file_path
        self.exp_runtime: float = None
        self.timeout_ratio: float = timeout_ratio

    def __repr__(self):
        return f"<TestCase name:{self.name} texp_time: {self.exp_runtime} s>"

    def __str__(self):
        return f"{self.name}: {self.exp_runtime} s"

    def set_exp_run_time(self, run_time: float) -> None:
        """
        Set expected run time (sec) for testcase
        """
        self.exp_runtime = run_time

    def run(self, process: subprocess.Popen):
        self.start_time: float = time.time()
        self.process: subprocess.Popen = process

    def finish(self, failed_cnt: int, message: str):
        self.final_status = TestResultType.PASS if failed_cnt == 0 else TestResultType.FAIL
        self.message: str = message

    def terminate(self):
        self.terminate_time: float = time.time()
        self.process.terminate()

        self.final_status = TestResultType.TERMINATED
        runtime = int(self.terminate_time - self.start_time)
        self.message = f"shut down at {timedelta(seconds=runtime)}"

    def check_timeout(self) -> bool:
        """To see if we can tolerate the delaying process"""
        return (time.time() - self.start_time) >= (self.exp_runtime * self.timeout_ratio)


class ParallelTestRunner:
    def __init__(
        self,
        test_path_list: list[str],
        cmd_format: str,
        rerun_dir_path: Path,
        html_dir_path: Path,
        output_dir_path: Path,
        timeout_ratio: int,
        default_runtime: str,
    ):
        self._timeout_ratio: int = timeout_ratio
        self.default_exp_runtime: str = default_runtime
        self._waiting_jobs: list[TestCase] = self._get_sorted_test_list(test_path_list)
        self._running_jobs: list[TestCase] = []
        self._finished_jobs: list[TestCase] = []
        self._terminated_jobs: list[TestCase] = []

        self._cmd_format: str = cmd_format
        self._rerun_dir_path: Path = rerun_dir_path
        self._html_dir_path: Path = html_dir_path
        self._output_dir_path: Path = output_dir_path

        if sys.platform in POSIX_OS:
            self._progress_bar_fill = "█"
        else:
            self._progress_bar_fill = "#"
        self._max_test_name_length = 35

    def _get_sorted_test_list(self, test_path_list: list[str]) -> list[TestCase]:
        """
        test set are sorted by expected runtime in ascending order
        return {test_name: TestCaseObject}
        """
        # init testcase
        test_list: list[TestCase] = []
        for path in test_path_list:
            name = Path(path).stem
            test_list.append(TestCase(name, self._timeout_ratio, path))

        # setting exp runtime
        for testcase in test_list:
            try:
                run_time: str = TEST_RUNTIME[testcase.name]
            except KeyError:
                run_time = self.default_exp_runtime
                msg = f"Missing setting runtime config for { testcase.name }, now set temporarily to { run_time }"
                Logger.getLogger().warning(msg)
            try:
                exp_runtime_in_sec: float = trans_dur_str_to_sec(run_time)
            except Exception:
                run_time = "30m 00s"
                exp_runtime_in_sec: float = trans_dur_str_to_sec(run_time)
                msg = f"Wrong format for default exp_runtime, now set { name }'s runtime temporarily to { run_time }"
                Logger.getLogger().warning(msg)
            testcase.set_exp_run_time(exp_runtime_in_sec)

        # sort
        test_list.sort(key=lambda testcase: testcase.exp_runtime)

        # combine testcase combo
        test_list = self._combine_integration_tests(test_list)

        return test_list

    def _combine_integration_tests(self, test_list: list[TestCase]) -> list[TestCase]:
        """
        TO combine several tests into one big test
        """

        for name in COMBO_TEST_SET:
            tests = [PurePath(p).stem for p in TEST_SET[name]]
            test_list = self._merge_test(test_list, tests, name)

        test_list.sort(key=lambda testcase: testcase.exp_runtime)
        return test_list

    def _merge_test(self, test_list: list[TestCase], combined_tests: list[str], combined_name: str) -> list[TestCase]:
        if any(test.name == name for test in test_list for name in combined_tests):
            new_test = TestCase(combined_name, self._timeout_ratio)
            new_path = ""
            new_runtime = 0
            for name in combined_tests:
                for testcase in test_list:
                    if testcase.name == name:
                        test_list.remove(testcase)
                        path = testcase.file_path
                        exp_runtime = testcase.exp_runtime

                        new_path += path + " "
                        new_runtime += exp_runtime
                        break

            new_test.file_path = new_path
            new_test.set_exp_run_time(new_runtime)
            test_list.append(new_test)

        return test_list

    def _run(self, next_test: TestCase, process: subprocess.Popen) -> None:
        next_test.run(process)
        self._running_jobs.append(next_test)

    def _finish(self, test: TestCase):
        with open(self._output_dir_path / f"{test.name}_output.txt", encoding="utf8") as file:
            output_lines = file.readlines()
        failed_cnt, msg = extract_test_result("\n".join(output_lines))

        try:
            test.finish(failed_cnt, msg)
            self._running_jobs.remove(test)
            self._finished_jobs.append(test)
        except:
            Logger.getLogger().warning(f"There's no such job {test}")

    def _terminate(self, test: TestCase):
        try:
            test.terminate()
            self._running_jobs.remove(test)
            self._terminated_jobs.append(test)
        except:
            Logger.getLogger().warning(f"There's no such job {test}")

        # To mark this test as needed-rerun
        with open(self._rerun_dir_path / f"rerun_{test.name}.txt", mode="w", encoding="utf8") as file:
            file.write(f"{test.file_path}: terminated")

    def _get_next_job(self) -> TestCase:
        return self._waiting_jobs.pop(0)

    def _get_running_jobs(self) -> list[TestCase]:
        return self._running_jobs

    def _print_status_panel(self) -> None:
        current_time = time.time()

        # running process
        running_cnt = len(self._running_jobs)
        for i in range(running_cnt):
            test = self._running_jobs[i]
            run_time = int(current_time - test.start_time)
            prefix = f"{i+1} of {running_cnt}  {test.name:<{self._max_test_name_length}}"
            infix = f"{timedelta(seconds=run_time)} / {timedelta(seconds=test.exp_runtime)}"
            bar = get_progress_bar_str(
                iteration=run_time,
                total=test.exp_runtime,
                prefix=prefix,
                infix=infix,
                length=40,
                fill=self._progress_bar_fill,
            )
            Logger.getLogger().info(bar)
        print()

        # waiting process
        if self._waiting_jobs:
            waiting_pool_msg = f"Waiting: {', '.join([t.name for t in self._waiting_jobs])}"
            Logger.getLogger().info(waiting_pool_msg)
        else:
            Logger.getLogger().info("Waiting: No waiting jobs")
        print()

        # ended process
        ended_job = self._finished_jobs + self._terminated_jobs
        ended_job.sort(key=lambda testcase: testcase.name)
        for test in ended_job:
            msg = f"{test.final_status.value:<10} {test.name:<{self._max_test_name_length}} {test.message}"
            if test.final_status == TestResultType.PASS:
                Logger.getLogger().info(msg)
            else:
                Logger.getLogger().warning(msg)
        print()

    def is_all_done(self) -> bool:
        return not self._running_jobs and not self._waiting_jobs

    def has_waiting_tests(self) -> bool:
        return len(self._waiting_jobs) > 0

    def get_all_test_names(self) -> list[str]:
        all_test = self._waiting_jobs + self._running_jobs + self._finished_jobs + self._terminated_jobs
        return [test.name for test in all_test]

    def get_running_cnt(self) -> int:
        return len(self._running_jobs)

    def run_all(self, max_parallel_cnt: int) -> list[Path]:
        while not self.is_all_done():
            # update status in parallel_task
            # and terminate timeout process
            for test in self._get_running_jobs():
                process = test.process
                return_code = process.poll()  # check if process has terminated

                if return_code != None:
                    self._finish(test)
                elif test.check_timeout():  # check if process is timeout
                    self._terminate(test)

            # run available tests and update status in parallel_task
            parallel_cnt = self.get_running_cnt()
            while self.has_waiting_tests() and parallel_cnt < max_parallel_cnt:
                test = self._get_next_job()
                cmd = self._cmd_format.format(
                    run_test_paths_cmd=test.file_path,
                    html_report_path=self._html_dir_path / f"report_{test.name}.html",
                    rerun_path=self._rerun_dir_path / f"rerun_{test.name}.txt",
                )

                with open(self._output_dir_path / f"{test.name}_output.txt", mode="w", encoding="utf8") as file:
                    if sys.platform in POSIX_OS:
                        args = shlex.split(cmd)
                    else:
                        args = cmd
                    p = subprocess.Popen(
                        args,
                        stdin=subprocess.PIPE,
                        stdout=file,
                        stderr=file,
                    )
                self._run(test, p)
                parallel_cnt = self.get_running_cnt()  # update current runner count

            # update progress in console
            self._print_status_panel()
            sleep(5)

        return [self._rerun_dir_path / f"rerun_{name}.txt" for name in self.get_all_test_names()]


def trans_dur_str_to_sec(duration: str) -> float:
    """Turn time duration string into number
    Parameters:
    duration (int): time duration in "%Mm %Ss" format, such as "30m 00s"

    Returns:
    int: duration in seconds
    """
    daration_dt: datetime = datetime.strptime(duration, "%Mm %Ss")
    delta = timedelta(hours=daration_dt.hour, minutes=daration_dt.minute, seconds=daration_dt.second)
    return delta.total_seconds()


def extract_test_result(behave_output: str) -> tuple[int, str]:
    try:
        # e.g., "22 scenarios passed, 0 failed, 0 skipped"
        result_format = "(\d+) {type}(s?) passed, (\d+) failed, (\d+) skipped(.*)"
        result = re.search(result_format.format(type="scenario"), behave_output)
        failed_cnt = int(result.group(3))
        message = result.group()
    except:
        failed_cnt, message = 1, "There's something wrong with Behave output"
    return failed_cnt, message


def get_progress_bar_str(
    iteration: int,
    total: int,
    prefix: str = "",
    infix: str = "",
    suffix: str = "",
    decimals: int = 1,
    length: int = 100,
    fill: str = "█",
) -> str:
    """
    Format a beatiful customized progress bar string
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g., "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = min(length, int(length * iteration // total))
    bar = fill * filledLength + "-" * (length - filledLength)
    return f"{prefix} |{bar}| {infix} {percent}% {suffix}"


def run_parallel_test(
    cmd_format: str,
    max_parallel_cnt: int,
    test_set: list[str],
    rerun_dir_path: Path,
    html_dir_path: Path,
    timeout_ratio: int,
    default_runtime: str,
) -> list[Path]:

    # prepare environment
    Logger(name="Test Runner", level="info")
    console_output_dir = Path(gl.console_output_path)
    if not console_output_dir.exists():
        console_output_dir.mkdir()

    rerun_paths: list[Path] = []  # rerun.txt (if the scenario fail or occurs error then would create this file)
    reset_test: list[str] = []
    normal_test: list[str] = []

    reset_test_path_set: list[str] = [str(PurePath(p)) for p in TEST_SET["RESET_DB"]]
    for test in test_set:
        if test in reset_test_path_set:
            reset_test.append(test)
        else:
            normal_test.append(test)
    # reset part
    if reset_test:
        reset_task = ParallelTestRunner(
            test_path_list=reset_test,
            cmd_format=cmd_format,
            rerun_dir_path=rerun_dir_path,
            html_dir_path=html_dir_path,
            output_dir_path=console_output_dir,
            timeout_ratio=timeout_ratio,
            default_runtime=default_runtime,
        )
        rerun_paths += reset_task.run_all(max_parallel_cnt=max_parallel_cnt)

        # if reset-db is failed, then terminates other tests
        for path in rerun_paths:
            if path.is_file():
                with path.open(encoding="utf8") as f:
                    failed_feature_text = f.read()
                if failed_feature_text != None:
                    return rerun_paths

    # actual testing part
    parallel_task = ParallelTestRunner(
        test_path_list=normal_test,
        cmd_format=cmd_format,
        rerun_dir_path=rerun_dir_path,
        html_dir_path=html_dir_path,
        output_dir_path=console_output_dir,
        timeout_ratio=timeout_ratio,
        default_runtime=default_runtime,
    )
    rerun_paths += parallel_task.run_all(max_parallel_cnt=max_parallel_cnt)

    return rerun_paths
