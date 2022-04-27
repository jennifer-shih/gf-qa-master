import sys

sys.path.append(".")
import unittest
from datetime import datetime
from pathlib import Path

import yaml

import chromedriver.chrome_helper as chrome_helper
import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.script import login_as, wait_reset_db_process_done
from src.helper.timer import PatchDBTimer

TIME = datetime.now()


class ResetBackupDB(unittest.TestCase):
    def __init__(self, test_name, test_server, monitor, backup_path):
        super(ResetBackupDB, self).__init__(test_name)
        self.TEST_NAME = test_name
        self.SERVER_URL = test_server
        self.MONITOR = monitor
        self.BACKUP_PATH = backup_path

    def setUp(self) -> None:
        gl.read_company_config_files()
        gl.company = "BugRegression"
        gl.init_url(custom_base_url=self.SERVER_URL)
        chrome_helper.check_browser_driver_available()
        Driver("Chrome_1", chrome_helper.get_driver_path(), monitor=self.MONITOR)
        print("\n")  # for verbosity=2 formatting

    def tearDown(self) -> None:
        Driver.quit()

    def test_reset_db(self):
        Logger.getLogger().info("Start Test: [{0}]".format(self._testMethodName))
        Logger.getLogger().info("Backup File Path: {}".format(self.BACKUP_PATH))

        # # go to reset backup db page
        folders = [i.strip() for i in self.BACKUP_PATH.split("/")][:-1]
        backup_file = [i.strip() for i in self.BACKUP_PATH.split("/")][-1]
        backup_folder_url = gl.URL.DASHBOARD + "/superuser/super/reset-backups-db/?prefix={0}".format("/".join(folders))
        Driver.open(backup_folder_url)
        login_as("super_admin")

        # find the specific reset button
        Pages.ResetBackupsDBPage.reset_button(backup_file).click()
        Pages.ResetBackupsDBPage.reset_db_save_button.click()
        wait_reset_db_process_done()

        # patch db (for upsell)
        patch_name = "patch_upsell_read_all_feeds"
        with open(gl.patch_db_msg_path, encoding="UTF-8") as f:
            msgs = yaml.safe_load(f)
        Driver.open(gl.URL.PATCH_DB)
        timer = PatchDBTimer(msgs[patch_name], 30)
        Pages.PatchDBPage.patch_apply_button(patch_name).click()
        Pages.PatchDBPage.proceed_button.click()
        timer.start()
        assert (
            timer.is_passed()
        ), f"Patch upsell read all feads fail\nConsole textarea:\n{timer.get_console_textarea_text()}"


def cmd_option():
    """
    test_server: testing url                                e.g., https://fms-stage-stress-1.gofreight.co
    monitor: driver monitor mode.                           e.g., 0
    backup_path                                             e.g., aws-sfi-gofreight/fms/backup.tar.gz-20211212
    """
    args_map = {}

    for arg in sys.argv[1:]:
        key, val = arg.split("=")
        args_map[key.lower()] = val
        Logger.getLogger().debug("[{}] = [{}]".format(key, val))

    Logger.getLogger().info(" Test Parametes ".center(80, "*"))
    Logger.getLogger().info("test_server: {0}".format(args_map["test_server"]).ljust(80))
    Logger.getLogger().info("backup_path: {0}".format(args_map["backup_path"]).ljust(80))
    Logger.getLogger().info("monitor: {0}".format(args_map["monitor"]).ljust(80))
    Logger.getLogger().info("*" * 80)

    return args_map


if __name__ == "__main__":
    Logger(
        name="ResetLatestBackupDB",
        level="debug",
        path=Path(__file__).parent
        / "log"
        / Path(Path(__file__).stem + "_" + TIME.strftime("%Y-%m-%d_%H_%M_%S") + ".log"),
    )

    options = cmd_option()
    suite = unittest.TestSuite()
    suite.addTest(
        ResetBackupDB(
            test_name="test_reset_db",
            backup_path=options["backup_path"],
            test_server=options["test_server"],
            monitor=options["monitor"],
        )
    )

    unittest.TextTestRunner(verbosity=2).run(suite)
