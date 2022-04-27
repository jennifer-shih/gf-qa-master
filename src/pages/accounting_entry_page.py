from time import sleep

from selenium.webdriver.common.by import By

from src.drivers.driver import Driver
from src.elements import *


class AREntry:
    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))
    save_as_draft_button = Button((By.XPATH, r"//button[@ng-click='vm.save({asDraft: true})']"))
    save_and_create_another = Button((By.XPATH, "//button[@ng-click=\"vm.save({redirect: 'new_entry'})\"]"))

    bill_to_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='bill_to']"), (By.XPATH, "//hc-tp-select[@name='bill_to']//input[@type='search']"))
    attention_to_input = Input((By.XPATH, "//input[@ng-model='vm.inv.data.attention_to']"))
    ship_to_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='ship_to']"), (By.XPATH, "//hc-tp-select[@name='ship_to']//input[@type='search']"))
    post_date_datepicker = Datepicker((By.XPATH, "//input[@name='post_date']"))
    invoice_date_datepicker = Datepicker((By.XPATH, "//input[@name='invoice_date']"))
    due_date_datepicker = Datepicker((By.XPATH, "//input[@name='due_date']"))

    new_freight_button = Button((By.XPATH, "//button[@ng-click='vm.addNewFreight()']"))

    class freight:
        _rows = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//div[@class='ui-grid-canvas']/div[{0}]{1}".format(index, xpath)

            self.select_checkbox = Checkbox((By.XPATH, ROW_XPATH("""//label[@model="row['entity']['__checked']"]""")))
            self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//hc-billing-select")), (By.XPATH, "//body/div[@name='frt_billing']//input[@type='search']"))
            self.freight_description_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['name']"]""")))
            self.p_c_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['freight_term']"]""")))
            self.type_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['link_type']"]""")))
            self.unit_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['unit']"]""")))
            self.currency_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['currency']"]""")))
            self.volume_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='row.entity.volume']")))
            self.rate_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['rate']"]""")))
            self.amount_label = Label((By.XPATH, ROW_XPATH("""//div[@ng-bind="row['entity']['currency_amount']"]""")))
            self.agent_amount_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['dc_amount']"]""")))
            self.status_status_icon = StatusIcon((By.XPATH, ROW_XPATH("//a[@uib-tooltip]/..")),{
                "Wating": ROW_XPATH("//span[text()='Waiting']"),
                "Linked": ROW_XPATH("//span[text()='Linked']"),
                "Re-Linking": ROW_XPATH("//span[text()='Re-Linking']"),
                "Matched": ROW_XPATH("//span[text()='Matched']"),
                "No Match": ROW_XPATH("//span[text()='No Match']")
            })

        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//div[@class='ui-grid-canvas']/div")


class DCNoteEntry:
    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))
    save_as_draft_button = Button((By.XPATH, r"//button[@ng-click='vm.save({asDraft: true})']"))
    save_and_create_another = Button((By.XPATH, "//button[@ng-click=\"vm.save({redirect: 'new_entry'})\"]"))

    agent_name_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='vendor']"), (By.XPATH, "//hc-tp-select[@name='vendor']//input[@type='search']"))
    attention_to_input = Input((By.XPATH, "//input[@ng-model='vm.inv.data.attention_to']"))
    post_date_datepicker = Datepicker((By.XPATH, "//input[@name='post_date']"))
    invoice_date_datepicker = Datepicker((By.XPATH, "//input[@name='invoice_date']"))
    due_date_datepicker = Datepicker((By.XPATH, "//input[@name='due_date']"))

    new_freight_button = Button((By.XPATH, "//button[@ng-click='vm.addNewFreight()']"))
    load_and_link_button = Button((By.XPATH, "//button[@ng-click='vm.loadLoadableFreight()']"))

    class freight:
        _rows = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//div[@class='ui-grid-canvas']/div[{0}]{1}".format(index, xpath)

            self.select_checkbox = Checkbox((By.XPATH, ROW_XPATH("""//label[@model="row['entity']['__checked']"]""")))
            self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//hc-billing-select")), (By.XPATH, "//body/div[@name='frt_billing']//input[@type='search']"))
            self.freight_description_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['name']"]""")))
            self.type_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['type']"]""")))
            self.p_c_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['freight_term']"]""")))
            self.unit_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['unit']"]""")))
            self.currency_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['currency']"]""")))
            self.volume_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['volume']"]""")))
            self.rate_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['rate']"]""")))
            self.amount_label = Label((By.XPATH, ROW_XPATH("""//div[@ng-bind="row['entity']['currency_amount']"]""")))
            self.agent_amount_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['dc_amount']"]""")))
            self.status_status_icon = StatusIcon((By.XPATH, ROW_XPATH("//a[@uib-tooltip]/..")),{
                "Matched": ROW_XPATH("//span[@uib-tooltip='Matched']"),
                "Linking": ROW_XPATH("//span[@uib-tooltip=""]"),
                "Linked": ROW_XPATH("//a[@uib-tooltip='Linked']"),
                "No Match": ROW_XPATH("//span[@uib-tooltip='No Match']")
            })

        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//div[@class='ui-grid-canvas']/div")

class APEntry:
    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))
    save_as_draft_button = Button((By.XPATH, r"//button[@ng-click='vm.save({asDraft: true})']"))
    save_and_create_another = Button((By.XPATH, "//button[@ng-click=\"vm.save({redirect: 'new_entry'})\"]"))

    vendor_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='vendor']"), (By.XPATH, "//hc-tp-select[@name='vendor']//input[@type='search']"))
    attention_to_input = Input((By.XPATH, "//input[@ng-model='vm.inv.data.attention_to']"))
    post_date_datepicker = Datepicker((By.XPATH, "//input[@name='post_date']"))
    invoice_date_datepicker = Datepicker((By.XPATH, "//input[@name='invoice_date']"))
    due_date_datepicker = Datepicker((By.XPATH, "//input[@name='due_date']"))

    new_freight_button = Button((By.XPATH, "//button[@ng-click='vm.addNewFreight()']"))

    class freight:
        _rows = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//div[@class='ui-grid-canvas']/div[{0}]{1}".format(index, xpath)

            self.select_checkbox = Checkbox((By.XPATH, ROW_XPATH("""//label[@model="row['entity']['__checked']"]""")))
            self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//hc-billing-select")), (By.XPATH, "//body/div[@name='frt_billing']//input[@type='search']"))
            self.freight_description_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['name']"]""")))
            self.p_c_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['freight_term']"]""")))
            self.type_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['link_type']"]""")))
            self.unit_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['unit']"]""")))
            self.currency_select = Select((By.XPATH, ROW_XPATH("""//select[@ng-model="row['entity']['currency']"]""")))
            self.volume_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='row.entity.volume']")))
            self.rate_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['rate']"]""")))
            self.amount_label = Label((By.XPATH, ROW_XPATH("""//div[@ng-bind="row['entity']['currency_amount']"]""")))
            self.agent_amount_input = Input((By.XPATH, ROW_XPATH("""//input[@ng-model="row['entity']['dc_amount']"]""")))
            self.status_status_icon = StatusIcon((By.XPATH, ROW_XPATH("//a[@uib-tooltip]/..")),{
                "Wating": ROW_XPATH("//span[text()='Waiting']"),
                "Linked": ROW_XPATH("//span[text()='Linked']"),
                "Re-Linking": ROW_XPATH("//span[text()='Re-Linking']"),
                "Matched": ROW_XPATH("//span[text()='Matched']"),
                "No Match": ROW_XPATH("//span[text()='No Match']")
            })

        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//div[@class='ui-grid-canvas']/div")
