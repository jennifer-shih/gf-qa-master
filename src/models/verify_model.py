from __future__ import annotations

import collections
import copy

from src.helper.executor import exec_act_cmd
from src.helper.log import Logger


class VerifiedModel:
    """
    A data structure that stores the data we want to verify on the page
    and verify them.
    The common usage is calling add() to add things we want to verify, then
    call verify() to verify them all at once.

    data_table: {field: {"attribute": attribute, "data": data}}
    """

    ATTRIBUTE = "attribute"
    DATA = "data"

    def __init__(self, page_class_name: str):
        self.data_table = collections.OrderedDict()
        self.page_class_name = page_class_name

    def __iter__(self) -> dict:
        for i in self.data_table:
            yield i

    def __getitem__(self, field: str) -> dict:
        return self.data_table[field]

    def copy(self) -> VerifiedModel:
        copy_VerifiedModel = copy.deepcopy(self)
        return copy_VerifiedModel

    def add(self, field: str, attribute: str, data: str | bool) -> None:
        """Add a field we want to verify to the model"""

        self.data_table[field] = {self.ATTRIBUTE: attribute, self.DATA: data}

    def has_key(self, field: str) -> bool:
        return field in self.data_table

    def pop(self, field: str, not_exist_ok: bool = False) -> dict | None:
        """
        Remove and return the data and the attribute of the given field in the model

        not_exist_ok:  If it's True, this method won't raise KeyError in case the field doesn't exist
        """

        if not_exist_ok:
            return self.data_table.pop(field, None)
        else:
            return self.data_table.pop(field)

    def get_data(self, field: str) -> str:
        return self.data_table[field][self.DATA]

    def get_attribute(self, key: str) -> str:
        return self.data_table[key][self.ATTRIBUTE]

    def get_page_class_name(self) -> str:
        return self.page_class_name

    def set_page_class_name(self, page_class_name: str) -> None:
        self.page_class_name = page_class_name

    def get_all_fields(self) -> list:
        return [k for k in self.data_table.keys()]

    def verify(self) -> None:
        """Verify if the data saved in the model matches that on the web page"""

        failed_cases = []

        for field, v in self.data_table.items():
            result = exec_act_cmd(field, v[self.ATTRIBUTE], "get_value", page=self.page_class_name)
            expect = v[self.DATA]

            Logger.getLogger().info("[{0}]: [{1}]".format(field, result))
            if expect != result:
                failed_cases.append("{0}: Expect [{1}] but get [{2}]".format(field, expect, result))

        if len(failed_cases) != 0:
            msg = ""
            for case in failed_cases:
                msg = msg + "\n" + case
            assert False, msg
