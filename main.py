import json
import os
from user import User
import getpass
import sys
from datetime import datetime


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


def login():
    pass


def manager_menu():
    print("Manager Menu")


def login_manager():
    if os.path.exists("manager.json"):
        with open("manager.json", "r") as f:
            manager_dict = json.load(f)
        manager_name = input("Enter your Name:")
        if manager_name not in manager_dict.keys():
            print("Your Name is not in Manager list!!!")
            return
        password = input("Enter Password : ")
        if password == manager_dict[manager_name]:
            manager_menu()
        else:
            print("Wrong Password!!!")
    else:
        print("There is no Manager!!!")


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
