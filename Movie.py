from uuid import uuid4
from datetime import datetime
import json
from user import User
import logging

logging.basicConfig(level=logging.INFO, filename="cinematicket.log",
                    format="%(asctime)s - %(levelname)s - %(lineno)d - %(msg)s")
logger = logging.getLogger("Movie")

file_handler = logging.FileHandler("cinematicket.log")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
pattern = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(msg)s")
console_handler.setFormatter(pattern)
file_handler.setFormatter(pattern)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class Movie:
    
    movies_dict = {}
    NOW = datetime.now()

    def __init__(self, id_manager, name: str, scr_date: datetime, seats_capacity: int, price: float,
                 age_group: int) -> None:

        self.id_manager = id_manager
        self.name = name
        self.scr_date = scr_date
        self.seats_capacity = seats_capacity
        self.price = price
        self.age_group = age_group
        self.id_movie = uuid4().hex

#   *********************************************************************************

    #   *********************************************************************************

    @classmethod
    def create_movie(cls, id_manager, movie_name: str, scr_date: datetime, seats_capacity: int, price: float,
                     age_group: int):
        cls.movies_dict[movie_name] = {
            "id_movie": uuid4().hex,
            "id_manager": id_manager,
            "scr_date": scr_date,
            "seats_capacity": seats_capacity,
            "price": price,
            "age_group": age_group}

        # storing to the json file
        with open('movies_dict.json', 'w+') as f:
            json.dump(cls.movies_dict, f, cls=DateTimeEncoder)

    #   ********************************************************************************
    @classmethod
    def buy_movie(cls, name, movie_name):
        with open("users_json.json", "r") as f1:
            user_json = json.load(f1)
            user = user_json[name]
        with open("movies_dict.json", "r") as f2:
            movies = json.load(f2)
            movie = movies[movie_name]
        if cls.check_capacity(movie) == False:
            logger.error("Sold out")
            raise Exception("all tickets have been sold")
        if cls.check_time == False:
            logger.error("passed time")
            raise Exception("screening time has passed")
        if cls.check_age(user, movie) == False:
            logger.error("not appropriate")
            raise Exception("this movie isn't appropriate for you")

        price = cls.apply_discount(movie, user)
        user["wallet"] -= price
        user_json[name] = user
        with open('users_json.json', 'w') as f1:
            json.dump(user_json, f1)

        movie["seats_capacity"] -= 1
        movies[movie_name] = movie
        with open('movies_dict.json', 'w') as f2:
            json.dump(movies, f2)

            # adding movie to users movies list
        with open("users_json.json", "r") as f3:
            my_dict = json.load(f3)
            list_movies = my_dict[name]
            list_movies.append(movie_name)
            my_dict[name] = list_movies
        with open('users_movies.json', 'w') as f3:
            json.dump(my_dict, f3)
        #   ********************************************************************************

    @staticmethod
    def show_my_movies(name):
        with open("users_movies.json", "r") as f2:
            users_movies = json.load(f2)
        for each in users_movies:
            if each == name:
                print(users_movies[each])
                #   ********************************************************************************

    @staticmethod
    def show_movies():
        with open("movies_dict.json", "r") as f2:
            movies = json.load(f2)
        print("ON SCREEN MOVIES:")
        for movie in movies:
            print(movie)

    #   ********************************************************************************
    @staticmethod
    def apply_discount(movie, user):

        NOW = datetime.now()
        ry, rm, rd = user["register_date"].split("-")
        by, bm, bd = user["register_date"].split("-")

        month_passed = NOW.month - int(rm)
        if int(bm) == NOW.month and int(bd) == NOW.day:
            price = movie["price"] / 2
            return price

        price = (1 - month_passed) * movie["price"]
        return price 

    #   *********************************************************************************
    @staticmethod
    def check_time(movie):
        NOW = datetime.now()
        if NOW > movie["scr_date"]:
            return False
        return True

    #   *********************************************************************************
    @staticmethod
    def check_capacity(movie):

        if movie["seats_capacity"] > 0:
            return True
        return False

    #   *********************************************************************************
    @staticmethod
    def check_age(user, movie):

        NOW = datetime.now()
        by, m, d = user["birth_date"].split("-")
        age = NOW.year - int(by)

        if age < movie["age_group"]:
            return False
        return True
