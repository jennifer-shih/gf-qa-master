import sys
from pathlib import Path

import allure

import chromedriver.chrome_helper as chrome_helper
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.function import check_company_is_consistent
from src.helper.log import Logger
from src.variables import VariablePool


def before_all(context):
    # cmd variables
    context.LOG_LEVEL = context.config.userdata.get("log_level", gl.log_level)
    context.COMPANY = context.config.userdata.get("company", gl.company)
    gl.monitor = context.config.userdata.get("monitor", gl.monitor)
    # import files and variables setting
    gl.read_company_config_files()
    gl.company = context.COMPANY
    gl.init_url()
    # check chromedriver
    chrome_helper.check_browser_driver_available()


def before_feature(context, feature):
    log_level = context.LOG_LEVEL
    company = context.COMPANY

    feature_path = Path(feature.filename)
    feature_file_name = feature_path.stem
    feature_folder_name = feature_path.parent
    t = str(gl.log_path / feature_folder_name / feature_file_name) + ".log"
    Logger(name=feature_file_name, level=log_level, path=t)
    Logger.getLogger().info(" Test Suite Settings ".center(80, "*"))
    Logger.getLogger().info("Features: {0}".format(feature.name).ljust(80))
    Logger.getLogger().info("Tags: {0}".format(context.config.tags).ljust(80))
    Logger.getLogger().info("Company: {0}".format(company).ljust(80))
    Logger.getLogger().info("Log level: {0}".format(log_level).ljust(80))
    Logger.getLogger().info("Test Server: {0}".format(gl.URL.DASHBOARD).ljust(80))
    Logger.getLogger().info("*" * 80)
    print("\n")

    gl.init_gofreight_config()
    check_company_is_consistent()


def before_scenario(context, scenario):
    # Initialize the browser
    Driver("Chrome_1", chrome_helper.get_driver_path(), monitor=gl.monitor)

    # 如果GoFreight在更新, 則中斷script
    if Driver.is_text_in_page_source("Server under Maintenance"):
        Driver.quit()
        sys.exit("Service under maintenance. Please retry after a few time.")
    context._vp = VariablePool()


def before_step(context, step):
    context.step_name = step.name


def after_feature(context, feature):
    pass

    # add log file to allure report
    # allure.attach.file(
    #         source=str(gl.log_path/Logger.getName()/(Logger.getName()+'.log')),
    #         name=str(feature.name),
    #         extension="txt")


def after_scenario(context, scenario):
    # Close the browser
    Driver.quit()


def after_step(context, step):
    # if step failed then take a screenshot
    if step.status == "failed":
        screenshot_path = (gl.log_path / "allure" / "error.png").as_posix()
        Driver.get_screenshot_for_all_windows(screenshot_path)
        with open(screenshot_path, "rb") as image:
            file = image.read()
            byte_array = bytearray(file)

        allure.attach(
            byte_array,
            name=str(Logger.getName() + step.name),
            attachment_type=allure.attachment_type.PNG,
        )

        error_logs = Driver.get_console_error_logs()
        Logger.getLogger().error(f"There are errors in broswer console.\n {error_logs}")
