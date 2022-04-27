import urllib.parse

import requests
from requests.exceptions import RequestException

import config.globalparameter as gl
from src.api.gofreight_config import GBy, GoFreightConfig


class Me:
    def __init__(self, host: str, username: str, password: str):
        API = "/api/user/me/"
        response = requests.get(urllib.parse.urljoin(host, API), auth=(username, password))
        if response.status_code != 200:
            raise RequestException(
                "Me API failed. Maybe there is some problem with the server, or the username or the password is wrong."
            )

        self.config = response.json()
        self.username = self.config["username"]  # e.g. op_joey
        self.office = self.config["default_office"]  # default office id
        self.department = self.config["default_department"]  # default_department id
        self.id = self.config["id"]  # e.g. 11, user id
        self.roles = self.config["groups"]  # e.g. [{code: "OP", name: "Operation"}]

        gfc = GoFreightConfig(
            host,
            gl.companyConfig[gl.company]["sa"],
            gl.companyConfig[gl.company]["sa_password"],
        )
        self.date_format = gfc.get_date_format(self.office, GBy.OID)
        self.date_time_format = f"{self.date_format} %H:%M"
