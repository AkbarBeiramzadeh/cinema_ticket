from uuid import uuid4
import json


class BankAccount:
    __min_balance = 10_000
    __commission = 600
    user_bank_account_json_dict = {}
    user_bank_account_dict = {}

    def __init__(self, id_user, balance, password, cvv2):
        self.id_user = id_user
        self._balance = balance
        self.__password = password
        self.__cvv2 = cvv2
        self.id_bank_account = uuid4().hex

    @staticmethod
    def amount_is_valid(amount: int):
        if amount > 0:
            return True
        raise Exception("The amount value is negative")

    @classmethod
    def balance_is_valid(cls, balance: int):
        if balance > cls.__min_balance:
            return True
        raise Exception("The minimum balance is not enough")

    def add_to_balance(self, amount):
        if type(self).amount_is_valid(amount):
            self._balance += amount

    def sub_from_balance(self, amount):
        if type(self).amount_is_valid(amount):
            if self._balance - amount > self.__min_balance:
                self._balance -= amount
            else:
                raise Exception("balance is not enough")

    def transfer(self, other: "BankAccount", amount: int):
        if type(self).amount_is_valid(amount):
            if self._balance - self.__commission - amount > self.__min_balance:
                self._balance -= (amount + self.__commission)
                other._balance += amount
            else:
                raise Exception("balance is not enough")

    def password_validation(self, password):
        if self.__password == password:
            return True
        raise Exception("The password is not valid")

    def cvv2_validation(self, cvv2):
        if self.__cvv2 == cvv2:
            return True
        raise Exception("The cvv2 is not valid")

    @classmethod
    def creat_bank_account(cls, id_user, balance, password, cvv2):
        if cls.balance_is_valid(balance):
            if id_user not in cls.user_bank_account_dict:
                cls.user_bank_account_json_dict[id_user] = {}
                cls.user_bank_account_dict[id_user] = {}
            bank_account = cls(id_user, balance, password, cvv2)
            cls.user_bank_account_json_dict[id_user][bank_account.id_bank_account] = {
                "bank account id": bank_account.id_bank_account, "balance": balance, "password": password, "cvv2": cvv2
            }
            cls.user_bank_account_dict[id_user][bank_account.id_bank_account] = bank_account
            json_string = json.dumps(cls.user_bank_account_json_dict)
            with open("bank_account.json", "w+") as f:
                f.write(json_string)
            return bank_account
