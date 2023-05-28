from uuid import uuid4
import json


class User:
    users_dict = {}

    def __init__(self, name, password, birth_date, register_date, wallet, subscription, phone_number=None):
        self.name = name
        self.password = password
        self.birth_date = birth_date
        self.register_date = register_date
        self.wallet = wallet
        self.subscription = subscription
        self.phone_number = phone_number
        self.id_user = uuid4().hex

    @classmethod
    def sign_up(cls, name, password, birth_date, register_date, wallet, subscription, phone_number):
        """
        This function is a method class used to create a new user and
        also validates the received values.
        """
        if name not in cls.users_dict.keys() and name != "" and len(password) >= 4:
            cls.users_dict[name] = {"password": password,
                                    "birth_date": f"{birth_date.year}-{birth_date.month}-{birth_date.day}",
                                    "register_date":
                                        f"{register_date.year}-{register_date.month}-{register_date.day}",
                                    "phone": phone_number}
            # storing to the json file
            json_string = json.dumps(cls.users_dict)
            with open("users_json.json", "w+") as f:
                f.write(json_string)

            return cls(name, password, birth_date, register_date, wallet, subscription, phone_number)
        raise Exception
