import copy
import random  # noqa
import re

from behave.model import Row as BehaveRow
from behave.model import Table as BehaveTable

from config import globalparameter as gl
from src.api.gofreight_config import GBy
from src.helper.function import container_no_generator, invoiceMonth, now, randN, randomNo, wday, wyear  # noqa
from src.helper.function_vin import randomVin
from src.helper.log import Logger


def transfer_data(data: str) -> str | bool:
    """
    將BDD之 {keyword} 轉換成其所代表的值
    Example:
        transfer_data("{on}")                   ->  True
        trnasfer_data("{randomTradePartner}")   ->  "AIR9191"
        trnasfer_data("HACO-{randN(6)}")        ->  "HACO-123456"
    """
    keywords = re.findall("\{[^\{]+\}", data)
    variables = []
    for x in keywords:
        data = data.replace(x, "$$")

    for keyword in keywords:
        if keyword == "{on}":
            return True
        elif keyword == "{off}":
            return False
        elif keyword == "{randomOnOff}":
            return random.choice([True, False])
        elif "today" in keyword:
            if keyword == "{today}":
                variables.append(wday(0))
            else:
                day = int(keyword.replace("{today", "").replace("}", ""))
                variables.append(wday(day))
        elif "now" in keyword:
            if keyword == "{now}":
                variables.append(now())
        elif "year" in keyword:
            if keyword == "{year}":
                variables.append(wyear(0))
            else:
                year = int(keyword.replace("{wyear", "").replace("}", ""))
                variables.append(wyear(year))
        elif "invoiceMonth" in keyword:
            if keyword == "{invoiceMonth}":
                variables.append(invoiceMonth(0))
            else:
                month = int(keyword.replace("{invoiceMonth", "").replace("}", ""))
                variables.append(invoiceMonth(month))
        elif keyword == "{None}":
            variables.append("")
        elif "randomNo" in keyword:
            variables.append(eval(keyword.replace("{", "").replace("}", "")).upper())
        elif "randN" in keyword:
            variables.append(str(eval(keyword.replace("{", "").replace("}", ""))))
        elif "randInt" in keyword:
            variables.append(str(eval("random." + keyword.replace("{", "").replace("}", "").lower())))
        elif keyword == "{randomTradePartner}":
            variables.append(random.choice(gl.tp_name).upper())
        elif keyword == "{companySales}":
            variables.append(gl.companyConfig[gl.company]["sales"])
        elif keyword == "{companyBillToName}":
            # shipment 預設 bill to 顯示的是縮寫
            # bill_to = gl.companyConfig[gl.company]['bill_to_name']
            variables.append(gl.bill_to_nick_name[gl.company])
        elif keyword == "{companyDefaultPackage}":
            variables.append(gl.gofreight_config.get_default_package(gl.user_info.id, GBy.OID))
        elif keyword == "{randomVessel}":
            variables.append(random.choice(gl.vessel_list))
        elif keyword == "{randomCity}":
            variables.append(random.choice(gl.city_list))
        elif keyword == "{randomPort}":
            variables.append(random.choice(gl.port_list))
        elif keyword.replace("{", "").replace("}", "").isnumeric():
            variables.append(keyword)
        elif keyword == "{randomCommodity}":
            variables.append(random.choice(gl.commodity_list))
        elif keyword == "{companyLogo}":
            path = gl.project_path / "pic" / (gl.company + "_Logo.png")
            if path.is_file():
                variables.append(str(path.as_posix()))
            else:
                variables.append("")
        elif keyword == "{randomContainerNo}":
            variables.append(container_no_generator())
        elif keyword == "{randomVin}":
            variables.append(randomVin())
        elif keyword == "{randomModel}":
            variables.append(random.choice(gl.model_list))
        elif keyword == "{randomColor}":
            variables.append(random.choice(gl.color_list))
        elif keyword == "{randomSales}":
            variables.append(random.choice(gl.sales_list))
        elif keyword == "{randomUnit}":
            variables.append(random.choice(gl.unit_list))
        elif keyword == "{blank}":
            variables.append("")
        else:
            variables.append("")

    for v in variables:
        data = data.replace("$$", v, 1)

    return data


def transfer_str_element(field: str, attribute: str, page_class_name=None) -> str:
    """
    將 field, attr, page_class_name 組合成對應的 Object script, 需使用 eval 作轉換
    Example:
        transfer_str_element("File No.", "input", "Pages.OIBasicTab")   ->  "Pages.OIBasicTab.file_no_input"
    """
    page_class = page_class_name if page_class_name != None else ""
    attribute = transfer_attribute(attribute)
    field = transfer_field(field)
    locator = "_".join((field, attribute))
    return page_class + "." + locator


def transfer_field(field: str) -> str:
    """
    標準化 feature file 的 field
    Example:
        transfer_field("File No.")      ->  "file_no"
        transfer_field("B/L Type")      ->  "b_l_type"
    """
    symbols_mapping = {
        "/": "_",
        ".": "",
        " ": "_",
        "-": "_",
        "(": "",
        ")": "",
        "'": "",
        "=": "_",
        "&": "_",
    }
    for s in symbols_mapping:
        if s in field:
            field = field.replace(s, symbols_mapping[s])
    return field.lower()


def transfer_action(action: str) -> str:
    """
    標準化 feature file 的 action
    Example:
        transfer_action("input")            ->  "input"
        transfer_action("random select")    ->  "random_select"
    """
    return action.replace(" ", "_").lower()


def transfer_attribute(attribute: str) -> str:
    """
    標準化 feature file 的 attribute
    Example:
        transfer_attribute("input")         ->  "input"
        transfer_attribute("tag input")     ->  "tag_input"
    """
    return attribute.replace(" ", "_").lower()


def transfer_keyword(action: str) -> str:
    """
    標準化 feature file 裡的 keyword ex. log in with [{character}] --(login.py)
    """
    return action.replace(" ", "_").lower()


def get_execute_script(field: str, attribute: str, action: str, datas: list = [], page_class_name="") -> str:
    """
    將 feature file 的 table value 轉換成可執行的 script
    Example:
        get_execute_script("File No.", "input", "input", ["HACO-111"], "Pages.OIBasicTab")
        ->    'Pages.OIBasicTab.file_no_input.input("HACO-111")'
    """
    _action = transfer_action(action)
    _element = transfer_str_element(field, attribute, page_class_name=page_class_name)
    _datas = []
    for data in datas:
        if isinstance(data, float):  # for para 'timeout'
            _datas.append(str(data))
        elif data:  # if data is None, don't append '' into _datas
            transfered_data = transfer_data(data)
            if type(transfered_data) == str:
                _datas.append(f'"{ transfered_data }"')
            else:
                _datas.append(str(transfered_data))

    parameters = "(" + ", ".join(_datas) + ")"
    script = _element + "." + _action + parameters
    Logger.getLogger().debug("execute script: {0}".format(script))
    return script


def transfer_to_feature_table(text_table: str) -> BehaveTable:
    """
    Example:
        transfer_to_feature_table("
        | field             | attribute    | action             | data   |
        | Received By       | select       | random select      |        |
        ")
    """

    def sterilize(text):
        return [t.strip() for t in text.strip().split("|")][1:-1]

    texts = text_table.strip().splitlines()
    headings = sterilize(texts[0])
    rows = []
    for i in texts[1:]:
        rows.append(sterilize(i))

    return BehaveTable(headings=headings, rows=rows)


def trans_data_to_value(data: str, attribute: str, get_value=None):
    value = data
    if attribute == "checkbox":
        if data == "0":
            value = False
        elif data == "1":
            value = True
    elif attribute == "multi autocomplete":
        data = data.split(";")
        if get_value:
            get_value = get_value.split(";")
            for i in range(len(data)):
                if data[i] in get_value[i]:
                    data[i] = get_value[i]
        data = ";".join(data)
    elif attribute == "autocomplete":
        if data in get_value:
            value = get_value
    elif attribute == "tag input":
        value = value.replace(" ", "")
    return value


def transfer_str_of_indices_to_list(string_of_indices: str) -> list:
    """
    Example:  transfer_str_of_indices_to_list("1, 3, 6, 8")  =>  [1, 3, 6, 8]
    """
    list_of_char = string_of_indices.split(",")
    return_list = []
    for char in list_of_char:
        return_list.append(int(char))

    return return_list


def combine_outline_with_table(active_outline: BehaveRow, table: BehaveTable) -> BehaveTable:
    """
    add data in 'active_outline' into table 'data' column
    """
    datas = active_outline.cells
    combined_table = copy.deepcopy(table)
    combined_table.add_column(column_name="data", values=datas)

    return combined_table
