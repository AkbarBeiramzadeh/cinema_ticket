from uuid import uuid4 
from datetime import datetime
import json
from user import User

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
    
class Movie:
    
    movies_dict = {}
    NOW = datetime.now()
    
    def __init__(self, id_manager, name: str, scr_date: datetime, seats_capacity: int, price: float, age_group: int) -> None:
        
        self.id_manager = id_manager
        self.name = name
        self.scr_date = scr_date
        self.seats_capacity = seats_capacity
        self.price = price
        self.age_group = age_group
        self.id_movie = uuid4().hex

#   *********************************************************************************

    @classmethod
    def create_movie(cls,id_manager, movie_name: str, scr_date: datetime, seats_capacity: int, price: float, age_group: int):
    
        cls.movies_dict[movie_name] = {
            "id_movie": uuid4().hex,
            "id_manager": id_manager,
            "scr_date": scr_date,
            "seats_capacity": seats_capacity,
            "price": price,
            "age_group": age_group}
            
        # storing to the json file
        with open('movies_dict.json', 'w+') as f:
            json.dump(cls.movies_dict, f,cls=DateTimeEncoder)

    
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
            raise Exception("all tickets have been sold")
        if cls.check_time == False :
            raise Exception("screening time has passed")
        if cls.check_age(user,movie) == False:
            raise Exception("this movie isn't appropriate for you")
        
        
        price = cls.apply_discount
        user["wallet"] -= price
        with open('users_json.json', 'w') as f1:
            json.dump(user_json, f1)
            
        movie["seats_capacity"] -= 1
        with open('movies_dict.json', 'w') as f2:
            json.dump(movies, f2)   
               
#   ********************************************************************************
#     @staticmethod
#     def show_my_movies(user): 
  

 #   ********************************************************************************
    # @staticmethod
    # def show_movies(user): 
    #     pass

        
#   ******************************************************************************** 
    @staticmethod
    def apply_discount(movie,user):
        
        NOW = datetime.now()
        ry,rm,rd = user["register_date"].split("-")
        by,bm,bd = user["register_date"].split("-")
        
        month_passed = NOW.month - rm
        if bm == NOW.month and bd == NOW.day:
            price = movie["price"]/2
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
    def check_age(user,movie):
        
        NOW = datetime.now()
        by,m,d = user["birth_date"].split("-")
        age = NOW.year - by
        
        if age < movie["age_group"]:
            return False
        return True
    
        
               
    