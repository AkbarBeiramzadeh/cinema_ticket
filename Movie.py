from uuid import uuid4 
from datetime import datetime
import json
# from users import User
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
    def create_movie(cls,id_manager, name: str, scr_date: datetime, seats_capacity: int, price: float, age_group: int):
        new_movie = cls(id_manager, name, scr_date, seats_capacity, price, age_group)
        cls.movies_dict[new_movie.id_movie] = new_movie
        
        # storing in json file (??)
        # json_string = json.dumps(Movie.movies_dict)
        # with open("movies_dict.json", "w") as f:
        #     f.write(json_string)    
        with open('movies_dict.json', 'w') as f:
            json.dump(cls.movies_dict, f)
    
#   ********************************************************************************
    @staticmethod
    def show_movies(): 
        with open('movies.json', 'r') as f:
            movies = json.load(f)
        for movie in movies:
            print(movie)  
#   ********************************************************************************
    def buy_movie(self):
        
        if self.seats_capacity > 0:
            self.seats_capacity -= 1
        else:
            self.seats_capacity = 0
        
#   ******************************************************************************** 
    
    def apply_discount(self, user):
        
        month_passed = self.NOW.month - user.register_date.month
        self.price = (1 - month_passed) * self.price 
        
        if user.birth_date.month == self.NOW.month and user.birth_date.day == self.NOW.day:
            self.price /= 2
            
        return self.price
    
#   *********************************************************************************
    
    def check_time(self):
        
        if self.NOW > self.scr_date:
            print("screening date has passed!")
            
#   *********************************************************************************           
       
    def check_capacity(self):
        
        if self.seats_capacity == 0:
            print("all tickets have been sold!")
            
        return True
        
#   *********************************************************************************
    @classmethod   
    def check_age(cls,user):
        
        age = cls.NOW.year - user.birth_date.year
        if age < cls.age_group:
            print("This movie isn't appropriate for you")
        
               
    