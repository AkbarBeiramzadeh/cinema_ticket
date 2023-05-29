import json
import os


class Manager:
    manager_json_dict = {}

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @classmethod
    def create_manager(cls, name, password):
        if name not in cls.manager_json_dict.keys():
            cls.manager_json_dict[name] = password
            # storing to the json file
            json_string = json.dumps(cls.manager_json_dict)
            with open("manager.json", "w+") as f:
                f.write(json_string)
            return cls(name, password)
        raise Exception("Error")

    @classmethod
    def is_manger(cls, name):
        if os.path.exists("manager.json"):
            with open("manager.json", "r") as f:
                manager_dict = json.load(f)
            if name in manager_dict.keys():
                return True
        return False

    @classmethod
    def check_password(cls, name, password):
        if os.path.exists("manager.json"):
            with open("manager.json", "r") as f:
                manager_dict = json.load(f)
            if manager_dict[name] == password:
                return True
        return False
