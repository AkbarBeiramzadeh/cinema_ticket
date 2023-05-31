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

               
    