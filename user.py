from uuid import uuid4
import json
import os
import logging

logging.basicConfig(level=logging.INFO, filename="cinematicket.log",
                    format="%(asctime)s - %(levelname)s - %(lineno)d - %(msg)s")
logger = logging.getLogger("user")

file_handler = logging.FileHandler("cinematicket.log")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
pattern = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(msg)s")
console_handler.setFormatter(pattern)
file_handler.setFormatter(pattern)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class User:
    users_dict = {}
    users_movies = {}
    subscription = ["Boronz", "Silver", "Gold"]

    def __init__(self, name, password, birth_date, register_date, phone_number=None):
        self.name = name
        self.password = password
        self.birth_date = birth_date
        self.register_date = register_date
        self.wallet = 0
        self.subscription = type(self).subscription[0]
        self.phone_number = phone_number
        # if self.users_dict[name] in self.users_dict.keys():
        #     self.id_user = self.users_dict[name]["id_user"]
        #logger.info('created user: {} - {} - {} - {} - {} - {} - {}'.format(self.name, self.password, self.birth_date,
        #                                                                    self.register_date, self.wallet, self.subscription,
        #                                                                    self.phone_number))

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
                "wallet": 0,
                "subscription": "Boronz",
                "phone": phone_number}


            # creating users_movie json -----------
            with open('users_movies.json', 'w+') as f3:
                cls.users_movies[name] = []
                json.dump(cls.users_movies, f3)
            # -------------------------------------


            # storing to the json file
            json_string = json.dumps(cls.users_dict)
            with open("users_json.json", "w+") as f:
                f.write(json_string)

            return cls(name, password, birth_date, register_date, phone_number)
        logger.exception("Wrong info")
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
        logger.error("wrong password")
        return False

    @staticmethod
    def show_wallet(name):
        with open("users_json.json", "r") as f:
            user_json = json.load(f)
        return user_json[name]["wallet"]

    @staticmethod
    def show_subscription_type(name):
        with open("users_json.json", "r") as f:
            user_json = json.load(f)
        return user_json[name]["subscription"]

    @classmethod
    def change_username_and_phone_number(cls, name, new_name, new_phone_number=None):

        """
        This function changes the username and phone number
        """
        if new_name not in cls.users_dict.keys():
            cls.users_dict[new_name] = cls.users_dict.pop(name)
            cls.users_dict[new_name]["phone"] = new_phone_number
            name = new_name
            json_string = json.dumps(cls.users_dict)
            with open("users_json.json", "w+") as f:
                f.write(json_string)
        else:
            logger.exception("this name already exist")
            raise Exception("The name is exist. try again")


    @staticmethod
    def show_wallet(name):
        with open("users_json.json", "r") as f:
            user_json = json.load(f)
        return user_json[name]["wallet"]

    @staticmethod
    def show_subscription_type(name):
        with open("users_json.json", "r") as f:
            user_json = json.load(f)
        return user_json[name]["subscription"]


    @classmethod
    def change_username_and_phone_number(cls, name, new_name, new_phone_number= None):

        """
        This function changes the username and phone number
        """  
        if new_name not in cls.users_dict.keys():
            cls.users_dict[new_name] = cls.users_dict.pop(name)
            cls.users_dict[new_name]["phone"] = new_phone_number
            name = new_name
            json_string = json.dumps(cls.users_dict)
            with open("users_json.json", "w+") as f:
                f.write(json_string)

        else:

        logger.exception("this name already exist")
        raise Exception("The name is exsist. try again")



    @classmethod

    def change_password(cls, name, password, new_password, re_new_password):
        if cls.check_password(name, password):

            if len(new_password) >= 4:
                if new_password == re_new_password:
                    cls.users_dict[name]["password"] = new_password
                    password = new_password
                    json_string = json.dumps(cls.users_dict)
                    with open("users_json.json", "w+") as f:
                        f.write(json_string)

                else:
                    logger.exception("new_password and re_new_password is not equal")
                    raise Exception("new_password and re_new_password is not equal")
            else:
                logger.exception("not enough character")
                raise Exception("Enter at least four characters for password")


