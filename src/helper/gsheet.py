from datetime import datetime

import pygsheets

from src.exception.exception import KeyCanNotBeModifiedError, ParametersAreMutuallyExclusiveError


class GRecord:
    def __init__(self, key: str, key_index: int):
        values = [""] * (key_index + 1)
        values[key_index] = key

        self._values = values
        self._key = key
        self._key_index = key_index

    @property
    def key(self) -> str:
        return self._key

    @property
    def values(self):
        return self._values

    def get(self, index):
        return self._values[index]

    def set(self, index: int, value):
        curr_len = len(self._values)
        if index == self._key_index:
            raise KeyCanNotBeModifiedError(f"Values[{index}] is a key and can NOT be changed.")
        if not index < curr_len:
            exp_len = index + 1
            extend_list = [""] * (exp_len - curr_len)
            self._values.extend(extend_list)
        self._values[index] = value

    def record_values_to_str_list(self) -> list[str]:
        return [str(v) for v in self._values]


class GWorkSheet:
    TIME_FORMAT = r"%Y-%m-%d %H:%M:%S"

    def __init__(self, worksheet: pygsheets.Worksheet, key_index: int):
        self._worksheet = worksheet
        self._key_index = key_index

    @property
    def url(self):
        return self._worksheet.url

    @property
    def title(self):
        return self._worksheet.title

    def delete_all(self):
        """only leave first row"""
        num_of_rows = self._worksheet.rows
        if not num_of_rows < 2:
            self._worksheet.delete_rows(2, num_of_rows)

    def clear(self):
        num_of_rows = self._worksheet.rows
        if not num_of_rows < 2:
            self._worksheet.clear(start="A2")

    def init_row_record(self, insert_row=1) -> GRecord:
        key = datetime.now().strftime(self.TIME_FORMAT)
        record = GRecord(key, self._key_index)
        self._worksheet.insert_rows(row=insert_row, values=record.record_values_to_str_list(), inherit=True)
        return record

    def get_all_values(self):
        return self._worksheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)

    def get_all_cells(self) -> list[list[pygsheets.Cell]]:
        return self._worksheet.get_all_values(
            include_tailing_empty=False,
            include_tailing_empty_rows=False,
            returnas="cell",
        )

    def _get_row(self, index):
        return self._worksheet.get_row(row=index, returnas="cell")

    def _get_column(self, index):
        return self._worksheet.get_col(col=index, returnas="cell")

    def _get_record_row_index(self, key: str) -> int:
        for row in self.get_all_cells():
            try:
                cell = row[self._key_index]
                d = datetime.strptime(cell.value, self.TIME_FORMAT)
                target = datetime.strptime(key, self.TIME_FORMAT)
                if d == target:
                    return cell.row
            except:
                pass

    def send_record(self, record: GRecord):
        row_index = self._get_record_row_index(record.key)
        self._worksheet.update_row(index=row_index, values=record.record_values_to_str_list(), col_offset=0)


class GSpreadSheet:
    """
    save data to https://docs.google.com/spreadsheets/d/18Hl_JqMZO4orZxPeoLGPQWNmjdJSEDrOHAXlewP6VaU/edit#gid=621204057
    將 time 設為 key 以避免多人同時存取 gsheet 時，資料的欄位變動導致存錯欄位
    key_index 為儲存 time 的 column (0 ~ )
    可使用 tab_title (table的名稱) 或是 tab_index (第一張table的index為0) 決定要存取在哪張 table
    """

    def __init__(self, client_secret_path: str, gsheet_key: str):
        self._client = pygsheets.authorize(client_secret=client_secret_path)
        self._spreadsheet = self._client.open_by_key(gsheet_key)

    def get_worksheet(self, name=None, index=None, key_index: int = 0):
        if name != None and index != None:
            raise ParametersAreMutuallyExclusiveError("Cannot input both 'name' and 'index'")
        if name:
            return GWorkSheet(self._spreadsheet.worksheet("title", name), key_index=key_index)
        elif index:
            return GWorkSheet(self._spreadsheet[index], key_index=key_index)
