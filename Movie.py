from uuid import uuid4 
from datetime import datetime
import json
from user import User
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


    @classmethod
    def create_movie(cls,id_manager, movie_name: str, scr_date: datetime, seats_capacity: int, price: float, age_group: int):
        new_movie = cls(id_manager, movie_name, scr_date, seats_capacity, price, age_group)
        cls.movies_dict[new_movie.id_movie] = new_movie
        
        # storing in json file   
        with open('movies_dict.json', 'w+') as f:
            json.dump(cls.movies_dict, f)
    
#   ********************************************************************************
    @staticmethod
    def show_movies(): 
        with open('movies_dict.json', 'r') as f:
            movies = json.load(f)
        for movie in movies:
            print(movie)  
#   ********************************************************************************
    @staticmethod
    def show_my_movies(user): 
  

#   ********************************************************************************
    def buy_movie(self, id_user):
        

        
#   ******************************************************************************** 
    
    def apply_discount():
        
        month_passed = self.NOW.month - user.register_date.month
        self.price = (1 - month_passed) * self.price 
        
        if user.birth_date.month == self.NOW.month and user.birth_date.day == self.NOW.day:
            self.price /= 2
            
        return self.price
    
#   *********************************************************************************
    
    def check_time():
        
     
            
#   *********************************************************************************           
       
    def check_capacity():
        
#   *********************************************************************************
    @classmethod   
    def check_age():
    
        
               
    