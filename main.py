import json
import os
from user import User
from manager import Manager
import getpass
import sys
from datetime import datetime
import BankAccount
import Movie


def register():
    """
    This function is used for user registration.
    The username should not be duplicated.
    The entered password should be equal to or greater than 4 characters in length.
    """
    name = input("Enter Your Name :")
    if User.is_user(name):
        print("This Name is taken already")
        return
    password = getpass.getpass(stream=sys.stderr, prompt="Enter Password : ")
    phone_number = input("Enter phone (optional): ")
    register_date = datetime.now()
    birth_date_str = input("Enter your birthday in the format YYYY-MM-DD : ")
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    try:
        User.sign_up(name, password, birth_date, register_date, phone_number)
        print("The User Registered Successfully!!!")
    except Exception:
        print("User not registered")


def show_users_info():
    """Mahsa"""
    pass


def edit_user(name):
    """Hesel"""
    new_name = input("Enter Your New Name :")
    new_phone_number = input("Enter Your New Phone Number :")
    if new_phone_number == "":
            new_phone_number = None    
    User.change_username_and_phone_number(name, new_name, new_phone_number)


def create_bank_account():
    """Akbar"""
    with open("users_json.json", "r") as f:
        user_json = json.load(f)
    id_user = user_json[name]["id_user"]
    balance = int(input("Enter Balance : "))
    password = input("Enter password : ")
    cvv2 = input("Enter CVV2 : ")
    BankAccount.creat_bank_account(id_user, balance, password, cvv2)


def change_password(name):
    """Hesel"""
    password = getpass.getpass(stream=sys.stderr, prompt="Enter Password : ")
    new_password = getpass.getpass(stream=sys.stderr, prompt="Enter New_Password : ")
    re_new_password = getpass.getpass(stream=sys.stderr, prompt="Enter Re_New_Password : ")
    User.change_password(name, password, new_password, re_new_password)


def show_bank_account():
    """Mahsa"""
    pass


def show_wallet():
    """Akbar"""
    pass


def charge_wallet():
    """Mahsa"""
    pass


def show_my_movies():
    """Hesel"""
    show_my_movies(id_user)
    Movie.


def show_my_subscription_type():
    """Akbar"""
    pass


def buy_movie():
    """Akbar"""
    pass


def login():
    name = input("Enter Your Name : ")
    if User.is_user(name):
        password = getpass.getpass(stream=sys.stderr, prompt="Enter Password : ")
        if User.check_password(name, password):
            print("-" * 30, "\tLogin Menu", "-" * 30, sep="\n")
            print("Please select an option:",
                  "1. Show Your Specifications",
                  "2. Edit",
                  "3. Change Password",
                  "4. Create Bank Account",
                  "5. Show Bank Accounts",
                  "6. Show Wallet",
                  "7. Charge Wallet",
                  "8. Show Movies",
                  "9. Show my Movies",
                  "10. Show my subscription_type",
                  "11. Buy_movie",
                  "12. Exit",
                  sep="\n")
            print("-" * 30)
            choice = input(">>> ")
            match choice:
                case "1":
                    show_users_info()
                case "2":
                    edit_user_and_phone_number(name)
                case "3":
                    change_password(name)
                case "4":
                    create_bank_account()
                case "5":
                    show_bank_account()
                case "6":
                    show_wallet()
                case "7":
                    charge_wallet()
                case "8":
                    show_movies()
                case "9":
                    show_my_movies()
                case "10":
                    show_my_subscription_type()
                case "11":
                    buy_movie()
                case "12":
                    return


        else:
            print("Wrong Password!!!")
    else:
        print("Invalid Name")


def show_movies():
    """Mahsa"""
    pass


def creat_movie():
    """Hesel"""
    pass


def login_manager():
    manager_name = input("Enter your Name : ")
    if not Manager.is_manger(manager_name):
        print("Invalid manager name")
        return
    password = input("Enter Password : ")
    if Manager.check_password(manager_name, password):
        print("-" * 30, "|\t  >>> Manager Menu <<<   |", "-" * 30, sep="\n")
        print("Please select an option:",
              "1. Show Movies",
              "2. Create Movie",
              "3. Exit",
              sep="\n")
        print("-" * 30)
        choice = input(">>> ")
        match choice:
            case "1":
                show_movies()
            case "2":
                creat_movie()
            case "3":
                return
    else:
        print("Wrong Password!!!")


def main():
    """
    This function is the main function of the program used to display
    the main menu to the user for registering or editing user information.
    """
    while True:
        print("-" * 30, "|\t  >>> Main Menu <<<   \t |", "-" * 30, sep="\n")
        print("Please select an option:",
              "0. Exit",
              "1. Register",
              "2. Login User",
              "3. Login Manager",
              sep="\n")

        choice = input(">>> ")
        match choice:
            case "0":
                break
            case "1":
                register()
                continue
            case "2":
                login()
                continue
            case "3":
                login_manager()
                continue


if __name__ == "__main__":
    main()
