from selenium.webdriver.common.by import By

from src.elements import *


class ResetBackupsDBPage:
    db_table = Element((By.XPATH, "//table[@class='table table-fixed table-bordered table-striped table-hover table-col-link table-data']"))
    aws_sfi_gofreight_link = Link((By.XPATH, "//a[contains(.,'aws-sfi-gofreight')]"))
    aws_lohan_gofreight_link = Link((By.XPATH, "//a[contains(.,'aws-lohan-gofreight')]"))
    aws_ewi_gofreight_link = Link((By.XPATH, "//a[contains(.,'aws-ewi-gofreight')]") )
    aws_olc_gofreight_link = Link((By.XPATH, "//a[contains(.,'aws-olc-gofreight')]"))
    aws_ssc_gofreight_link = Link((By.XPATH, "//a[contains(.,'aws-ssc-gofreight')]"))
    aws_cfm_gofreight_link = Link((By.XPATH, "//a[contains(.,'aws-cfm-gofreight')]"))
    fms_link = Link((By.XPATH, "//a[contains(.,'fms')]"))

    def reset_button(name):
        return Button((By.XPATH, "//span[contains(text(),'{0}')]//following::td[2]/button[text()='Reset DB']".format(name)))

    reset_db_save_button = Button((By.XPATH, "//button[@ng-click='save()']"))
