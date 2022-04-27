import json
import os
import subprocess

from rich import print


def get_file_version(file_path):
    print('[black bold]Get file version of[/] "{0}"'.format(file_path))
    if not os.path.isfile(file_path):
        raise FileNotFoundError("{!r} is not found.".format(file_path))
    from win32com import client as wincom_client

    wincom_obj = wincom_client.Dispatch("Scripting.FileSystemObject")
    version = wincom_obj.GetFileVersion(file_path)
    print('[black bold]The file version of[/] "{0}" is [yellow]"{1}"[/]'.format(file_path, version))
    return version.strip()


def get_file_version_for_mac(file_path):
    import macApp

    chrome = macApp.App(file_path)
    return chrome.version.version


def get_file_version_for_linux(file_path):
    result = subprocess.run(["google-chrome", "--version"], stdout=subprocess.PIPE)
    return result.stdout.decode()


def write_json(file_path, data):
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=2)


def read_json(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data
