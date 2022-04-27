import urllib.parse

import requests

"""
Config api:
    host_id (str): current host id
    company (dict): config of 'Company Management'
    offices (list): list of offices in 'Office Management'
    system_configs (list): list of Target in 'System Configuration'
    currencies (list): list of currencies in 'Currency' section of 'Company Management'
    office_currencies: None
Usage:
    gfc = GoFreightConfig('https://fms-autotest.gofreight.co', 'hardcore', 'hardc0re')
    print(gfc.get_default_filing_no_format('LAX', GBy.ONAME))
    print(gfc.get_default_filing_no_format(1, GBy.OID))
"""


class GBy:
    OID = "office id"
    ONAME = "office short name"


class GoFreightConfig:
    CONFIG_API = "/api/superuser/dump-config/"
    PACKAGE_UNIT_API = "/api/options/?choices=package_unit"
    DEPARTMENT_LIST_API = "/api/office-department/list/"

    def __init__(self, host: str, admin_username: str, admin_password: str):
        if not host:
            raise ValueError(
                f"host: [{host}] is invalid. Please fill in correct GoFreight server url in company_config.yml"
            )
        self._host = host
        self._admin_username = admin_username
        self._admin_password = admin_password
        self.update()

    def update(self):
        response = requests.get(
            urllib.parse.urljoin(self._host, self.CONFIG_API),
            auth=(self._admin_username, self._admin_password),
        )
        if response.status_code == 200:
            self.config = response.json()
        else:
            raise requests.exceptions.RequestException(
                "Get Gofreight config request failed. Maybe the server has some problem, or the username or the password is wrong."
            )

        self.package_unit_mapping = self._to_package_unit_mapping(
            requests.get(
                urllib.parse.urljoin(self._host, self.PACKAGE_UNIT_API),
                auth=(self._admin_username, self._admin_password),
            ).json()["package_unit"]
        )

        self.package_unit_mapping = self._to_package_unit_mapping(
            requests.get(
                urllib.parse.urljoin(self._host, self.PACKAGE_UNIT_API),
                auth=(self._admin_username, self._admin_password),
            ).json()["package_unit"]
        )
        self.department_info = self._to_department_mapping(
            requests.get(
                urllib.parse.urljoin(self._host, self.DEPARTMENT_LIST_API),
                auth=(self._admin_username, self._admin_password),
            ).json()
        )

    @staticmethod
    def _to_package_unit_mapping(units):
        mapping = {}
        for u in units:
            mapping[u["id"]] = u["text"]
        return mapping

    @staticmethod
    def _to_department_mapping(department_info: list) -> dict:
        mapping = {}
        for info in department_info:
            office_id = info["id"]
            dept_mapping = {}
            for d in info["office_department_set"]:
                dept_mapping[d["id"]] = d
            mapping[office_id] = dept_mapping
        return mapping

    def _system_config_by_id(self, office_id: int):
        self.update()
        # 'office' of default system config is None
        for selector in [office_id, None]:
            for office in self.config["system_configs"]:
                if office["office"] == selector:
                    return office

    def _office_by_id(self, office_id: int):
        self.update()
        for office in self.config["offices"]:
            if office["id"] == office_id:
                return office

    def _office_by_name(self, office_name: str):
        self.update()
        for office in self.config["offices"]:
            if office["short_name"] == office_name:
                return office

    def _office(self, d, strategy: str):
        if strategy == GBy.OID:
            return self._office_by_id(d)
        elif strategy == GBy.ONAME:
            return self._office_by_name(d)
        else:
            raise Exception(f"strategy: [{strategy}] is NOT existed")

    def _system_config(self, d, strategy: str):
        if strategy == GBy.OID:
            return self._system_config_by_id(d)
        elif strategy == GBy.ONAME:
            raise Exception(f"strategy: [{strategy}] is NOT allowed")
        else:
            raise Exception(f"strategy: [{strategy}] is NOT existed")

    def get_office_full_name(self, office: str, strategy: str):
        return self._office(office, strategy)["full_name"]

    def get_default_filing_no_format(self, office: str, strategy: str):
        return self._office(office, strategy)["filing_no_prefix_fmt"]

    def get_quotation_no_prefix(self, office: str, strategy: str):
        return self._office(office, strategy)["quotation_no_prefix"]

    def get_quotation_no_seq(self, office: str, strategy: str):
        return self._office(office, strategy)["quotation_no_seq"]

    def get_quotation_no_format(self, office: str, strategy: str):
        return self._office(office, strategy)["quotation_no_prefix_fmt"]

    def get_wh_receipt_no_prefix(self, office: str, strategy: str):
        return self._office(office, strategy)["wh_receipt_no_prefix"]

    def get_wh_receipt_no_seq(self, office: str, strategy: str):
        return self._office(office, strategy)["wh_receipt_no_seq"]

    def get_wh_receipt_no_format(self, office: str, strategy: str):
        return self._office(office, strategy)["wh_receipt_no_prefix_fmt"]

    def get_date_format(self, office, strategy: str):
        """
        Return the format of the date in string
        For example: "%m-%d-%Y"
        """
        return self._office(office, strategy)["date_fmt_default"]

    def get_ai_weight_decimal(self, office, strategy: str):
        """
        e.g., SFI
        office_id=None ->   Target=Company
        office_id=1    ->   Target=LAX
        """
        return self._system_config(office, strategy)["ai_weight_float_precision"]

    def get_default_package(self, office, strategy: str):
        pkg_unit_code = self._office(office, strategy)["package_unit"]
        return self.package_unit_mapping[pkg_unit_code]

    def get_measurement_decimal(self, office, strategy):
        return self._system_config(office, strategy)["measure_float_precision"]
