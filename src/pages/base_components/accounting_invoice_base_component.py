from selenium.webdriver.common.by import By

from src.elements import *


class BaseAccountingInvoiceBasedMblAr:
    _rows = {}
    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index)
        def ROW_XPATH(xpath):
            return "//div[contains(@class, 'mbl_board')]//tr[@ng-repeat='inv in vm.invList.invoice'][{0}]{1}".format(index, xpath)

        self.reference_no_link = Link((By.XPATH, ROW_XPATH("//a[contains(@class, 'link')]")))
        self.party_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.trade_partner.name']")))
        self.revenue_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvAmountBeforeTax(inv) | number:2']")))
        self.cost_label = Label((By.XPATH, ROW_XPATH("/td[contains(@class, 'text-right')][2]")))
        self.balance_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvBalance(inv) | number:2']")))
        self.status_label = Label((By.XPATH, ROW_XPATH("/td[7]")))
        self.date_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.invoice_date | date_format']")))
        self.email_button = Button((By.XPATH, ROW_XPATH("/td[9]/div/a")))
        self.action_button = Button((By.XPATH, ROW_XPATH("/td[10]/div/a")))


class BaseAccountingInvoiceBasedMblDc:
    _rows = {}
    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index)
        def ROW_XPATH(xpath):
            return "//div[contains(@class, 'mbl_board')]//tr[@ng-repeat='inv in vm.invList.dc'][{0}]/td{1}".format(index, xpath)

        self.reference_no_link = Link((By.XPATH, ROW_XPATH("/a[contains(@class, 'link')]")))
        self.party_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.trade_partner.name']")))
        self.revenue_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvAmountBeforeTax(inv) | number:2']")))
        self.cost_label = Label((By.XPATH, ROW_XPATH("/td[contains(@class, 'text-right')][2]")))
        self.balance_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvBalance(inv) | number:2']")))
        self.status_label = Label((By.XPATH, ROW_XPATH("/td[7]")))
        self.date_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.invoice_date | date_format']")))
        self.email_button = Button((By.XPATH, ROW_XPATH("/td[9]/div/a")))
        self.action_button = Button((By.XPATH, ROW_XPATH("/td[10]/div/a")))


class BaseAccountingInvoiceBasedMblAp:
    _rows = {}
    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index)
        def ROW_XPATH(xpath):
            return "//div[contains(@class, 'mbl_board')]//tr[@ng-repeat='inv in vm.invList.ap'][{0}]/td{1}".format(index, xpath)

        self.reference_no_link = Link((By.XPATH, ROW_XPATH("/a[contains(@class, 'link')]")))
        self.party_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.trade_partner.name']")))
        self.revenue_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvAmountBeforeTax(inv) | number:2']")))
        self.cost_label = Label((By.XPATH, ROW_XPATH("/td[contains(@class, 'text-right')][2]")))
        self.balance_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvBalance(inv) | number:2']")))
        self.status_label = Label((By.XPATH, ROW_XPATH("/td[7]")))
        self.date_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.invoice_date | date_format']")))
        self.email_button = Button((By.XPATH, ROW_XPATH("/td[9]/div/a")))
        self.action_button = Button((By.XPATH, ROW_XPATH("/td[10]/div/a")))


class BaseAccountingInvoiceBasedHblAr:
    _rows = {}
    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index)
        def ROW_XPATH(xpath):
            return "//div[contains(@class, 'hbl_board')]//tr[@ng-repeat='inv in vm.invList.invoice'][{0}]{1}".format(index, xpath)

        self.reference_no_link = Link((By.XPATH, ROW_XPATH("//a[contains(@class, 'link')]")))
        self.party_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.trade_partner.name']")))
        self.revenue_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvAmountBeforeTax(inv) | number:2']")))
        self.cost_label = Label((By.XPATH, ROW_XPATH("/td[contains(@class, 'text-right')][2]")))
        self.balance_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvBalance(inv) | number:2']")))
        self.status_label = Label((By.XPATH, ROW_XPATH("/td[7]")))
        self.date_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.invoice_date | date_format']")))
        self.email_button = Button((By.XPATH, ROW_XPATH("/td[9]/div/a")))
        self.action_button = Button((By.XPATH, ROW_XPATH("/td[10]/div/a")))


class BaseAccountingInvoiceBasedHblDc:
    _rows = {}
    def __new__(cls, index=1):
        index = int(index) - 1
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index)
        def ROW_XPATH(xpath):
            return "//div[contains(@class, 'hbl_board')]//tr[@ng-repeat='inv in vm.invList.dc'][{0}]/td{1}".format(index, xpath)

        self.reference_no_link = Link((By.XPATH, ROW_XPATH("/a[contains(@class, 'link')]")))
        self.party_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.trade_partner.name']")))
        self.revenue_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvAmountBeforeTax(inv) | number:2']")))
        self.cost_label = Label((By.XPATH, ROW_XPATH("/td[contains(@class, 'text-right')][2]")))
        self.balance_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvBalance(inv) | number:2']")))
        self.status_label = Label((By.XPATH, ROW_XPATH("/td[7]")))
        self.date_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.invoice_date | date_format']")))
        self.email_button = Button((By.XPATH, ROW_XPATH("/td[9]/div/a")))
        self.action_button = Button((By.XPATH, ROW_XPATH("/td[10]/div/a")))


class BaseAccountingInvoiceBasedHblAp:
    _rows = {}
    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index)
        def ROW_XPATH(xpath):
            return "//div[contains(@class, 'hbl_board')]//tr[@ng-repeat='inv in vm.invList.ap'][{0}]/td{1}".format(index, xpath)

        self.reference_no_link = Link((By.XPATH, ROW_XPATH("/a[contains(@class, 'link')]")))
        self.party_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.trade_partner.name']")))
        self.revenue_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvAmountBeforeTax(inv) | number:2']")))
        self.cost_label = Label((By.XPATH, ROW_XPATH("/td[contains(@class, 'text-right')][2]")))
        self.balance_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='vm.getInvBalance(inv) | number:2']")))
        self.status_label = Label((By.XPATH, ROW_XPATH("/td[7]")))
        self.date_label = Label((By.XPATH, ROW_XPATH("/*[@ng-bind='inv.invoice_date | date_format']")))
        self.email_button = Button((By.XPATH, ROW_XPATH("/td[9]/div/a")))
        self.action_button = Button((By.XPATH, ROW_XPATH("/td[10]/div/a")))
