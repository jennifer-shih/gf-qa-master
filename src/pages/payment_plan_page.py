from selenium.webdriver.common.by import By

from src.elements import *


class PaymentPlanPage:
    payment_plan_no_input = Input((By.XPATH, "//input[@formcontrolname='payment_plan_no']"))
