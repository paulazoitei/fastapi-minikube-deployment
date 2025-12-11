import random
from typing import Annotated
from fastapi import Query,HTTPException

def generate_random_number(max_value:int)-> int:
    return random.randint(1,max_value)

def generate_random_between(min_value: int, max_value: int) -> int:
    if min_value > max_value:
        
        raise ValueError("min_value can't be greater than max_value")
    return random.randint(min_value, max_value)