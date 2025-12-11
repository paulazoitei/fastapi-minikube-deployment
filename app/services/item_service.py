
import random
from app.schemas.item import Item

items_db = ["random_number"]
class ItemAlreadyExists(Exception):
    pass

class ItemNotFound(Exception):
    pass

class ItemService:
    @staticmethod
    def add_item(name:str)->None:
        if name in items_db:
            raise ItemAlreadyExists()
        items_db.append(name)
    @staticmethod
    def get_items() -> list[str]:
        return list(items_db)
    @staticmethod
    def get_randomized_items()->list[str]:
        randomized=items_db.copy()
        random.shuffle(randomized)
        return randomized
    
    @staticmethod
    def update_item(update_item_name:str,item:Item):
        if update_item_name not in items_db:
            raise ItemNotFound()
        if item.name in items_db and item.name != update_item_name:
            raise ItemAlreadyExists()
        index=items_db.index(update_item_name)
        items_db[index]=item.name

    @staticmethod
    def delete_item(item:str):
        if item not in items_db:
            raise ItemNotFound()
        items_db.remove(item)