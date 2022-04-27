from selenium.webdriver.common.by import By

from src.elements import *


class AWBNoMngPage:
    new_awb_no_range_button = Button((By.XPATH, "//button[@ng-click='vm.addAwbNoRange()']"))
    delete_button = Button((By.XPATH, "//button[@name='delete_awb_no_range']"))
    title_label = Label((By.XPATH, "//div[@class='portlet-title']/div[contains(@class,'caption')]/span"))
    save_fail_msg_by_serial_num_large_than_1000_label = Label((By.XPATH, "//div[contains(@class,'alert')][contains(.,'CloseThe range of the serial numbers cannot be larger than 1000. Please edit and try again.')]"))
    class DeleteModal:
        ok_button = Button((By.XPATH, "//div[@class='modal-content']//button[@ng-click='ok()']"))
        cancel_button = Button((By.XPATH, "//div[@class='modal-content']//button[@ng-click='cancel()']"))
        message_label = Label((By.XPATH, "//div[@class='modal-content']//*[@ng-bind-html='msg']"))

    class AWBRanges:
        _rows = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return '//tbody//tr[@ng-repeat="r in vm.awbNoRanges.data_list"][{0}]{1}'.format(index, xpath)

            self.checked_checkbox = Checkbox((By.XPATH, ROW_XPATH("//input[@ng-model='r.__checked']")))
            self.created_date_label = Label((By.XPATH, ROW_XPATH('//td[contains(@ng-bind, "r.data.created_at")]')))
            self.carrier_autocomplete = Autocomplete((By.XPATH, ROW_XPATH('//hc-tp-select[@ng-model="r.data.carrier"]')),
                                    (By.XPATH, '//ng-dropdown-panel//input'),
                                    advance_locator = (By.XPATH, '//ng-dropdown-panel//span[.="Advance"]'),
                                    new_locator = (By.XPATH, '//ng-dropdown-panel//button[./i[contains(@class, "fa-plus")]]'),
                                    hyper_link_locator = (By.XPATH, ROW_XPATH('//hc-tp-select[@ng-model="r.data.carrier"]//i[contains(@class, "icon-share-alt")]')),
                                    clear_locator = (By.XPATH, ROW_XPATH('//hc-tp-select[@ng-model="r.data.carrier"]//span[@title="Clear all"]')))
            self.prefix_label = Label((By.XPATH, ROW_XPATH('//td[@ng-bind="r.data.carrier.prefix"]')))
            self.begin_no_input = Input((By.XPATH, ROW_XPATH('//input[@ng-model="r.data.begin_no"]')))
            self.end_no_input = Input((By.XPATH, ROW_XPATH('//input[@ng-model="r.data.end_no"]')))
            self.latest_assigned_no_label = Label((By.XPATH, ROW_XPATH("//td[@ng-bind='r.data.current_assigned_no']")))
            self.remark_input = Input((By.XPATH, ROW_XPATH('//input[@ng-model="r.data.remark"]')))

        @staticmethod
        def get_len():
            return Driver.num_of_element("//tbody//tr[@ng-repeat='r in vm.awbNoRanges.data_list']")

    class TradePartnerModal:
        def MO_XPATH(xpath):
            return "//modal-container{0}".format(xpath)

        keyword_input = Input((By.XPATH, MO_XPATH("//input[@formcontrolname='keyword']")))
        search_button = Button((By.XPATH, MO_XPATH("//button[.='Search']")))

        ok_button = Button((By.XPATH, MO_XPATH("//button[.='OK']")))

        class SearchResult:
            _rows = {}

            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                index = int(index)
                def MO_XPATH(xpath):
                    return "//modal-container{0}".format(xpath)
                def ROW_XPATH(xpath):
                    return MO_XPATH("//tbody//tr{0}".format(xpath))

                self.name_button = Button((By.XPATH, '({})[{}]'.format(ROW_XPATH("//td[1]"), index)))

    class SetupAirCarrierPrefixModal:
        def MO_XPATH(xpath):
            return "//div[@class='modal-dialog']{0}".format(xpath)

        prefix_input = Input((By.XPATH, MO_XPATH("//input[@ng-model='vm.prefix']")))
        cancel_button = Button((By.XPATH, MO_XPATH("//button[.='Cancel']")))
        save_button = Button((By.XPATH, MO_XPATH("//button[.='Save']")))
