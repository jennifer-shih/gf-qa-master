from time import sleep

from behave import *

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import trnas_ele_cmd
from src.helper.log import Logger


@Given("the user is on '{page_name}' page")
def step_impl(context, page_name):
    url = gl.URL.to_url(page_name=page_name)

    if Driver.is_url_fully_match(url) == False:
        Driver.open(url)

    Pages.Common.spin_bar.gone()


@When("go to 'Reset Backups DB' page")
def step_impl(context):
    try:
        Pages.NavigatorBar.super_user.hover()
        Pages.NavigatorBar.super_user.click()
        Pages.NavigatorBar.super_user_super.click()
        Pages.NavigatorBar.super_user_super_reset_backups_db.click()
    except Exception:
        url = gl.URL.RESET_BACKUPS_DB
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to url:[{0}] directly".format(url))


@Then("'Reset Backups DB' page show normally")
def step_impl(context):
    assert Pages.ResetBackupsDBPage.db_table.is_enable(timeout=10) is True, "Loading [Reset Backups DB] page timeout"


@When("go to 'Office Management' page")
def step_impl(context):
    try:
        Pages.NavigatorBar.super_user.hover()
        Pages.NavigatorBar.super_user.click()
        Pages.NavigatorBar.super_user_admin.click()
        Pages.NavigatorBar.super_user_admin_office_management.click()
    except Exception:
        url = gl.URL.OFFICE_MANAGEMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to url:[{0}] directly".format(url))

    assert Pages.OfficeMngPage.lax_link.is_enable(timeout=10) is True, "Loading [Office Management] page timeout"


@When("the user go to 'Office Entry' page")
def step_impl(context):
    element = trnas_ele_cmd(gl.company, "link", page_class_name="Pages.OfficeMngPage")
    element.click()
    Pages.Common.spin_bar.gone()


@Then("'Office Entry' page show normally")
def step_impl(context):
    assert Pages.OfficeMngPage.save_button.is_enable(timeout=10) is True, "Loading [Office Entry] page timeout"


@When("the user browse to 'New Shipment of Ocean Import' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.ocean_import.hover()
        Pages.NavigatorBar.ocean_import.click()
        Pages.NavigatorBar.ocean_import_new_shipment.click()
    except:
        url = gl.URL.OI_NEW_SHIPMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Shipment of Ocean Import' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert Pages.OIBasicTab.MBL.title.is_enable(timeout=10) is True, "Loading new shipment page is timeout"
    assert Pages.OIBasicTab.MBL.file_no_input.is_visible(timeout=10) is True, "Loading new shipment page is timeout"


@When("the user browse to 'New Shipment of Ocean Export' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.ocean_export.hover()
        Pages.NavigatorBar.ocean_export.click()
        Pages.NavigatorBar.ocean_export_new_shipment.click()
    except:
        url = gl.URL.OE_NEW_SHIPMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Shipment of Ocean Export' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert Pages.OEBasicTab.MBL.mb_l_no_input.is_enable(timeout=10) is True, "Loading new shipment page is timeout"
    assert Pages.OEBasicTab.MBL.file_no_input.is_visible(timeout=10) is True, "Loading new shipment page is timeout"


@When("the user browse to 'New Shipment of Air Import' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.air_import.hover()
        Pages.NavigatorBar.air_import.click()
        Pages.NavigatorBar.air_import_new_shipment.click()
    except:
        url = gl.URL.AI_NEW_SHIPMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Shipment of Air Import' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert Pages.AIBasicTab.MAWB.more_button.is_visible() is True, "Loading new shipment page is timeout"
    assert Pages.AIBasicTab.MAWB.file_no_input.is_visible() is True, "Loading new shipment page is timeout"


@When("the user browse to 'New Shipment of Air Export' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.air_export.hover()
        Pages.NavigatorBar.air_export.click()
        Pages.NavigatorBar.air_export_new_shipment.click()
    except:
        url = gl.URL.AE_NEW_SHIPMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Shipment of Air Export' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert Pages.AEBasicTab.MAWB.more_button.is_visible() is True, "Loading new shipment page is timeout"
    assert Pages.AEBasicTab.MAWB.file_no_input.is_visible() is True, "Loading new shipment page is timeout"


@When("the user browse to 'New Shipment of Truck' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.truck.hover()
        Pages.NavigatorBar.truck.click()
        Pages.NavigatorBar.truck_new_shipment.click()
    except:
        url = gl.URL.TK_NEW_SHIPMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Shipment of Truck' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert Pages.TKBasicTab.MBL.more_button.is_visible() is True, "Loading new shipment page is timeout"
    assert Pages.TKBasicTab.MBL.file_no_input.is_visible() is True, "Loading new shipment page is timeout"


@When("the user browse to 'New Operation of Misc' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.misc.hover()
        Pages.NavigatorBar.misc.click()
        Pages.NavigatorBar.misc_new_operation.click()
    except:
        url = gl.URL.MS_NEW_OPERATION
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Operation of Misc' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert Pages.MiscBasicTab.MBL.more_button.is_visible() is True, "Loading new operation page is timeout"
    assert Pages.MiscBasicTab.MBL.file_no_input.is_visible() is True, "Loading new operation page is timeout"


@When("the user browse to 'Balance Sheet' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_report.hover()
        Pages.NavigatorBar.accounting_report.click()
        Pages.NavigatorBar.accounting_report_balance_sheet.hover()
        Pages.NavigatorBar.accounting_report_balance_sheet.click()
    except:
        url = gl.URL.BALANCE_SHEET
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'Balance Sheet' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert (
        Pages.BalanceSheetPage.as_of_datepicker.is_enable(timeout=10) is True
    ), "Loading balance sheet page is timeout"


@When("the user browse to 'Trial Balance' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_report.hover()
        Pages.NavigatorBar.accounting_report.click()
        Pages.NavigatorBar.accounting_report_trial_balance.hover()
        Pages.NavigatorBar.accounting_report_trial_balance.click()
    except:
        url = gl.URL.TRIAL_BALANCE
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'Trial Balance' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert (
        Pages.TrialBalancePage.period_period_datepicker.is_enable(timeout=10) is True
    ), "Loading trial balance page is timeout"


@When("the user browse to 'General Ledger Report' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_report.hover()
        Pages.NavigatorBar.accounting_report.click()
        Pages.NavigatorBar.accounting_report_gl_report.hover()
        Pages.NavigatorBar.accounting_report_gl_report.click()
    except:
        url = gl.URL.GENERAL_LEDGER_REPORT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'General Ledger Report' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert (
        Pages.GeneralLedgerReportPage.period_period_datepicker.is_enable(timeout=10) is True
    ), "Loading gl report page is timeout"


@When("the user browse to 'New Receipt' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.warehouse.hover()
        Pages.NavigatorBar.warehouse.click()
        Pages.NavigatorBar.warehouse_receipts.hover()
        Pages.NavigatorBar.warehouse_receipts.click()
        Pages.NavigatorBar.warehouse_new_receipt.hover()
        Pages.NavigatorBar.warehouse_new_receipt.click()
    except:
        url = gl.URL.WH_NEW_RECEIPTS
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Receipt' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert (
        Pages.WHReceiptBasicTab.received_date_time_datepicker.is_enable(timeout=10) is True
    ), "Loading new receipt page is timeout"


@When("the user browse to 'New Receiving' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.warehouse.hover()
        Pages.NavigatorBar.warehouse.click()
        Pages.NavigatorBar.warehouse_receiving_and_shipping.hover()
        Pages.NavigatorBar.warehouse_receiving_and_shipping.click()
        Pages.NavigatorBar.warehouse_new_receiving.hover()
        Pages.NavigatorBar.warehouse_new_receiving.click()
    except:
        url = gl.URL.WH_NEW_RECEIVING
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Receiving' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert (
        Pages.WHReceivingBasicTab.post_date_datepicker.is_enable(timeout=10) is True
    ), "Loading new receiving page is timeout"


@When("the user browse to 'New Shipping' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.warehouse.hover()
        Pages.NavigatorBar.warehouse.click()
        Pages.NavigatorBar.warehouse_receiving_and_shipping.hover()
        Pages.NavigatorBar.warehouse_receiving_and_shipping.click()
        Pages.NavigatorBar.warehouse_new_shipping.hover()
        Pages.NavigatorBar.warehouse_new_shipping.click()
    except:
        url = gl.URL.WH_NEW_SHIPPING
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@Then("'New Shipping' page show normally")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    assert (
        Pages.WHShippingBasicTab.post_date_datepicker.is_enable(timeout=10) is True
    ), "Loading new receiving page is timeout"


@When("the user browse to the Permission Management page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.super_user.hover()
        Pages.NavigatorBar.super_user.click()
        sleep(0.5)
        Pages.NavigatorBar.super_user_admin.click()
        sleep(0.5)
        Pages.NavigatorBar.super_user_admin_permission_management.click()
    except:
        url = gl.URL.PERMISSION_MANAGEMENT
        Logger.getLogger().warning(("Operating by user interface timeout, so go to link:[{0}] directly".format(url)))
        Driver.open(url)
    Pages.Common.spin_bar.gone()


@When("the user is in New {shipment} page")
def step_impl(context, shipment):
    if shipment == "Ocean Import Shipment":
        url = gl.URL.OI_NEW_SHIPMENT
    elif shipment == "Ocean Export Shipment":
        url = gl.URL.OE_NEW_SHIPMENT
    elif shipment == "Ocean Export Booking":
        url = gl.URL.OE_NEW_BOOKING
    elif shipment == "Ocean Export Vessel Schedule":
        url = gl.URL.OE_NEW_VESSEL_SCHEDULE
    elif shipment == "Air Import Shipment":
        url = gl.URL.AI_NEW_SHIPMENT
    elif shipment == "Air Export Shipment":
        url = gl.URL.AE_NEW_SHIPMENT
    elif shipment == "Truck Shipment":
        url = gl.URL.TK_NEW_SHIPMENT
    elif shipment == "Misc Operation":
        url = gl.URL.MS_NEW_OPERATION
    elif shipment == "Warehouse Receiving":
        url = gl.URL.WH_NEW_RECEIVING
    elif shipment == "Warehouse Shipping":
        url = gl.URL.WH_NEW_SHIPPING
    else:
        raise Exception("shipemnt: [{0}] is not valid, please check it.".format(shipment))

    Driver.open(url)
    Pages.Common.spin_bar.gone()


@When("the user expand the navigator 'Air Export'")
def step_impl(context):
    Pages.NavigatorBar.air_export.hover()
    Pages.NavigatorBar.air_export.click()


@When("the user expand the navigator 'Accounting'")
def step_impl(context):
    Pages.NavigatorBar.accounting.hover()
    Pages.NavigatorBar.accounting.click()


@When("the user expand the navigator 'Front Desk'")
def step_impl(context):
    Pages.NavigatorBar.accounting_front_desk.hover()
    Pages.NavigatorBar.accounting_front_desk.click()


@When("the user expand the navigator 'Settings'")
def step_impl(context):
    Pages.NavigatorBar.settings.hover()
    Pages.NavigatorBar.settings.click()


@When("the user browse to 'Front Desk Portal' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_front_desk.hover()
        Pages.NavigatorBar.accounting_front_desk.click()
        Pages.NavigatorBar.accounting_front_desk_front_desk_portal.hover()
        Pages.NavigatorBar.accounting_front_desk_front_desk_portal.click()
    except:
        url = gl.URL.FRONT_DESK_PORTAL
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'Uniform Invoice Management' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_front_desk.hover()
        Pages.NavigatorBar.accounting_front_desk.click()
        Pages.NavigatorBar.accounting_front_desk_uniform_invoice_management.hover()
        Pages.NavigatorBar.accounting_front_desk_uniform_invoice_management.click()
    except:
        url = gl.URL.UNIFORM_INVOICE_MANAGEMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'Uniform Invoice Setting' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_front_desk.hover()
        Pages.NavigatorBar.accounting_front_desk.click()
        Pages.NavigatorBar.accounting_front_desk_uniform_invoice_setting.hover()
        Pages.NavigatorBar.accounting_front_desk_uniform_invoice_setting.click()
    except:
        url = gl.URL.UNIFORM_INVOICE_SETTING
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'AWB No. Management' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.settings.hover()
        Pages.NavigatorBar.settings.click()
        Pages.NavigatorBar.settings_awb_no_management.hover()
        Pages.NavigatorBar.settings_awb_no_management.click()
        Pages.Common.spin_bar.gone()
    except:
        url = gl.URL.AWB_NO_MANAGEMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'MAWB Stock List' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.air_export.hover()
        Pages.NavigatorBar.air_export.click()
        Pages.NavigatorBar.air_export_mawb_stock_list.hover()
        Pages.NavigatorBar.air_export_mawb_stock_list.click()
        Pages.Common.spin_bar.gone()
    except:
        url = gl.URL.AE_MAWB_STOCK_LIST
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'Income Statement' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_report.hover()
        Pages.NavigatorBar.accounting_report.click()
        Pages.NavigatorBar.accounting_report_income_statement.hover()
        Pages.NavigatorBar.accounting_report_income_statement.click()
    except:
        url = gl.URL.INCOME_STATEMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'Receive Payment' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_payment.hover()
        Pages.NavigatorBar.accounting_payment.click()
        Pages.NavigatorBar.accounting_payment_receive_payment.hover()
        Pages.NavigatorBar.accounting_payment_receive_payment.click()
    except:
        url = gl.URL.RECEIVE_PAYMENT
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))


@When("the user browse to 'Payment Plan List' page by navigator")
def step_impl(context):
    try:
        Pages.NavigatorBar.accounting.hover()
        Pages.NavigatorBar.accounting.click()
        Pages.NavigatorBar.accounting_payment_plan.hover()
        Pages.NavigatorBar.accounting_payment_plan.click()
        Pages.NavigatorBar.accounting_payment_plan_payment_plan_list.hover()
        Pages.NavigatorBar.accounting_payment_plan_payment_plan_list.click()
    except:
        url = gl.URL.PAYMENT_PLAN_LIST
        Driver.open(url)
        Logger.getLogger().warning("Operating by user interface timeout, so go to link:[{0}] directly".format(url))
