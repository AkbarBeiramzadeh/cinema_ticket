import json


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
