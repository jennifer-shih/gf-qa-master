import sys
from pathlib import Path

import yaml

project_path = Path.cwd()

"""
Usage:
python set_variable.py SFI.url=https://fms-stage-qa-5.gofreight.co
"""


if __name__ == "__main__":
    settings = {}
    for arg in sys.argv[1:]:
        key, value = arg.split("=")
        print("[{0}]=[{1}]".format(key, value))
        settings[key] = value

    # read file
    with open(project_path / "config/company_config.yml", "r", encoding="UTF-8") as file:
        company_config = yaml.safe_load(file)

    for key, val in settings.items():
        keys = key.split(".")
        company = keys[0]
        attr = keys[1]
        company_config[company][attr] = val

    # write file
    with open(project_path / "config/company_config.yml", "w", encoding="UTF-8") as file:
        yaml.safe_dump(company_config, file, default_flow_style=False)
