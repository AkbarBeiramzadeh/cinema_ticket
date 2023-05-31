import json
import os
from user import User
from manager import Manager
import getpass
import sys
from datetime import datetime
from BankAccount import BankAccount
from Movie import Movie


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


def show_users_info(name):
    """Mahsa"""
    with open("users_json.json", "r") as f:
        user_json = json.load(f)

    id_user = user_json[name]["id_user"]
    User.show_info(id_user)  # undefined method


def edit_user(name):
    """Hesel"""
    new_name = input("Enter Your New Name :")
    new_phone_number = input("Enter Your New Phone Number :")
    if new_phone_number == "":

        new_phone_number = None

    User.change_username_and_phone_number(name, new_name, new_phone_number)


def create_bank_account(name):
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


def show_bank_account(name):
    """Shows list of user's bank accounts"""

    with open("users_json.json", "r") as f:
        user_json = json.load(f)

    id_user = user_json[name]["id_user"]
    BankAccount.show_bank_account(id_user)


def show_wallet(name: str):
    """Akbar"""
    print(User.show_wallet(name))


def charge_wallet(name):
    """subs from balance and adds to wallet"""
    amount = input("How much do you wanna charge your wallet? ")
    show_bank_account(name)
    id_bank_account = input("Enter one of id_bank_accounts_for_charge_wallet: ")
    bank_password = input("Enter bank_password: ")
    cvv2 = input("Entr cvv2:")
    with open("users_json.json", "r") as f:
        user_json = json.load(f)
    id_user = user_json[name]["id_user"]
    with open("users_json.json", "r") as f2:
        users = json.load(f2)
        if users[name] == name:
            wallet = users[name]["wallet"]
            new_wallet = BankAccount.transfer(wallet, id_user, id_bank_account, bank_password, cvv2, amount)
            users[name]["wallet"] = new_wallet
            users_string = json.dumps(users)
            f2.write(users_string)


def show_my_movies(name):
    """Hesel"""
    with open("users_json.json", "r") as f:
        user_json = json.load(f)
    id_user = user_json[name]["id_user"]
    Movie.show_my_movies(id_user)


def show_my_subscription_type(name):
    """Akbar"""
    print(User.show_subscription_type(name))


def buy_movie(name):
    """Akbar"""
    show_movies()
    print("Enter the name of the movie you want ")
    film_name = input("film_name : ")
    Movie.buy_movie(name, film_name)


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
                    show_users_info(name)
                case "2":
                    edit_user(name)
                case "3":
                    change_password(name)
                case "4":
                    create_bank_account(name)
                case "5":
                    show_bank_account(name)
                case "6":
                    show_wallet(name)
                case "7":
                    charge_wallet(name)
                case "8":
                    show_movies()
                case "9":
                    show_my_movies(name)
                case "10":
                    show_my_subscription_type(name)
                case "11":
                    buy_movie(name)
                case "12":
                    return


        else:
            print("Wrong Password!!!")
    else:
        print("Invalid Name")


def show_movies():
    """Shows list of available movies"""
    Movie.show_movies()


def creat_movie(manager_name):
    """Hesel"""
    with open("manager.json", "r") as f:
        manager_informations_json = json.load(f)
    id_manager = manager_informations_json[manager_name]["id_manager"]
    movie_name = input("Enter movie_name: ")
    scr_date = datetime.strptime(
        input("Enter Screening_datetime with 'yyyy-mm-dd  hh:mm:ss' format: "), '%Y-%m-%d %H:%M:%S'
    )
    seats_capacity = int(input("Enter seats_capacity: "))
    price = float(input("Enter price of movie: "))
    age_group = int(input("Enter age_group limitation for the movie: "))
    Movie.create_movie(id_manager, movie_name, scr_date, seats_capacity, price, age_group)


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
                creat_movie(manager_name)
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
