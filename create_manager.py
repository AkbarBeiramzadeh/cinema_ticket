import argparse
import json
import os
from manager import Manager
import logging

logging.basicConfig(level=logging.INFO, filename="cinematicket.log",
                    format="%(asctime)s - %(levelname)s - %(lineno)d - %(msg)s")
logger = logging.getLogger("create_manager")

#file_handler = logging.FileHandler("cinematicket.log")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
pattern = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(msg)s")
console_handler.setFormatter(pattern)
#file_handler.setFormatter(pattern)
logger.addHandler(console_handler)
#logger.addHandler(file_handler)

if os.path.exists("manager.json"):
    with open("manager.json", "r") as f:
        manager_json = json.load(f)
        for key in manager_json.keys():
            if key not in Manager.manager_json_dict.keys():
                Manager.manager_json_dict[key] = manager_json[key]

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='manager_name')
parser.add_argument('--password', help='manager_password')

args = parser.parse_args()
try:
    Manager.create_manager(args.name, args.password)
except Exception:
    logger.exception("This name has already been used.")


