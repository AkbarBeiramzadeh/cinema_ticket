from uuid import uuid4
import json


class BankAccount:


    __min_balance = 10_000
    __commission = 600 
    bank_account_json_dict = {}
    bank_account_dict = {}
    user_bank_account_json_dict = {}
    user_bank_account_dict = {}



    def __init__(self, id_user, balance, password, cvv2):
        self.id_user = id_user
        self.balance = balance
        self.__password = password
        self.__cvv2 = cvv2
        self.id_bank_account = uuid4().hex()
        type(self).__accounts.append(self)


    @staticmethod
    def amount_is_valid(amount: int):
        if amount > 0:
            return True
        print("The amount value is negative")
        return False  


    @classmethod
    def balance_is_valid(cls, balance: int):
        if balance > cls.__min_balance:
            return True
        else:
            print("The minimum balance is not enough")
           
    
    def add_to_balance(self, amount):
        if type(self).amount_is_valid(amount):
            self._balance += amount


    def sub_from_balance(self, amount):
        if type(self).amount_is_valid(amount):    
            if self._balance - amount > self.__min_balance:
                self._balance -= amount
            else:
                print("balance is not enough")  


    def transfer(self, other: "BankAccount", amount: int):
        if type(self).amount_is_valid(amount):
            if self._balance - self.__commission - amount > self.__min_balance:
                self._balance -=( amount + self.__commission)
                other._balance += amount
            else:
                print("balance is not enough")


    def password_validation(self, password):
        if self.__password == password:
            return True
        print("The password is not valid")    
        return False


    def cvv2_validation(self, cvv2):
        if self.__cvv2 == cvv2:
            return True
        print("The cvv2 is not valid")    
        return False


    def creat_bank_account(self, id_user, balance, password, cvv2):
                bank_account = type(self)(id_user, balance, password, cvv2)
                type(self).bank_account_dict[self.id_bank_account] = bank_user
                type(self).bank_account_json_dict[self.id_bank_account] = {"bank account id": self.id_bank_account, "balance": balance, "password": password, "cvv2": cvv2}
                type(self).user_bank_account_dict[id_user] = type(self).bank_account_dict
                type(self).user_bank_account_json_dict[id_user]= type(self).bank_account_json_dict
                json_string = json.dumps(type(self).user_bank_account_json_dict)
                with open("bank_account.json", "w+") as f:
                    f.write(json_string)









    


