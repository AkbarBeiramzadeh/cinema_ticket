import json
import os
from user import User
from manager import Manager
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
                  "8. Show Cinema Sans",
                  "9. Show my Cinema Sans",
                  "10. Show my Cinema Ticket's info",
                  "11. Buy Cinema Ticket",
                  "12. Exit",
                  sep="\n")
            print("-" * 30)
            choice = input(">>> ")
        else:
            print("Wrong Password!!!")

    else:
        print("Invalid Name")


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
                pass
            case "2":
                pass
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
