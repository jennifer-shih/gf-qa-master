import re
from datetime import date, timedelta

import requests
from behave import *

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.script import login_as, wait_reset_db_process_done


@When("the user resets DB to {company_name}'s latest one")
def step_impl(contex, company_name):
    login_as("Super Admin")
    folder = "aws-{0}-gofreight/fms".format(company_name.lower())
    backup_folder_url = gl.URL.DASHBOARD + "/superuser/super/reset-backups-db/?prefix={0}".format(folder)
    Driver.open(backup_folder_url)
    Pages.Common.spin_bar.gone()

    # Calculate the file name of the DB of yesterday
    # Our integration test trigger time is at 3 A.M, but SFI need more time to backup the last day DB.
    # So we use the day before yesterday DB to reset.
    if gl.company == "SFI":
        # the_day_before_yesterday = date.today() - timedelta(days=2)
        the_day_before_yesterday = date.today() - timedelta(days=10)
        file_name = f'backup.tar.gz-{ the_day_before_yesterday.strftime("%Y%m%d") }'
    else:
        # yesterday = date.today() - timedelta(days=1)
        yesterday = date.today() - timedelta(days=10)
        file_name = f'backup.sql.gz-{ yesterday.strftime("%Y%m%d") }'

    Pages.ResetBackupsDBPage.reset_button(file_name).click()
    Pages.ResetBackupsDBPage.reset_db_save_button.click()
    wait_reset_db_process_done()


@When("the user resets DB to {company_name}'s latest one by Jenkins")
def step_impl(contex, company_name):
    login_as("Super Admin")
    folder = "aws-{0}-gofreight/fms".format(company_name.lower())
    server_name = re.match("https://(.*).gofreight.co", gl.URL.DASHBOARD).group(1)

    # Calculate the file name of the DB of yesterday
    # Our integration test trigger time is at 3 A.M, but SFI need more time to backup the last day DB.
    # So we use the day before yesterday DB to reset.
    if gl.company == "SFI":
        the_day_before_yesterday = date.today() - timedelta(days=2)
        file_name = f'backup.tar.gz-{ the_day_before_yesterday.strftime("%Y%m%d") }'
    else:
        yesterday = date.today() - timedelta(days=1)
        file_name = f'backup.sql.gz-{ yesterday.strftime("%Y%m%d") }'

    user = "restoredb"
    api_token = "11ed0a52d54a4559e3a2a0193b4b96b416"
    job_token = "BxKBBg8aTrQdL79mhuky94BpbFV7YRHU"
    host = "jenkins.hardcoretech.co"
    sql_file_path = folder + "/" + file_name
    job_name = server_name + "-restore-db"
    tenant_id = re.match("fms-(.*)", server_name).group(1)

    url = "https://{USER}:{API_TOKEN}@{HOST}/view/fms-stage/job/{JOB_NAME}/buildWithParameters?token={JOB_TOKEN}&s3_sql_file_path={SQL_FILE_PATH}&wait_timeout=3600&tenant_id={TENANT_ID}".format(
        USER=user,
        API_TOKEN=api_token,
        HOST=host,
        JOB_NAME=job_name,
        JOB_TOKEN=job_token,
        SQL_FILE_PATH=sql_file_path,
        TENANT_ID=tenant_id,
    )

    response = requests.request("GET", url)
    assert response.status_code == 201, f"Fail to reset db by Jenkins build, response code: {response.status_code}"


@Given("DB is reset to {path}")
@When("the user resets DB to {path}")
def step_impl(context, path):
    login_as("Super Admin")
    folders = [i.strip() for i in path.split("/")][:-1]
    backup_file = [i.strip() for i in path.split("/")][-1]
    backup_folder_url = gl.URL.DASHBOARD + "/superuser/super/reset-backups-db/?prefix={0}".format("/".join(folders))
    Driver.open(backup_folder_url)
    Pages.ResetBackupsDBPage.reset_button(backup_file).click()
    Pages.ResetBackupsDBPage.reset_db_save_button.click()
    wait_reset_db_process_done()
