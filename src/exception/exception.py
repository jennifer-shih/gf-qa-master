class GfqaException(Exception):
    """User defined exception in this project"""


class ParametersAreMutuallyExclusiveError(GfqaException):
    """parameters 互斥"""


class KeyCanNotBeModifiedError(GfqaException):
    """不能修改當作 Key 的值"""


class PageElementManipulationError(GfqaException):
    """Fail to manipulate a page element (Timeout or the locator is outdated)"""


class ElementTransError(GfqaException):
    """Fail to use field|attr|page to get Element"""

    def __init__(self, field: str, attr: str, page: str):
        super().__init__(f"Element [{field}] [{attr}] in [{page}] is NOT found")


class StepParaNotDefinedError(GfqaException):
    """The step parameter is NOT defined"""

    def __init__(self, *para: str):
        super().__init__(f"the parameter [{', '.join(para)}] is NOT defined in this step")


class AutocompleteOptionNotFoundError(GfqaException):
    """Not found any option when searching in an autocomplete"""

    def __init__(self, input_val=None):
        if input_val:
            self.message = f"""Can't find the corresponding option for input "{ input_val }" in the autocomplete"""
        else:
            self.message = f"""Can't find the corresponding option in the autocomplete"""
        super().__init__(self.message)
