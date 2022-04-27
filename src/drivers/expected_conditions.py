from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located

SPIN_BAR_LOCATOR = (By.XPATH, "//div[@class='page-spinner-bar']")


class element_clickable_and_uncovered:
    """
    An Expectation for checking an element is
    1. Visible (On the DOM and has a height and width that is greater than 0)
    2. Enabled (such that you can click it)
    3. No spin bar presented

    Return False if not all of the conditions are satisfied, and return the element itself if satisfied.
    """

    def __init__(self, locator):
        self.locator = locator
        self.spin_bar_locator = SPIN_BAR_LOCATOR

    def __call__(self, driver):
        try:
            element: WebElement = element_to_be_clickable(self.locator)(driver)
        except NoSuchElementException:
            return False

        if element:
            try:
                if presence_of_element_located(self.spin_bar_locator)(driver):
                    return False
                else:
                    return element
            except NoSuchElementException:
                return element
        else:
            return False


class element_exist_and_uncovered:
    """
    An Expectation for checking an element is
    1. Exist on the DOM
    2. No spin bar presented

    Return False if not all of the conditions are satisfied, and return the element itself if satisfied.
    """

    def __init__(self, locator):
        self.locator = locator
        self.spin_bar_locator = SPIN_BAR_LOCATOR

    def __call__(self, driver):
        try:
            element: WebElement = presence_of_element_located(self.locator)(driver)
        except NoSuchElementException:
            return False

        if element:
            try:
                if presence_of_element_located(self.spin_bar_locator)(driver):
                    return False
                else:
                    return element
            except NoSuchElementException:
                return element
        else:
            return False


class element_exist_and_disabled:
    """
    An Expectation for checking an element is
    1. Exist on the DOM
    2. Has a "disabled" or "readonly" attribute
    3. No spin bar presented

    Return False if not all of the conditions are satisfied, and return the element itself if satisfied.
    """

    def __init__(self, locator):
        self.locator = locator
        self.spin_bar_locator = SPIN_BAR_LOCATOR

    def __call__(self, driver):
        try:
            element: WebElement = presence_of_element_located(self.locator)(driver)
        except NoSuchElementException:
            return False

        if element:
            disabled = element.get_attribute("disabled")
            readonly = element.get_attribute("readonly")
            if disabled is None and readonly is None:
                return False

            try:
                if presence_of_element_located(self.spin_bar_locator)(driver):
                    return False
                else:
                    return element
            except NoSuchElementException:
                return element
        else:
            return False
