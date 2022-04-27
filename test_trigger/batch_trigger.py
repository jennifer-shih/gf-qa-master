import sys

sys.path.append(".")
import argparse
import os
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path, PurePath, PurePosixPath

import yaml
from bs4 import BeautifulSoup
from parallel_runner import run_parallel_test

import config.globalparameter as gl

"""
Usage:
python test_trigger/batch_trigger.py -t RESET_DB INTERGRATION -c SFI --tags SFI -m 3
python test_trigger/batch_trigger.py -f features/01_Role/0101_CreateRoles.feature -c SFI --tags SFI -m 3
"""

# load test_set and glob feature files
with open(gl.test_set_path, encoding="UTF-8") as f:
    TEST_SET = yaml.safe_load(f)

FEATURE_PATHS = gl.features_path.rglob("*.feature")
RELATIVE_FEATURE_PATHS = [p.relative_to(gl.project_path) for p in FEATURE_PATHS]


def init_argparse() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        prog="BDD Test Trigger",
        description="This is a batch tool for Jenkins to choose what test cases should be run",
    )

    # 互斥選項, 可以選擇以feature path
    test_selector_group = arg_parser.add_mutually_exclusive_group()
    test_selector_group.add_argument(
        "-t",
        "--test_set",
        nargs="*",
        type=str,
        choices=TEST_SET.keys(),
        help="test_set is a group of test cases, which defined in bdd_triger.py.",
    )
    test_selector_group.add_argument(
        "-f",
        "--feature_path",
        nargs="*",
        type=str,
        choices=[str(PurePosixPath(p)) for p in RELATIVE_FEATURE_PATHS],
        help="Input features path, e.g., feature/00_InitialSetup/0001_InitialSetup.feature",
    )
    arg_parser.add_argument(
        "-l",
        "--log_level",
        nargs="?",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="DEBUG",
        help="There are 4 logging levels: DEBUG, INFO, WARNING, ERROR",
    )
    arg_parser.add_argument(
        "-c",
        "--company",
        type=str,
        choices=gl.companyConfig.keys(),
        required=True,
        help="Select company will define basic infos about the company, which defined in config/company_config.yml",
    )
    arg_parser.add_argument(
        "-m",
        "--monitor",
        nargs="?",
        type=str,
        choices=["0", "1", "2", "3", "4"],
        default="0",
        help="Select the monitor mode. 0->headless 1->right 2->left 3->main, 4->Charles",
    )
    arg_parser.add_argument(
        "-p",
        "--parallel_cnt",
        type=int,
        default=1,
        help="Allowed maximum parallel runner count, e.g., 3",
    )
    arg_parser.add_argument(
        "--tags",
        type=str,
        required=True,
        help="BDD test case tags, choose which test case would be executed",
    )
    arg_parser.add_argument(
        "--report",
        nargs="?",
        type=str,
        default="allure-results",
        help="Generate a allure report and save in where.",
    )
    arg_parser.add_argument(
        "-drt",
        "--def_runtime",
        type=str,
        default="30m 00s",
        help="Default testcase expected runtime, e.g., '28m 01s'",
    )
    arg_parser.add_argument(
        "-s",
        "--timeout_ratio",
        type=int,
        default=3,
        help="Times of exp runtime for killing testcase, e.g., 3",
    )

    return arg_parser


@dataclass
class TestResult:
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    undefined: int = 0
    untested: int = 0


class ResultType(Enum):
    FEATURE = 0
    SCENARIO = 1
    STEP = 2


def extract_test_result(html_report: str, type: ResultType) -> TestResult:
    html_id_mapping = {
        ResultType.FEATURE: "feature_totals",
        ResultType.SCENARIO: "scenario_totals",
        ResultType.STEP: "step_totals",
    }
    result = TestResult()
    soup = BeautifulSoup(html_report, "html.parser")
    result_element = soup.find(id=html_id_mapping[type])

    if result_element != None:
        text = result_element.getText()
        passed_group = re.search("passed: (\d+)", text)
        failed_group = re.search("failed: (\d+)", text)
        skipped_group = re.search("skipped: (\d+)", text)
        undefined_group = re.search("undefined: (\d+)", text)
        untested_group = re.search("untested: (\d+)", text)
        result.passed = passed_group.group(1) if passed_group else 0
        result.failed = failed_group.group(1) if failed_group else 0
        result.skipped = skipped_group.group(1) if skipped_group else 0
        result.undefined = undefined_group.group(1) if undefined_group else 0
        result.untested = untested_group.group(1) if untested_group else 0
    return result


if __name__ == "__main__":
    gl.read_company_config_files()
    arg_parser = init_argparse()
    args = arg_parser.parse_args()

    # sterilize parameters
    log_level = args.log_level
    company = args.company
    allure_report_path = gl.project_path / args.report
    rerun_path = gl.report_path / "rerun.txt"
    html_report_path = gl.report_path / "report.html"
    monitor = args.monitor
    tags = args.tags
    run_test_paths = []
    if args.test_set:
        for test_name in args.test_set:
            match_os_paths = [str(PurePath(p)) for p in TEST_SET[test_name]]
            run_test_paths += match_os_paths
    elif args.feature_path:
        match_os_paths = [str(PurePath(p)) for p in args.feature_path]
        run_test_paths = args.feature_path
    run_test_paths_cmd = " ".join(run_test_paths)

    cmd_format = f"behave {{run_test_paths_cmd}} \
-D log_level={log_level} \
-D company={company} \
-D monitor={monitor} \
-f allure -o {allure_report_path} \
-f html -o {{html_report_path}} \
-f rerun -o {{rerun_path}} \
--tags={tags} \
-f color --no-logcapture --no-capture --no-capture-stderr --no-skipped"

    rerun_paths: list[Path] = []
    if args.parallel_cnt >= 2:
        rerun_paths = run_parallel_test(
            cmd_format=cmd_format,
            max_parallel_cnt=args.parallel_cnt,
            test_set=run_test_paths,
            rerun_dir_path=gl.report_path,
            html_dir_path=gl.report_path,
            timeout_ratio=args.timeout_ratio,
            default_runtime=args.def_runtime,
        )
    else:
        cmd = cmd_format.format(
            run_test_paths_cmd=run_test_paths_cmd,
            html_report_path=html_report_path,
            rerun_path=rerun_path,
        )
        os.system(cmd)
        rerun_paths.append(rerun_path)

    # parse html report to get num of passed, failed, untested tests
    # with html_report_path.open() as f:
    #     html_report = f.read()

    # feature_result = extract_test_result(html_report, ResultType.FEATURE)
    # scenario_result = extract_test_result(html_report, ResultType.SCENARIO)
    # step_result = extract_test_result(html_report, ResultType.STEP)

    # if step_result.passed == step_result.failed == 0 and \
    #     step_result.untested != 0:
    #     sys.exit("WARRNING: There is no test run")
    # elif step_result.untested != 0:
    #     sys.exit("WARRNING: Occur errors before testing (Maybe has a HOOK-ERROR)")

    if rerun_path.is_file():
        with rerun_path.open() as f:
            failed_feature_text = f.read()
        if failed_feature_text != None:
            sys.exit("ERROR: There are testcases failed")
