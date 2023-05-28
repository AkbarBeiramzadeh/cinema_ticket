def register():
    pass


def login():
    pass


def login_manager():
    pass


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