import json
from collections import OrderedDict
from pathlib import Path
from time import sleep

from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.log import Logger
from src.helper.transfer import transfer_keyword
from src.models import VerifiedModel
from src.pages import LoginPage, PageHeader


def login_as(role, office=""):
    """
    role:
        Operator
        Super Admin
        General Manager
        Accounting
        Accounting Manager
        Salesperson
    """
    suffix_office = ("_" + office.lower()) if office else ""
    # 如果不在 GoFreight 網頁，導頁到 GoFreight 首頁
    if Driver.is_url_match(gl.URL.DASHBOARD) is False:
        Driver.open(gl.URL.DASHBOARD)

    # 未登入，在登入畫面
    if Driver.is_url_match("login"):
        role_account_map = {
            "operator": {
                "username": gl.companyConfig[gl.company]["op" + suffix_office],
                "password": gl.companyConfig[gl.company]["password"],
            },
            "super_admin": {
                "username": gl.companyConfig[gl.company]["sa"],
                "password": gl.companyConfig[gl.company]["sa_password"],
            },
            "general_manager": {
                "username": gl.companyConfig[gl.company]["gm" + suffix_office],
                "password": gl.companyConfig[gl.company]["password"],
            },
            "accounting": {
                "username": gl.companyConfig[gl.company]["acc" + suffix_office],
                "password": gl.companyConfig[gl.company]["password"],
            },
            "accounting_manager": {
                "username": gl.companyConfig[gl.company]["am" + suffix_office],
                "password": gl.companyConfig[gl.company]["password"],
            },
            "salesperson": {
                "username": gl.companyConfig[gl.company]["sales" + suffix_office],
                "password": gl.companyConfig[gl.company]["password"],
            },
        }
        role_account = role_account_map[transfer_keyword(role)]
        LoginPage.username_input.input(role_account["username"])
        LoginPage.password_input.input(role_account["password"])
        LoginPage.login_button.click()

        # 將登入的user info 存到globalparameter
        gl.init_user_info(role_account["username"], role_account["password"])

    # 已登入，檢查 username
    else:
        nickname_map = {
            "operator": "op",
            "super_admin": "super",
            "general_manager": "gm",
            "accounting": "acc",
            "accounting_manager": "am",
            "salesperson": "sales",
        }
        nickname = nickname_map[transfer_keyword(role)] + suffix_office
        name = PageHeader.profile.get_value()
        # 登入的帳號錯誤，登出再登入正確的帳號
        if not nickname in name.lower():
            # redirect = Driver.get_logout_redirect_url()
            Driver.open(gl.URL.LOGOUT)
            # Driver.open(redirect)
            login_as(role, office)


def wait_reset_db_process_done():
    Logger.getLogger().info("Refresh and check login page or keep waiting")
    time_counter = 180

    while True:
        if Driver.is_text_in_page_source("Server under Maintenance"):
            Logger.getLogger().info("Show Server under Maintenance")
            sleep(10)
            time_counter -= 1
            Driver.refresh()
        elif Driver.is_text_in_page_source("502 Bad Gateway"):
            Logger.getLogger().info("Show 502 Bad Gateway")
            sleep(10)
            time_counter -= 1
            Driver.refresh()
        elif Driver.is_text_in_page_source("Internal Server Error."):
            assert False, "Reset DB Failed"
        elif Driver.is_text_in_page_source("Sign In"):
            Logger.getLogger().info("Show Login page")
            break
        else:
            sleep(10)
            Driver.refresh()
            time_counter -= 1
            if time_counter < 0:
                assert False, "Reset DB Timeout"


def input_dynamic_datas(action_table, page_class_name, excepted_filter=None) -> VerifiedModel:
    verified_model = VerifiedModel(page_class_name)

    for row in action_table:
        field = row["field"]
        attribute = row["attribute"]
        action = row["action"]
        data = [row["data"]]

        if excepted_filter != None and excepted_filter(verified_model, field) == True:
            continue

        # input data
        exec_act_cmd(field, attribute, action, data, page=page_class_name)

        # get data in field (GoFrieght有autocomoplete的功能，所以使用者輸入的值並不等於field上最後呈現和儲存的值)
        data_in_field = exec_act_cmd(field, attribute, "get_value", page=page_class_name)

        answer = data_in_field
        verified_model.add(field=field, attribute=attribute, data=answer)

    return verified_model


#! Warning !! Use this function very sparingly
def save_shipment_info_to_local_file(datas: dict, path: Path, need_to_delete_existed_file=False):
    if not gl.info_path.exists():
        gl.info_path.mkdir(parents=True)

    if not need_to_delete_existed_file:
        try:
            with path.open(mode="r") as file:
                old_datas = json.load(file, object_pairs_hook=OrderedDict)
                datas = {**old_datas, **datas}
        except:
            pass

    with path.open(mode="w") as file:
        json.dump(datas, file, indent=2)
