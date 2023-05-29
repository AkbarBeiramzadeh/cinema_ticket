from uuid import uuid4
import json
import os


class User:
    users_dict = {}

    def __init__(self, name, password, birth_date, register_date, phone_number=None):
        self.name = name
        self.password = password
        self.birth_date = birth_date
        self.register_date = register_date
        self.wallet = 0
        self.subscription = 0
        self.phone_number = phone_number
        # if self.users_dict[name] in self.users_dict.keys():
        #     self.id_user = self.users_dict[name]["id_user"]

    @classmethod
    def sign_up(cls, name, password, birth_date, register_date, phone_number=None):
        """
        This function is a method class used to create a new user and
        also validates the received values.
        """
        if name != "" and len(password) >= 4:
            cls.users_dict[name] = {
                "id_user": uuid4().hex,
                "password": password,
                "birth_date": f"{birth_date.year}-{birth_date.month}-{birth_date.day}",
                "register_date":
                    f"{register_date.year}-{register_date.month}-{register_date.day}",
                "phone": phone_number}
            # storing to the json file
            json_string = json.dumps(cls.users_dict)
            with open("users_json.json", "w+") as f:
                f.write(json_string)

            return cls(name, password, birth_date, register_date, phone_number)
        raise Exception

    @classmethod
    def is_user(cls, user_name):
        if os.path.exists("users_json.json"):
            with open("users_json.json", "r") as f:
                user_json = json.load(f)
            for user in user_json.keys():
                if user not in cls.users_dict.keys():
                    cls.users_dict[user] = user_json[user]
            if user_name in cls.users_dict.keys():
                return True
        return False

    @classmethod
    def check_password(cls, name, password):
        if cls.users_dict[name]["password"] == password:
            return True
        return False


    @classmethod
    def change_username_and_phone_number(cls, name, new_name, new_phone_number= None):

        """
        This function changes the username and phone number
        """  
        if not cls.users_dict.keys(new_name):
            cls.users_dict[new_name] = cls.users_dict.pop(name)
            cls.users_dict[new_name].name = new_name
            cls.users_dict[new_name].phone_number = new_phone_number
            json_string = json.dumps(cls.users_dict)
            with open("users_json.json", "w+") as f:
                f.write(json_string)
        raise Exception("The name is exsist. try again")    