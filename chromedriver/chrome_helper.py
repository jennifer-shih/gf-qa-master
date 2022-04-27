import sys

sys.path.append(".")
import os
import platform
import zipfile
from time import sleep

import requests
from rich import print

from chromedriver import file_util
from config import globalparameter as gl

CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com"
CHROME_DRIVER_FOLDER = gl.project_path / "chromedriver"
CHROME_DRIVER_MAPPING_FILE = str(CHROME_DRIVER_FOLDER / "mapping.json")
CHROME_DRIVER_EXE = str(CHROME_DRIVER_FOLDER / "chromedriver.exe")
CHROMW_DRIVER_EXE_FOR_MAC = str(CHROME_DRIVER_FOLDER / "chromedriver")
CHROME_DRIVER_EXE_FOR_LINUX = str(CHROME_DRIVER_FOLDER / "chromedriver")
CHROME_DRIVER_ZIP = str(CHROME_DRIVER_FOLDER / "chromedriver_win32.zip")
CHROME_DRIVER_ZIP_FOR_MAC = str(CHROME_DRIVER_FOLDER / "chromedriver_mac64.zip")
CHROME_DRIVER_ZIP_FOR_LINUX = str(CHROME_DRIVER_FOLDER / "chromedriver_linux64.zip")


def get_chrome_driver_major_version():
    chrome_browser_path_x64 = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_browser_path_x86 = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    chrome_browser_path_mac = r"/Applications/Google Chrome.app"
    chrome_browser_path_linux = r"/usr/bin/google-chrome"
    system_name = platform.system()
    if system_name == "Darwin":  # mac os
        chrome_ver = file_util.get_file_version_for_mac(chrome_browser_path_mac)
    elif system_name == "Windows":
        try:
            chrome_ver = file_util.get_file_version(chrome_browser_path_x86)
        except FileNotFoundError:
            chrome_ver = file_util.get_file_version(chrome_browser_path_x64)
    elif system_name == "Linux":
        chrome_ver = file_util.get_file_version_for_linux(chrome_browser_path_linux).split()[2]
    else:
        Exception("The system is not supported")

    chrome_major_ver = chrome_ver.split(".")[0]
    return chrome_major_ver


def get_latest_driver_version(browser_ver):
    latest_api = "{}/LATEST_RELEASE_{}".format(CHROME_DRIVER_BASE_URL, browser_ver)
    resp = requests.get(latest_api)
    lastest_driver_version = resp.text.strip()
    return lastest_driver_version


def download_driver(driver_ver, dest_folder):
    if platform.system() == "Darwin":  # mac os
        download_api = "{}/{}/chromedriver_mac64.zip".format(CHROME_DRIVER_BASE_URL, driver_ver)
    elif platform.system() == "Windows":
        download_api = "{}/{}/chromedriver_win32.zip".format(CHROME_DRIVER_BASE_URL, driver_ver)
    elif platform.system() == "Linux":
        download_api = "{}/{}/chromedriver_linux64.zip".format(CHROME_DRIVER_BASE_URL, driver_ver)
    else:
        Exception("The system is not supported")
    dest_path = os.path.join(dest_folder, os.path.basename(download_api))
    resp = requests.get(download_api, stream=True, timeout=300)

    if resp.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(resp.content)
        print("[bold cyan]Download driver completed[/]")
    else:
        raise Exception("Download chrome driver failed")


def unzip_driver_to_target_path(src_file, dest_path):
    print("[yellow]Unzip {} -> {}[/]".format(src_file, dest_path))
    with zipfile.ZipFile(src_file, "r") as zip_ref:
        zip_ref.extractall(dest_path)
    os.remove(src_file)


def read_driver_mapping_file():
    driver_mapping_dict = {}
    if os.path.exists(CHROME_DRIVER_MAPPING_FILE):
        driver_mapping_dict = file_util.read_json(CHROME_DRIVER_MAPPING_FILE)
    return driver_mapping_dict


def check_browser_driver_available():
    chrome_major_ver = get_chrome_driver_major_version()
    mapping_dict = read_driver_mapping_file()
    driver_ver = get_latest_driver_version(chrome_major_ver)

    if (
        platform.system() not in mapping_dict
        or chrome_major_ver not in mapping_dict[platform.system()]
        or not os.path.exists(get_driver_path())
    ):
        download_driver(driver_ver, str(CHROME_DRIVER_FOLDER))
        system_name = platform.system()
        if system_name == "Darwin":  # mac os
            unzip_driver_to_target_path(CHROME_DRIVER_ZIP_FOR_MAC, str(CHROME_DRIVER_FOLDER))
            sleep(5)
            os.chmod(get_driver_path(), 755)
        elif system_name == "Windows":
            unzip_driver_to_target_path(CHROME_DRIVER_ZIP, str(CHROME_DRIVER_FOLDER))
        elif system_name == "Linux":
            unzip_driver_to_target_path(CHROME_DRIVER_ZIP_FOR_LINUX, str(CHROME_DRIVER_FOLDER))
            os.chmod(get_driver_path(), 755)
        else:
            Exception("The system is not supported")

        mapping_dict = {
            platform.system(): {
                chrome_major_ver: {
                    "driver_path": CHROMW_DRIVER_EXE_FOR_MAC,
                    "driver_version": driver_ver,
                }
            }
        }

        mapping_dict.update(mapping_dict)
        file_util.write_json(CHROME_DRIVER_MAPPING_FILE, mapping_dict)


def get_driver_path():
    if platform.system() == "Darwin":  # mac os
        return CHROMW_DRIVER_EXE_FOR_MAC
    elif platform.system() == "Windows":
        return CHROME_DRIVER_EXE
    elif platform.system() == "Linux":
        return CHROME_DRIVER_EXE_FOR_LINUX
    else:
        raise Exception("The OS is NOT support.")


# if __name__ == "__main__":
#     check_browser_driver_available()
