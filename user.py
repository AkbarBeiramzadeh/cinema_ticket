class User:
    users_dict = {}

    def __init__(self,name,password,birth_date,register_date,wallet,subscription,phone_number=None):
        self.name = name
        self.password = password
        self.birth_date = birth_date
        self.register_date = register_date
        self.wallet = wallet
        self.subscription = subscription
        self.phone_number = phone_number
