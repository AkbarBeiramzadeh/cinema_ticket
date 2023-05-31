import json
import os
from uuid import uuid4
import logging

logging.basicConfig(level=logging.INFO, filename="cinematicket.log",
                    format="%(asctime)s - %(levelname)s - %(lineno)d - %(msg)s")
logger = logging.getLogger("manager")

#file_handler = logging.FileHandler("cinematicket.log")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
pattern = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(msg)s")
console_handler.setFormatter(pattern)
#file_handler.setFormatter(pattern)
logger.addHandler(console_handler)
#logger.addHandler(file_handler)


class Manager:
    manager_json_dict = {}

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @classmethod
    def create_manager(cls, name, password):
        if name not in cls.manager_json_dict.keys():
            id_manager = uuid4().hex
            cls.manager_json_dict[name] = {"id_manager": id_manager, "password": password}
            # storing to the json file
            json_string = json.dumps(cls.manager_json_dict)
            with open("manager.json", "w+") as f:
                f.write(json_string)
            return cls(name, password)
        raise Exception("Error")

    @staticmethod
    def is_manger(name):
        if os.path.exists("manager.json"):
            with open("manager.json", "r") as f:
                manager_dict = json.load(f)
            if name in manager_dict.keys():
                return True
        return False

    @staticmethod
    def check_password(name, password):
        if os.path.exists("manager.json"):
            with open("manager.json", "r") as f:
                manager_dict = json.load(f)
            if manager_dict[name]["password"] == password:
                return True
        return False