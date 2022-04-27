from selenium.webdriver.common.by import By

from src.elements import *


class LoginPage:
    username_input = Input((By.XPATH, '//*[@id="username"]'))
    password_input = Input((By.NAME, 'password'))
    login_button = Button((By.XPATH, "//input[@type='submit']"))
    login_fail_label = Label((By.XPATH, "//div[contains(@class, 'text-danger')][contains(@class, 'login-tip')]"))
    # recaptcha_iframe = IFrame((By.XPATH, "//iframe[@title=contains(.,'reCAPTCHA')]"))
