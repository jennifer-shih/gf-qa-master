from selenium.webdriver.common.by import By

from src.elements import *


class DocPreviewToolBar:
    pdf_button = Button((By.XPATH, "//button[@class='pdf']"))
    excel_button = Button((By.XPATH, "//button[@class='excel']"))
    print_button = Button((By.XPATH, "//button[@class='print']"))
    mail_button = Button((By.XPATH, "//button[@class='mail']"))
