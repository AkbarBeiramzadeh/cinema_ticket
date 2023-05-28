import argparse
import json
import os
from manager import Manager

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
    print("This name has already been used.")


