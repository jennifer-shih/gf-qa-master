import os
import re
from datetime import datetime

import pandas as pd
import pdfplumber
from behave import Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd, trnas_ele_cmd
from src.helper.function import diff_df, wday
from src.helper.script import input_dynamic_datas
from src.helper.timer import DownloadTimer
from src.helper.transfer import transfer_data


@When("the user enter 'Balance Sheet' info")
def step_impl(context):
    current_page_class_name = "Pages.BalanceSheetPage"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_v(v_name="bs_info", value=model)


@When("the user enter 'Trial Balance' info")
def step_impl(context):
    current_page_class_name = "Pages.TrialBalancePage"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_v(v_name="tb_info", value=model)


@When("the user enter 'General Ledger Report' info")
def step_impl(context):
    current_page_class_name = "Pages.GeneralLedgerReportPage"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_v(v_name="glr_info", value=model)


@When("the user enter 'Income Statement' info")
def step_impl(context):
    current_page_class_name = "Pages.IncomeStatementPage"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_v(v_name="is_info", value=model)


@When("the user click 'Balance Sheet' 'Print' button")
def step_impl(context):
    Pages.BalanceSheetPage.print_button.click()
    Driver.switch_to(window_name="Balance Sheet")
    Pages.Common.spin_bar.gone()


@When("the user click 'Trial Balance' 'Print' button")
def step_impl(context):
    Pages.TrialBalancePage.print_button.click()
    Driver.switch_to(window_name="Trial Balance")
    Pages.Common.spin_bar.gone()


@When("the user click 'General Ledger Report' 'Print' button")
def step_impl(context):
    Pages.GeneralLedgerReportPage.print_button.click()
    Driver.switch_to(window_index=1)
    Pages.Common.spin_bar.gone()


@When("the user click 'Income Statement' 'Print' button")
def step_impl(context):
    Pages.IncomeStatementPage.print_button.click()
    Driver.switch_to(window_name="Income Statement")
    Pages.Common.spin_bar.gone()


@When("the user choose '{office}' office for 'Balance Sheet'")
def step_impl(context, office):
    Pages.BalanceSheetPage.office_select.select(office)


@When("the user choose '{office}' office for 'Trial Balance'")
def step_impl(context, office):
    Pages.TrialBalancePage.office_select.select(office)


@When("the user choose '{office}' office for 'General Ledger Report'")
def step_impl(context, office):
    Pages.GeneralLedgerReportPage.office_select.select(office)


@Then("the 'Balance Sheet' values should be correct")
def step_impl(context):
    current_page_class_name = "Pages.BalanceSheetPage.Print.Table"

    assert Pages.BalanceSheetPage.Print.title_label.get_value() == "Balance Sheet", "Wrong title for Balance Sheet"

    for row in context.table:
        exp_value = exec_act_cmd(row["field"], "label", "get_value", page=current_page_class_name)
        assert exp_value == row["value"], f"Wrong { row['field'].lower() } for balance trial"
        context._vp.add_dict(dict_name="numbers", value={row["field"]: row["value"]})

        if row["field"] == "TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY":
            context._vp.add_v("total_leq", exp_value)


@Then("the 'Trial Balance' values for '{office}' office should be correct")
def step_impl(context, office):
    current_page_class_name = "Pages.TrialBalancePage.Print.Table"

    assert Pages.TrialBalancePage.Print.title_label.get_value() == "Trial Balance", "Wrong title for balance sheet"

    for row in context.table:
        exp_value = exec_act_cmd(row["field"], "label", "get_value", page=current_page_class_name)
        assert exp_value == row["value"], "Wrong " + row["field"].lower() + " for trial balance"
        context._vp.add_dict(dict_name="numbers", value={row["field"]: row["value"]})


@Then("the 'General Ledger Report' {report_type} values for '{office}' office should be correct")
def step_impl(context, report_type, office):
    if report_type == "summary":
        current_page_class_name = "Pages.GeneralLedgerReportPage.PrintSummary.Table"
        assert (
            Pages.GeneralLedgerReportPage.PrintSummary.title_label.get_value() == "G/L Summary"
        ), "Wrong title for gl summary report"
    elif report_type == "detail":
        landscape_title = "G/L Detail (Landscape)"
        BnE_title = "G/L Detail (B&E Balance)"
        actual_title = Pages.GeneralLedgerReportPage.PrintDetail.title_label.get_value()
        if actual_title == landscape_title:
            context._vp.add_v(v_name="detail_report_type", value="Landscape")
            current_page_class_name = "Pages.GeneralLedgerReportPage.PrintDetail.Landscape.Table"
        elif actual_title == BnE_title:
            context._vp.add_v(v_name="detail_report_type", value="BnEExpense")
            current_page_class_name = "Pages.GeneralLedgerReportPage.PrintDetail.BnEExpense.Table"
        else:
            assert False, "Wrong title"
    elif report_type == "tp summary":
        current_page_class_name = "Pages.GeneralLedgerReportPage.PrintTPSummary.Table"
        assert (
            Pages.GeneralLedgerReportPage.PrintTPSummary.title_label.get_value() == "G/L Summary (By Trade Partner)"
        ), "Wrong title for gl tp summary report"
    elif report_type == "A&G expense":
        current_page_class_name = "Pages.GeneralLedgerReportPage.PrintGAExpense.Table"
        assert (
            Pages.GeneralLedgerReportPage.PrintGAExpense.title_label.get_value() == "The Statement of G&A Expenses"
        ), "Wrong title for gl A&G expense report"

    for row in context.table:
        exp_value = exec_act_cmd(row["field"], "label", "get_value", page=current_page_class_name).replace("\n", "")
        assert exp_value == row["value"], "Wrong " + row["field"].lower() + " for gl report"
        context._vp.add_dict(dict_name="numbers", value={row["field"]: row["value"]})


@Then("the 'Income Statement' values should be correct")
def step_impl(context):
    current_page_class_name = "Pages.IncomeStatementPage.Print.Table"

    assert (
        Pages.IncomeStatementPage.Print.title_label.get_value() == "Income Statement"
    ), "Wrong title for Income Statement"

    for row in context.table:
        exp_value = exec_act_cmd(row["field"], "label", "get_value", page=current_page_class_name)
        assert (
            exp_value == row["value"]
        ), f"Expect { row['value'] } in { row['field'] }, Income Statement Page, but get { exp_value }"


@Then("the 'Balance Sheet' file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    model = context._vp.get("bs_info")
    if gl.company in ["SFI", "LOHAN"]:
        date = datetime.strptime(model.get_data("As of"), "%m-%d-%Y")
        date = date.strftime("%Y-%m-%d")
    elif gl.company in ["OLC", "MASCOT"]:
        date = model.get_data("As of")
    bs_pdf_name = "Balance Sheet as of " + date + ".pdf"
    bs_pdf_path = gl.download_path / bs_pdf_name
    dt = DownloadTimer(str(bs_pdf_path), int(timeout))
    dt.start()

    with pdfplumber.open(str(bs_pdf_path)) as pdf:
        bs_pdf_page = len(pdf.pages)

        if gl.company == "SFI":
            pdf_page = 2
        elif gl.company == "LOHAN":
            pdf_page = 1
        elif gl.company == "OLC":
            pdf_page = 2

        assert pdf_page == bs_pdf_page, "Expect [{0}] page, but get [{1}]".format(pdf_page, bs_pdf_page)

        leq_found = False
        for page in pdf.pages:
            reg = re.search("TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY.*\n", page.extract_text())
            if reg is not None:
                total_leq = reg.group(0).replace("TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY ", "").replace("\n", "")
                exp_total_leq = context._vp.get("total_leq")
                assert (
                    exp_total_leq == total_leq
                ), "Expect total liabilities and stockholders to be [{0}], but get [{1}]".format(
                    exp_total_leq, total_leq
                )
                leq_found = True
                break
        assert leq_found, "Total liabilities and equity text not found"


@Then("the 'Trial Balance' file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    tb_pdf_name = "Trial Balance.pdf"
    tb_pdf_path = gl.download_path / tb_pdf_name
    dt = DownloadTimer(str(tb_pdf_path), int(timeout))
    dt.start()

    pdf_page_dict = {"SFI": 5, "OLC": 2, "LOHAN": 1}

    with pdfplumber.open(str(tb_pdf_path)) as pdf:
        tb_pdf_page = len(pdf.pages)
        assert pdf_page_dict[gl.company] == tb_pdf_page, "Expect [{0}] page, but get [{1}]".format(
            pdf_page_dict[gl.company], tb_pdf_page
        )

        total_found = False
        reg = re.search("TOTAL .*\n", pdf.pages[-1].extract_text())
        if reg is not None:
            numbers = reg.group(0).split(" ")
            total_beginning_balance = numbers[-4]
            total_debit = numbers[-3]
            total_credit = numbers[-2]
            total_balance = numbers[-1].replace("\n", "")
            numbers = context._vp.get("numbers")
            assert (
                numbers["Total Beginning Balance"] == total_beginning_balance
            ), "Expect total begining balance to be [{0}], but get [{1}]".format(
                numbers["Total Beginning Balance"], total_beginning_balance
            )
            assert numbers["Total Debit"] == total_debit, "Expect total debit to be [{0}], but get [{1}]".format(
                numbers["Total  Debit"], total_debit
            )
            assert numbers["Total Credit"] == total_credit, "Expect total credit to be [{0}], but get [{1}]".format(
                numbers["Total Credit"], total_credit
            )
            assert numbers["Total Balance"] == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
                numbers["Total Balance"], total_balance
            )
            total_found = True
        assert total_found, "Total text not found"


@Then("the 'General Ledger Report' summary pdf file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_pdf_name = "GL Summary.pdf"
    gl_pdf_path = gl.download_path / gl_pdf_name
    dt = DownloadTimer(str(gl_pdf_path), int(timeout))
    dt.start()
    pdf_page_dict = {"SFI": 4, "OLC": 1, "LOHAN": 1}

    with pdfplumber.open(str(gl_pdf_path)) as pdf:
        gl_pdf_page = len(pdf.pages)
        assert pdf_page_dict[gl.company] == gl_pdf_page, "Expect [{0}] page, but get [{1}]".format(
            pdf_page_dict[gl.company], gl_pdf_page
        )

        total_found = False
        reg = re.search("Total.*Record\(s\).*\n", pdf.pages[-1].extract_text())
        if reg is not None:
            numbers = re.sub("Total.*Record\(s\) ", "", reg.group(0)).split(" ")
            total_balance = numbers[2].replace("\n", "")
            numbers = context._vp.get("numbers")
            assert numbers["Total Balance"] == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
                numbers["Total Balance"], total_balance
            )
            total_found = True
        assert total_found, "Total text not found"


@Then("the 'General Ledger Report' summary excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_excel_name = "GL_report_" + wday(0) + ".xlsx"
    gl_excel_path = gl.download_path / gl_excel_name
    dt = DownloadTimer(str(gl_excel_path), int(timeout))
    dt.start()

    excel = pd.read_excel(gl_excel_path)
    # ? KNOWN ISSUE
    if all(["Unnamed: " in header for header in excel.keys()]):
        excel = pd.read_excel(gl_excel_path, header=1)
    # ?
    total_balance = excel.iloc[-1]["Balance"]

    numbers = context._vp.get("numbers")
    ep_total_balance = float(re.sub(r"[^\d.-]", "", numbers["Total Balance"]))
    assert ep_total_balance == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
        ep_total_balance, total_balance
    )


@Then("the 'General Ledger Report' detail pdf file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_pdf_name = "GL Detail.pdf"
    gl_pdf_path = gl.download_path / gl_pdf_name
    dt = DownloadTimer(str(gl_pdf_path), int(timeout))
    dt.start()
    pdf_page_dict = {"SFI": 4, "OLC": 1, "LOHAN": 1}

    with pdfplumber.open(str(gl_pdf_path)) as pdf:
        gl_pdf_page = len(pdf.pages)
        assert pdf_page_dict[gl.company] == gl_pdf_page, "Expect [{0}] page, but get [{1}]".format(
            pdf_page_dict[gl.company], gl_pdf_page
        )

        total_found = False
        detail_report_type = context._vp.get("detail_report_type")
        if detail_report_type == "Landscape":
            reg = re.search("TOTAL.*Record\(s\) Balance.*\n", pdf.pages[-1].extract_text())
        elif detail_report_type == "BnEExpense":
            reg = re.search("TOTAL.*Record\(s\).*\n", pdf.pages[-1].extract_text())
        if reg is not None:
            if detail_report_type == "Landscape":
                numbers = list(
                    filter(
                        None,
                        re.sub("TOTAL.*Record\(s\) Balance", "", reg.group(0)).split(" "),
                    )
                )
                total_balance = numbers[0]
                total_credit = numbers[-1].replace("\n", "")
            elif detail_report_type == "BnEExpense":
                numbers = list(filter(None, re.sub("TOTAL.*Record\(s\)", "", reg.group(0)).split(" ")))
                total_balance = numbers[2]
                total_credit = numbers[1]
            numbers = context._vp.get("numbers")
            assert numbers["Total Balance"] == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
                numbers["Total Balance"], total_balance
            )
            assert numbers["Total Credit"] == total_credit, "Expect total credit to be [{0}], but get [{1}]".format(
                numbers["Total Credit"], total_credit
            )
            total_found = True
        assert total_found, "Total text not found"


@Then("the 'General Ledger Report' detail excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_excel_name = "GL_detail_" + wday(0) + ".xlsx"
    gl_excel_path = gl.download_path / gl_excel_name
    dt = DownloadTimer(str(gl_excel_path), int(timeout))
    dt.start()

    detail_report_type = context._vp.get("detail_report_type")
    if detail_report_type == "Landscape":
        excel = pd.read_excel(gl_excel_path)
        total_balance = excel.iloc[-1]["Description"]
    elif detail_report_type == "BnEExpense":
        # ? KNOWN ISSUE
        excel = pd.read_excel(gl_excel_path, header=1)
        # ?
        total_balance = excel.iloc[-1]["Balance"]
    total_credit = excel.iloc[-1]["Credit"]
    numbers = context._vp.get("numbers")
    ep_total_balance = float(re.sub(r"[^\d.-]", "", numbers["Total Balance"]))
    ep_total_credit = float(re.sub(r"[^\d.-]", "", numbers["Total Credit"]))
    assert ep_total_balance == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
        ep_total_balance, total_balance
    )
    assert ep_total_credit == total_credit, "Expect total credit to be [{0}], but get [{1}]".format(
        ep_total_credit, total_credit
    )


@Then("the 'General Ledger Report' tp summary pdf file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_pdf_name = "GL Summary By Trade Partner.pdf"
    gl_pdf_path = gl.download_path / gl_pdf_name
    dt = DownloadTimer(str(gl_pdf_path), int(timeout))
    dt.start()
    pdf_page_dict = {"SFI": 23, "OLC": 9, "LOHAN": 9}

    with pdfplumber.open(str(gl_pdf_path)) as pdf:
        gl_pdf_page = len(pdf.pages)
        assert pdf_page_dict[gl.company] == gl_pdf_page, "Expect [{0}] page, but get [{1}]".format(
            pdf_page_dict[gl.company], gl_pdf_page
        )

        total_found = False
        reg = re.search("Total.*Record\(s\).*\n", pdf.pages[-1].extract_text())
        if reg is not None:
            record = re.sub("Total.*Record\(s\) ", "", reg.group(0)).split(" ")
            total_balance = record[-1].replace("\n", "")
            numbers = context._vp.get("numbers")
            assert numbers["Total Balance"] == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
                numbers["Total Balance"], total_balance
            )
            total_found = True
        assert total_found, "Total text not found"


@Then("the 'General Ledger Report' tp summary excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_excel_name = "GL Summary By Trade Partner.xlsx"
    gl_excel_path = gl.download_path / gl_excel_name
    dt = DownloadTimer(str(gl_excel_path), int(timeout))
    dt.start()

    excel = pd.read_excel(gl_excel_path)
    # ? KNOWN ISSUE
    if all(["Unnamed: " in header for header in excel.keys()]):
        excel = pd.read_excel(gl_excel_path, header=1)
    # ?
    total_balance = excel.iloc[-1]["Balance"]

    numbers = context._vp.get("numbers")
    ep_total_balance = float(re.sub(r"[^\d.-]", "", numbers["Total Balance"]))
    assert ep_total_balance == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
        ep_total_balance, total_balance
    )


@Then("the 'General Ledger Report' A&G expense pdf file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    gl_pdf_name = "The Statement of G&A Expenses.pdf"
    gl_pdf_path = gl.download_path / gl_pdf_name
    dt = DownloadTimer(str(gl_pdf_path), int(timeout))
    dt.start()

    pdf_page = 1
    with pdfplumber.open(str(gl_pdf_path)) as pdf:
        gl_pdf_page = len(pdf.pages)
        assert pdf_page == gl_pdf_page, "Expect [{0}] page, but get [{1}]".format(pdf_page, gl_pdf_page)

        total_found = False
        reg = re.search("TOTAL.*Record\(s\).*\n", pdf.pages[-1].extract_text())
        if reg is not None:
            record = re.sub("TOTAL.*Record\(s\) ", "", reg.group(0)).split(" ")
            total_balance = record[-1].replace("\n", "")
            numbers = context._vp.get("numbers")
            assert numbers["Total Balance"] == total_balance, "Expect total balance to be [{0}], but get [{1}]".format(
                numbers["Total Balance"], total_balance
            )
            total_found = True
        assert total_found, "Total text not found"


@Then("the 'Trial Balance Print' should show without any errors")
def step_impl(context):
    assert Pages.TrialBalancePage.Print.period_label.is_visible(10)
    assert Pages.TrialBalancePage.Print.title_label.is_visible()
    item_count = Pages.TrialBalancePage.Print.Table.get_len()
    assert item_count > 0, "No items show on the Trial Balance."


@Then("the 'Period' on 'Trial Balance Print' should be '{start}' to '{end}'")
def step_impl(context, start, end):
    start_text = transfer_data(start)
    end_text = transfer_data(end)
    period_title = Pages.TrialBalancePage.Print.period_label.get_value()
    period_date_text = "Period: {0} ~ {1}".format(start_text, end_text)
    assert period_title == period_date_text, "Period title [{0}] is not equal to [{1}] on the gl report print.".format(
        period_title, period_date_text
    )

    Driver.close()
    Driver.switch_to(window_index=0)


@Then("the 'General Ledger Report' ({report_type}) should show without any errors")
def step_impl(context, report_type):
    if report_type == "Summary":
        assert Pages.GeneralLedgerReportPage.PrintSummary.title_label.is_visible(10), "Title should show"
        assert Pages.GeneralLedgerReportPage.PrintSummary.period_label.is_visible(), "Period should show"
    elif report_type == "Detail":
        assert Pages.GeneralLedgerReportPage.PrintDetail.title_label.is_visible(10), "Title should show"
        assert Pages.GeneralLedgerReportPage.PrintDetail.period_label.is_visible(), "Period should show"
    else:
        raise Exception(f"Invalid Parameter report_type [{report_type}]")


@Then("the 'Period' on 'General Ledger Report' ({report_type}) should be '{start}' ~ '{end}'")
def step_impl(context, report_type, start, end):
    if report_type == "Summary":
        start_text = transfer_data(start)
        end_text = transfer_data(end)
        period_title = Pages.GeneralLedgerReportPage.PrintSummary.period_label.get_value()
        period_date_text = "Period: {0} ~ {1}".format(start_text, end_text)
    elif report_type == "Detail":
        start_text = transfer_data(start)
        end_text = transfer_data(end)
        period_title = Pages.GeneralLedgerReportPage.PrintDetail.period_label.get_value()
        period_date_text = "Period: {0} ~ {1}".format(start_text, end_text)
    else:
        raise Exception(f"Invalid Parameter report_type [{report_type}]")

    assert period_title == period_date_text, "Period title [{0}] is not equal to [{1}] on the print.".format(
        period_title, period_date_text
    )


@Then("the 'General Ledger Report' ({report_type}) should show with freights")
def step_impl(context, report_type):
    if report_type == "Summary":
        print_item_count = Pages.GeneralLedgerReportPage.PrintSummary.Table.get_len()
        assert print_item_count > 0, "No items show on the report print."
    elif report_type == "Detail":
        print_item_count = Pages.GeneralLedgerReportPage.PrintDetail.Landscape.Table.get_len()
        assert print_item_count > 0, "No items show on the report print."
    else:
        raise Exception(f"Invalid Parameter report_type [{report_type}]")


@When("the user clicks 'NET INCOME FOR THIS PERIOD' link in 'Balance Sheet'")
def step_impl(context):
    Pages.BalanceSheetPage.Print.Table.net_income_for_this_period_link.click()
    Driver.switch_to(window_name="Income Statement")
    Pages.Common.spin_bar.gone()


@When("the user clicks '{link_name}' link in 'Trial Balance'")
def step_impl(context, link_name):
    element = trnas_ele_cmd(link_name, "Link", "Pages.TrialBalancePage.Print.Table")
    element.click()
    Driver.switch_to(window_name="General Ledger Report")
    Pages.Common.spin_bar.gone()


@Then("the 'Balance Sheet' excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    bs_excel_name = "Balance_sheet_{}.xlsx".format(wday(0))
    bs_excel_path = gl.download_path / bs_excel_name
    dt = DownloadTimer(str(bs_excel_path), int(timeout))
    dt.start()


@Then("the 'Balance Sheet' excel file should be as same as '{file_path}'")
def step_impl(context, file_path):
    new_file_path = str(gl.download_path / "Balance_sheet_{}.xlsx".format(wday(0)))
    new_file = pd.read_excel(new_file_path)
    reference_file = pd.read_excel(str(gl.project_path / file_path))
    assert new_file.iloc[3, 5] == wday(0), "Wrong reprot export date"

    # remove export date
    new_file.iloc[3, 5] = ""
    reference_file.iloc[3, 5] = ""

    # rename file to avoid misuse current file for future file
    os.rename(new_file_path, str(gl.download_path / file_path.split("/")[-1]))

    difference = diff_df(reference_file, new_file)
    assert difference.shape[0] == 0, difference.to_string()


@Then("the 'Trial Balance' excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    tb_excel_name = "Trial Balance.xlsx"
    tb_excel_path = gl.download_path / tb_excel_name
    dt = DownloadTimer(str(tb_excel_path), int(timeout))
    dt.start()


@Then("the 'Trial Balance' excel file should be as same as '{file_path}'")
def step_impl(context, file_path):
    new_file = pd.read_excel(str(gl.download_path / "Trial Balance.xlsx"))
    reference_file = pd.read_excel(str(gl.project_path / file_path))
    assert new_file.iloc[3, 0] == "Date : {}".format(wday(0)), "Wrong reprot export date"

    # remove export date
    new_file.iloc[3, 0] = ""
    reference_file.iloc[3, 0] = ""

    # rename file to avoid misuse current file for future file
    os.rename(
        str(gl.download_path / "Trial Balance.xlsx"),
        str(gl.download_path / file_path.split("/")[-1]),
    )

    difference = diff_df(reference_file, new_file)
    assert difference.shape[0] == 0, difference.to_string()


@Then("the 'Income Statement' excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    is_excel_name = "Income_statement_{}.xlsx".format(wday(0))
    is_excel_path = gl.download_path / is_excel_name
    dt = DownloadTimer(str(is_excel_path), int(timeout))
    dt.start()


@Then("the 'Income Statement' excel file should be as same as '{file_path}'")
def step_impl(context, file_path):
    new_file_path = str(gl.download_path / "Income_statement_{}.xlsx".format(wday(0)))
    new_file = pd.read_excel(new_file_path)
    reference_file = pd.read_excel(str(gl.project_path / file_path))
    assert new_file.iloc[3, 0] == "Date: {}".format(wday(0)), "Wrong reprot export date"

    # remove export date
    new_file.iloc[3, 0] = ""
    reference_file.iloc[3, 0] = ""

    # rename file to avoid misuse current file for future file
    os.rename(new_file_path, str(gl.download_path / file_path.split("/")[-1]))

    difference = diff_df(reference_file, new_file)
    assert difference.shape[0] == 0, difference.to_string()
