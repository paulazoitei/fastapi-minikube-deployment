from  main import items_db
import random
from schemas.item import Item

class ItemAlreadyExists(Exception):
    pass


class Item_Service:
    @staticmethod
    def add_item(name:str)->None:
        if name in items_db:
            raise ItemAlreadyExists()
        items_db.append(name)
    @staticmethod
    def get_randomized_items():
        randomized=items_db.copy()
        random.shuffle(randomized)
        return randomized
    @staticmethod
    def update_item_(update_item_name:str,item:Item):
        index=items_db.index(update_item_name)
        items_db[index]=item.name