from uuid import uuid4
import json
import os
import logging

logging.basicConfig(level=logging.INFO, filename="cinematicket.log",
                    format="%(asctime)s - %(levelname)s - %(lineno)d - %(msg)s")
logger = logging.getLogger("bankaccount")

file_handler = logging.FileHandler("cinematicket.log")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
pattern = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(msg)s")
console_handler.setFormatter(pattern)
file_handler.setFormatter(pattern)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class BankAccount:
    __min_balance = 10_000
    __commission = 600
    user_bank_account_json_dict = {}
    user_bank_account_dict = {}

    def __init__(self, id_user, balance, bank_password, cvv2: int):
        self.id_user = id_user
        self._balance = balance
        self.__bank_password = bank_password
        self.__cvv2 = cvv2
        self.id_bank_account = uuid4().hex

    @staticmethod
    def amount_is_valid(amount: int):
        if amount > 0:
            return True
        else:
            logger.exception("Negative amount")
            raise Exception("The amount value is negative")

    @classmethod
    def balance_is_valid(cls, balance: int):
        if balance > cls.__min_balance:
            return True
        else:
            logger.error("NOT enough balance")
            raise Exception("The minimum balance is not enough")

    @classmethod
    def add_to_balance(cls, id_user, id_bank_account, bank_password, cvv2, amount):
        if cls.check_bank_password_and_cvv2_and_id_bank_account_validity(id_user, id_bank_account, bank_password, cvv2):
            with open("bank_account.json", "r") as f:
                bank_account_of_user_json = json.load(f)
                balance = bank_account_of_user_json[id_user][id_bank_account]["balance"]
            if cls.amount_is_valid(amount):
                balance += amount
                bank_account_of_user_json[id_user][id_bank_account]["balance"] = balance
                creat_bank_account_json_string = json.dumps(bank_account_of_user_json)
                with open("bank_account.json", "w+") as f:
                    f.write(creat_bank_account_json_string)
            else:
                logger.error("NOT enough balance")
                raise Exception("balance is not enough")

    @classmethod
    def sub_from_balance(cls, id_user, id_bank_account, bank_password, cvv2, amount):
        if cls.check_bank_password_and_cvv2_and_id_bank_account_validity(id_user, id_bank_account, bank_password, cvv2):
            with open("bank_account.json", "r") as f:
                bank_account_of_user_json = json.load(f)
                balance = bank_account_of_user_json[id_user][id_bank_account]["balance"]
            if cls.amount_is_valid(amount):
                if balance - amount > cls.__min_balance:
                    balance -= amount
                    bank_account_of_user_json[id_user][id_bank_account]["balance"] = balance
                    creat_bank_account_json_string = json.dumps(bank_account_of_user_json)
                    with open("bank_account.json", "w+") as f:
                        f.write(creat_bank_account_json_string)
                else:
                    logger.error("NOT enough balance")
                    raise Exception("balance is not enough")

    @classmethod
    def transfer(cls, wallet, id_user, id_bank_account, bank_password, cvv2, amount):
        if cls.check_bank_password_and_cvv2_and_id_bank_account_validity(id_user, id_bank_account, bank_password, cvv2):
            with open("bank_account.json", "r") as f:
                bank_account_of_user_json = json.load(f)
                balance = bank_account_of_user_json[id_user][id_bank_account]["balance"]
            if cls.amount_is_valid(amount):
                if balance - amount - cls.__commission > cls.__min_balance:
                    balance -= (amount + cls.__commission)
                    new_wallet = wallet + amount
                    bank_account_of_user_json[id_user][id_bank_account]["balance"] = balance
                    creat_bank_account_json_string = json.dumps(bank_account_of_user_json)
                    with open("bank_account.json", "w+") as f:
                        f.write(creat_bank_account_json_string)
                    return new_wallet
                else:
                    logger.error("NOT enough balance")
                    raise Exception("balance is not enough")

    @classmethod
    def check_bank_password_and_cvv2_and_id_bank_account_validity(
            cls, id_user, id_bank_account, bank_password, cvv2):
        if os.path.exists("bank_account.json"):
            with open("bank_account.json", "r") as f:
                bank_account_of_user_json = json.load(f)
            if id_user in bank_account_of_user_json.keys():
                if id_bank_account in bank_account_of_user_json[id_user]:
                    if bank_password == bank_account_of_user_json[id_user][id_bank_account]["bank_password"]:
                        if cvv2 == bank_account_of_user_json[id_user][id_bank_account]["cvv2"]:
                            balance = bank_account_of_user_json[id_user][id_bank_account]["balance"]
                            return True
                        else:
                            logger.error("Wrong CCV2")
                            raise Exception("The cvv2 is not valid")
                    else:
                        logger.error("unvalid password")
                        raise Exception("The password is not valid")
                else:
                    logger.error("unvalid band ID")
                    raise Exception("The id_bankaccount is not valid")
            else:
                logger.error("you don't have a bank account")
                raise Exception("You have not Bank Account")

    @classmethod
    def creat_bank_account(cls, id_user, balance, bank_password, cvv2):
        if len(bank_password) >= 4:
            if cls.balance_is_valid(balance):
                if id_user not in cls.user_bank_account_dict.keys():
                    cls.user_bank_account_json_dict[id_user] = {}
                    cls.user_bank_account_dict[id_user] = {}
                bank_account = cls(id_user, balance, bank_password, cvv2)
                cls.user_bank_account_json_dict[id_user][bank_account.id_bank_account] = {
                    "bank account id": bank_account.id_bank_account, "balance": balance, "bank_password": bank_password,
                    "cvv2": cvv2
                }
                cls.user_bank_account_dict[id_user][bank_account.id_bank_account] = bank_account
                creat_bank_account_json_string = json.dumps(cls.user_bank_account_json_dict)
                with open("bank_account.json", "w+") as f:
                    f.write(creat_bank_account_json_string)
                return bank_account
        else:
            logger.error("enter four characters and more")
            raise ValueError("Enter at least four characters for password")

    @classmethod
    def show_bank_account(cls, id_user):
        if os.path.exists("bank_account.json"):
            with open("bank_account.json", "r") as f:
                bank_account_of_user_json = json.load(f)
            if id_user in bank_account_of_user_json.keys():
                for id_of_bank in bank_account_of_user_json[id_user]:
                    print("id of bank account: ", id_of_bank)
            else:
                logger.error("you don't have a bank account")
                raise Exception("You have not Bank Account")
        else:
            logger.error("you don't have a bank account")
            raise Exception("You have not Bank Account")