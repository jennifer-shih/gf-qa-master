import math
import random
import string
from datetime import date, datetime, timedelta

import pandas as pd
from dateutil.relativedelta import relativedelta

import config.globalparameter as gl
from src.api.gofreight_config import GBy
from src.helper.log import Logger


def randomNo(length):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def randN(n):
    assert n <= 10
    l = list(range(10))  # compat py2 & py3
    while l[0] == 0:
        random.shuffle(l)
    return int("".join(str(d) for d in l[:n]))


def wday(d, format: str = None):
    if format:
        dfmt = format
    else:
        dfmt = gl.user_info.date_format
    dd = date.today() + timedelta(d)
    oldformat = str(dd)
    datetimeobject = datetime.strptime(oldformat, "%Y-%m-%d")
    return datetimeobject.strftime(dfmt)


def now():
    dfmt = gl.user_info.date_time_format
    time = datetime.now()
    return time.strftime(dfmt)


def wmonth(m):
    mm = date.today().strftime("%m")
    mm = (int(mm) + m - 1) % 12 + 1
    return str(mm)


def invoiceMonth(m):
    mm = int(wmonth(m))
    if mm % 2 == 0:
        return "{}-{}".format(mm - 1, mm)
    else:
        return "{}-{}".format(mm, mm + 1)


def wyear(y):
    yy = date.today().strftime("%Y")
    yy = int(yy) + y
    return str(yy)


def container_no_generator():
    code = "0123456789A?BCDEFGHIJK?LMNOPQRSTU?VWXYZ"
    engchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cno = ""
    sum1 = 0
    for i in range(0, 10, 1):
        if i < 4:
            idx = int(math.floor(random.randint(0, 25)))
            char = engchar[idx]
        else:
            char = str(int(math.floor(random.randint(0, 9))))

        cno = cno + char

        n = int(code.index(char))
        n = str(int(n * math.pow(2, i)))

        sum1 = sum1 + int(n)

    sum1 %= 11
    sum1 %= 10
    cno = cno + str(sum1)

    return cno


def to_relativedelta(tdelta):
    return relativedelta(seconds=int(tdelta.total_seconds()), microseconds=tdelta.microseconds)


def get_quotation_no(office_code: str):
    gfc = gl.gofreight_config
    quote_prefix = gfc.get_quotation_no_prefix(office_code, GBy.ONAME)
    quote_no_seq = int(gfc.get_quotation_no_seq(office_code, GBy.ONAME))
    quote_format = str(gfc.get_quotation_no_format(office_code, GBy.ONAME))
    quote_no = quote_format.format(prefix=quote_prefix, seq=quote_no_seq)

    return quote_no


def get_wh_receipt_no(office_code: str, strategy: str):
    gfc = gl.gofreight_config
    default_format = gfc.get_default_filing_no_format(office_code, strategy)
    receipt_prefix = gfc.get_wh_receipt_no_prefix(office_code, strategy)
    receipt_no_seq = int(gfc.get_wh_receipt_no_seq(office_code, strategy))
    receipt_format = gfc.get_wh_receipt_no_format(office_code, strategy)
    receipt_format = receipt_format if receipt_format else default_format
    today = date.today()
    today_ym = today.strftime("%y%m")
    today_y = today.strftime("%y")

    receipte_no = receipt_format.format(prefix=receipt_prefix, ym=today_ym, y=today_y, seq=receipt_no_seq)
    return receipte_no


def get_current_company():
    gfc = gl.gofreight_config
    first_office_name = gfc.get_office_full_name(1, GBy.OID)

    if first_office_name == "STRAIGHT FORWARDING, INC.":
        return "SFI"
    elif first_office_name == "LOHAN LOGISTICS Co.,Ltd.":
        return "LOHAN"
    elif first_office_name == "ORIENTAL LOGISTICS GROUP LTD.":
        return "OLC"
    elif first_office_name == "MASCOT INTERNATIONAL LOGISTICS, INC.":
        return "MASCOT"
    else:
        return None


def check_company_is_consistent():
    """
    Compare the company in global parameter to company in GofreightConfig.
    If there are not the same, print a warning message to logger
    """
    company_of_gofreight_config = get_current_company()
    company_of_gl = gl.company

    if company_of_gl != "BugRegression":
        if company_of_gofreight_config != company_of_gl:
            msg = f"Expect server's company to be { company_of_gl }, but get { company_of_gofreight_config }"
            Logger.getLogger().warning(msg)


def diff_df(old_file: pd.DataFrame, new_file: pd.DataFrame):
    # If the 2 DataFrames haven't setted index (e.g., some of the columns), the default index will be row index.

    # First concat 2 DataFrames vertically
    combine_df = pd.concat([old_file, new_file], sort=False)
    # combine_df:
    #                                       Unnamed: 0   Unnamed: 1   Unnamed: 2   Unnamed: 3   Unnamed: 4   Unnamed: 5
    # 0   ORIENTAL LOGISTICS GROUP LTD. QINGDAO BRANCH          NaN          NaN          NaN          NaN          NaN
    # 1                                  Balance Sheet          NaN          NaN          NaN          NaN          NaN
    # 2                               As of 2020-09-30          NaN          NaN          NaN          NaN          NaN
    # 3                                            RMB          NaN          NaN         Date          NaN   2021-12-14
    # ...
    #     ORIENTAL LOGISTICS GROUP LTD. QINGDAO BRANCH          NaN          NaN          NaN          NaN          NaN
    # 1                                  Balance Sheet          NaN          NaN          NaN          NaN          NaN
    # 2                               As of 2020-10-31          NaN          NaN          NaN          NaN          NaN
    # ...

    # Transform the concated file by stacking all levels from columns to index.
    # Grouping the series by the first 2 levels (which are row index and column in this function).
    # unique() is for transforming SeriesGroupBy to ndarray in this case.
    # Then transform the dataframe into the origin shape
    #
    # draft_diff_df has same size as old_file/new_file df. The cell value is a List object contains old_file and new_file value.
    # if values in old/new are same, List object only has one element.
    draft_diff_df: pd.DataFrame = combine_df.stack().groupby(level=[0, 1]).unique().unstack(1)

    # For the rows whose index didn't show up in old_file, mark their status to be "new"
    draft_diff_df.loc[~draft_diff_df.index.isin(old_file.index), "status"] = "new"
    # For the rows whose index didn't show up in new_file, mark their status to be "deleted"
    draft_diff_df.loc[~draft_diff_df.index.isin(new_file.index), "status"] = "deleted"

    # Get all 2 level indexs
    idx = combine_df.stack().groupby(level=[0, 1]).nunique()
    # Find the 2 level indexs whose count > 1 (they are the indexs of modefied cells)
    # For theese indexs, mark their status to be "modified"
    draft_diff_df.loc[idx.mask(idx <= 1).dropna().index.get_level_values(0), "status"] = "modified"

    # Assume that anything not fufilled by above rules is the same.
    # Drop the rows whose 'status' are nan.
    draft_diff_df = draft_diff_df.dropna(subset=["status"])
    # Make the draft_diff_df more readable by combining old values and new values with '-->'
    diff_df = draft_diff_df.stack().explode().astype(str).groupby(level=[0, 1]).agg("-->".join).unstack(1)

    return diff_df
