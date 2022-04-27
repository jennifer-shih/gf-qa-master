import urllib.parse
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import globalparameter as gl
from src.drivers.expected_conditions import (
    element_clickable_and_uncovered,
    element_exist_and_disabled,
    element_exist_and_uncovered,
)
from src.helper.img_tool import concat_pic
from src.helper.log import Logger
from src.helper.retry import retry


class Driver:
    _instance = None
    _name = None
    _drivers = {}
    _drivers_info = {}

    def __new__(cls, name: str, driver_path: str, monitor: str = "0", page_load_timeout: float = 2400):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        if name not in cls._drivers or cls.get_driver(name).session_id == None:
            cls._drivers[name] = cls._init_driver(driver_path, str(monitor), page_load_timeout)
            cls._drivers_info[name] = {
                "name": name,
                "driver_path": driver_path,
                "monitor": str(monitor),
                "page_load_timeout": page_load_timeout,
            }
            cls._name = name
        return cls._instance

    def __init__(self, name: str, driver_path: str, monitor: str = "0", page_load_timeout: float = 2400):
        pass

    @retry(times=2, exceptions=(WebDriverException))
    @staticmethod
    def _init_driver(driver_path: str, monitor: str, page_load_timeout):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": str(gl.download_path)}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--lang=en-US")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("enable-automation")

        if monitor == "0":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument(
                "--window-size=1920,1080"
            )  # if not set by argument, the new tab or new browser will not apply the setting
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        elif monitor == "1":
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
            driver.set_window_position(0, 0)
            driver.maximize_window()

        driver.set_page_load_timeout(page_load_timeout)
        return driver

    @classmethod
    def get_driver(cls, name=None) -> webdriver.Chrome:
        if name == None:
            return cls._drivers[cls._name]
        elif name not in cls._drivers:
            raise Exception(f"Driver [{name}] does not exist")
        else:
            cls._name = name
            return cls._drivers[name]

    @classmethod
    def get_driver_info(cls, name=None):
        if name == None:
            return cls._drivers_info[cls._name]
        elif name not in cls._drivers_info:
            raise Exception(f"Driver [{name}] does not exist")
        else:
            return cls._drivers_info[name]

    @classmethod
    def open(cls, url: str) -> None:
        """
        Open an url in current tab. Dismiss the popup alert if it exists
        """
        Logger.getLogger().debug("Open url [{0}]".format(url))
        cls.get_driver().get(url)

        cls.manipulate_alert()
        sleep(3)

    @classmethod
    def open_new_tab(cls) -> None:
        """
        Open a new window
        """
        cls.get_driver().switch_to.new_window("tab")

    @classmethod
    def previous(cls) -> None:
        """
        Goes back to the previous web page
        """
        Logger.getLogger().debug("Goes back to the previous page")
        cls.get_driver().back()

        cls.manipulate_alert()
        sleep(3)

    @classmethod
    def refresh(cls) -> None:
        Logger.getLogger().debug("Refresh")
        cls.get_driver().refresh()

        cls.manipulate_alert()
        sleep(3)

    @classmethod
    def close(cls) -> None:
        """
        Close current window
        """
        Logger.getLogger().debug("Close tab")
        cls.get_driver().close()

    @classmethod
    def quit(cls, name=None) -> None:
        """
        Close the browser
        """
        if name == None:
            name = cls._name
        if name not in cls._drivers:
            raise Exception(f"Driver [{name}] does not exist")
        Logger.getLogger().debug(f"Close browser [{name}]")
        curr_driver = cls.get_driver(name)
        curr_driver.quit()
        curr_driver.session_id = None
        cls._drivers.pop(name)
        cls._drivers_info.pop(name)

    @classmethod
    def restart(cls, name=None) -> None:
        if name == None:
            name = cls._name
        Logger.getLogger().debug(f"Restart browser [{name}]")
        driver_info = cls.get_driver_info(name)
        cls.quit(name)
        cls._drivers[name] = cls._init_driver(
            driver_info["driver_path"],
            driver_info["monitor"],
            driver_info["page_load_timeout"],
        )
        cls._drivers_info[name] = {
            "name": name,
            "driver_path": driver_info["driver_path"],
            "monitor": driver_info["monitor"],
            "page_load_timeout": driver_info["page_load_timeout"],
        }
        cls._name = name

    @classmethod
    def wait_element_enable(cls, locator: tuple, timeout: float = 3) -> WebElement | None:
        """
        Wait until the element satisfied all following conditions:
        1. Visible (On the DOM and has a height and width that is greater than 0)
        2. Enabled (such that you can click it)
        3. No spin bar presented

        Return the WebElement itself if the conditions are all satisfied, if not, return None.
        """
        try:
            ele = WebDriverWait(cls.get_driver(), timeout).until(element_clickable_and_uncovered((locator)))
            cls.scroll_element_into_view(ele)
            return ele
        except:
            return None

    @classmethod
    def wait_element_disabled(cls, locator: tuple, timeout: float = 5) -> WebElement | None:
        """
        Wait until the element satisfied all following conditions:
        1. Exist on the DOM
        2. Has a "disabled" or "readonly" attribute
        3. No spin bar presented

        Return the WebElement itself if the conditions are all satisfied, if not, return None.
        """
        ele = None
        try:
            ele = WebDriverWait(cls.get_driver(), timeout).until(element_exist_and_disabled((locator)))
            cls.scroll_element_into_view(ele)
            return ele
        except:
            return ele

    @classmethod
    def wait_element_visible(cls, locator: tuple, timeout: float = 5) -> WebElement | None:
        """
        Wait until the element satisfied all following conditions:
        1. Exist on the DOM
        2. No spin bar presented

        Return the WebElement itself if the conditions are all satisfied, if not, return None.
        """
        try:
            ele = WebDriverWait(cls.get_driver(), timeout).until(element_exist_and_uncovered((locator)))
            cls.scroll_element_into_view(ele)
            return ele
        except:
            return None

    @classmethod
    def wait_element_exist(cls, locator: tuple, timeout: float = 5) -> WebElement | None:
        """
        Wait until the element satisfied all following conditions:
        1. Exist on the DOM

        Return the WebElement itself if the conditions are all satisfied, if not, return None.
        """
        try:
            ele = WebDriverWait(cls.get_driver(), timeout).until(EC.presence_of_element_located((locator)))
            cls.scroll_element_into_view(ele)
            return ele
        except:
            return None

    @classmethod
    def wait_element_invisible(cls, locator: tuple, timeout=5) -> WebElement | None:
        # return element
        try:
            return WebDriverWait(cls.get_driver(), timeout).until(EC.invisibility_of_element_located((locator)))
        except:
            return None

    @classmethod
    def num_of_element(cls, xpath: str) -> int:
        return len(Driver.get_driver().find_elements_by_xpath(xpath))

    @classmethod
    def move_mouse_to(cls, element: WebElement) -> None:
        ActionChains(cls.get_driver()).move_to_element(element).perform()

    @classmethod
    def drag_and_drop(cls, element: WebElement, target_ele: WebElement) -> None:
        ActionChains(cls.get_driver()).drag_and_drop(element, target_ele).perform()

    @classmethod
    def drag_and_drop_by_offset(cls, element: WebElement, offset: tuple = (0, 0)) -> None:
        """
        offset: (x, y)
        """
        ActionChains(cls.get_driver()).drag_and_drop_by_offset(element, offset[0], offset[1]).perform()

    @classmethod
    def is_url_match(cls, url: str) -> bool:
        return url in cls.get_driver().current_url

    @classmethod
    def is_url_fully_match(cls, url: str) -> bool:
        current_url = cls.get_driver().current_url
        Logger.getLogger().debug(
            "current url [{0}] is equal [{1}] ? [{2}] ".format(current_url, url, url == current_url)
        )

        return url == current_url

    @classmethod
    def is_title_match(cls, text: str) -> str:
        return text in cls.get_driver().title

    @classmethod
    def is_text_in_page_source(cls, text: str) -> bool:
        return text in cls.get_driver().page_source

    @classmethod
    def get_url(cls) -> str:
        return cls.get_driver().current_url

    @classmethod
    def get_logout_redirect_url(cls):
        route = cls.get_driver().current_url.replace(gl.URL.DASHBOARD, "")
        redirect = "/login/?next=" + route
        return urllib.parse.urljoin(gl.URL.DASHBOARD, redirect)

    @classmethod
    def take_screenshot_as_png(cls) -> bytes:
        return cls.get_driver().get_screenshot_as_png()

    @classmethod
    def get_screenshot_as_file(cls, path: Path | str) -> bool:
        # TODO or not... https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver
        path = Path(path)
        folder = path.parent
        if not folder.exists():
            folder.mkdir(parents=True)
        try:
            cls.get_driver().get_screenshot_as_file(str(path.as_posix()))
            return True
        except Exception as e:
            Logger.getLogger().error(f"get_screenshot_as_file occur error:\n{e}")
            return False

    @classmethod
    def get_screenshot_for_all_windows(cls, path: Path | str) -> None:
        driver = cls.get_driver()
        path = Path(path)
        folder = path.parent
        screenshoots = []

        if not folder.exists():
            folder.mkdir(parents=True)
        i = 1
        for h in driver.window_handles:
            driver.switch_to.window(h)
            p = "{0}_{1}{2}".format(str(folder / path.stem), i, path.suffix)
            if cls.get_screenshot_as_file(p):
                screenshoots.append(p)
                i += 1

        concat_pic(screenshoots, path)

    @classmethod
    def switch_to(cls, window_name: str = None, window_index: int = 0) -> None:
        """
        Switch the window (or tab) we are manipulating by specifying the name or the index of the window
        """
        driver = cls.get_driver()
        if window_name != None:
            is_found = False
            for h in driver.window_handles:
                driver.switch_to.window(h)
                if driver.title == str(window_name):
                    is_found = True
                    break
            if not is_found:
                raise NoSuchWindowException("Not found any window title match '{}'".format(window_name))
        elif window_index != None:
            driver.switch_to.window(driver.window_handles[int(window_index)])

    @classmethod
    def set_download_path(cls, path: Path) -> None:
        # ? 在 Headless mode 中，execute_cdp_cmd 不會 wrok 在新的 window，所以當遇到需要更改下載路經時，
        # ? 必須確定 driver 是處於 "執行下載動作的 window" ，再執行這項指令才會生效
        # path 必須是絕對路徑(windows下)
        # path = path.resolve().as_posix()
        # path = os.path.abspath(str(path))
        path = str(Path(path).resolve())
        params = {"behavior": "allow", "downloadPath": path}
        cls.get_driver().execute_cdp_cmd("Page.setDownloadBehavior", params)
        Logger.getLogger().info("Set the download path to {}".format(path))

    @classmethod
    def go_to_position(cls, x_coord: int, y_coord: int) -> None:
        cls.get_driver().execute_script("window.scrollTo(" + str(x_coord) + "," + str(y_coord) + ")")

    @classmethod
    def scroll_to_bottom(cls) -> None:
        cls.get_driver().execute_script("window.scrollTo(0,document.body.scrollHeight);")

    @classmethod
    def scroll_up_by_element(cls, ele, times=10, timeout=5) -> None:
        cls._scroll_by_element(ele, 3, times, timeout)

    @classmethod
    def scroll_down_by_element(cls, ele, times=10, timeout=5) -> None:
        cls._scroll_by_element(ele, 4, times, timeout)

    @classmethod
    def scroll_right_by_element(cls, ele, times=10, timeout=5) -> None:
        cls._scroll_by_element(ele, 2, times, timeout)

    @classmethod
    def scroll_left_by_element(cls, ele, times=10, timeout=5) -> None:
        cls._scroll_by_element(ele, 1, times, timeout)

    @classmethod
    def scroll_top_by_element(cls, ele, timeout=5) -> None:
        element = WebDriverWait(cls.get_driver(), timeout).until(element_exist_and_uncovered((ele.locator)))
        ActionChains(cls.get_driver()).send_keys_to_element(element, Keys.HOME).perform()

    @classmethod
    def scroll_bottom_by_element(cls, ele, timeout=5) -> None:
        element = WebDriverWait(cls.get_driver(), timeout).until(element_exist_and_uncovered((ele.locator)))
        ActionChains(cls.get_driver()).send_keys_to_element(element, Keys.END).perform()

    @classmethod
    def _scroll_by_element(cls, ele, direction: int, times, timeout=5):
        element = WebDriverWait(cls.get_driver(), timeout).until(element_exist_and_uncovered((ele.locator)))
        mapping = {1: Keys.LEFT, 2: Keys.RIGHT, 3: Keys.UP, 4: Keys.DOWN}
        for _ in range(times):
            ActionChains(cls.get_driver()).send_keys_to_element(element, mapping[direction]).perform()
            sleep(0.1)

    @classmethod
    def manipulate_alert(cls, accept: bool = True) -> None:
        """
        Accept or reject the browser's popup alert (Usually is 「要離開網站嗎？系統可能不會儲存你所做的變更。」)

        Currently, this function can manipulate popup dialogs, but it won't disappear from the UI for an unknown reason
        """
        try:
            alert = cls.get_driver().switch_to.alert
            if accept:
                alert.accept()
                Logger.getLogger().debug("Accept popup dialog")
            else:
                alert.dismiss()
                Logger.getLogger().debug("Dismiss popup dialog")
        except NoAlertPresentException:
            # Logger.getLogger().debug("No popup dialog appears")
            pass

    @classmethod
    def get_console_logs(cls):
        return cls.get_driver().get_log("browser")

    @classmethod
    def get_console_error_logs(cls):
        logs = []
        for log in cls.get_driver().get_log("browser"):
            if log["level"] == "SEVERE":
                logs.append(log)

        return logs

    @classmethod
    def zoom(cls, percent: float) -> None:
        """
        percent=50 -> 縮小50%
        percent=175 -> 放大70%
        """
        Logger.getLogger().debug(f"Zoom [{percent}%]")
        current = cls.get_url()
        cls.open("chrome://settings/")
        cls.get_driver().execute_script(f"chrome.settingsPrivate.setDefaultZoom({str(percent/100)});")
        cls.open(current)

    @classmethod
    def scroll_element_into_view(cls, element: WebElement) -> None:
        #! these not work
        # ActionChains(cls.get_driver()).move_to_element(ele).perform()
        # cls.get_driver().execute_script("arguments[0].scrollIntoView(false)", ele)
        #! bad, sometimes the element is still not in the view
        # position = ele.location_once_scrolled_into_view
        # cls.get_driver().execute_script("window.scrollTo({}, {})".format(position['x'], position['y']))

        scrollElementIntoMiddle = (
            "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
            + "var elementTop = arguments[0].getBoundingClientRect().top;"
            + "window.scrollBy(0, elementTop-(viewPortHeight/2));"
        )

        cls.get_driver().execute_script(scrollElementIntoMiddle, element)

    @classmethod
    def set_page_load_timeout(cls, timeout) -> None:
        cls.get_driver().set_page_load_timeout(timeout)

    @classmethod
    def set_default_page_load_timeout(cls, name=None) -> None:
        page_load_timeout = cls.get_driver_info(name)["page_load_timeout"]
        cls.set_page_load_timeout(page_load_timeout)
