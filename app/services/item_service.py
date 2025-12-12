import logging
import random
from app.schemas.item import Item

logger=logging.getLogger(__name__)

items_db = ["random_number"]
class ItemAlreadyExists(Exception):
    pass

class ItemNotFound(Exception):
    pass

class ItemService:
    
    @staticmethod
    def add_item(name: str) -> None:
        if name in items_db:
            logger.warning("Attempted to add existing item: %s", name)
            raise ItemAlreadyExists()

        items_db.append(name)
        logger.info("Item added: %s", name)

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
            logger.warning("Attempted update on non-existent item: %s", update_item_name)
            raise ItemNotFound()
        
        if item.name in items_db and item.name != update_item_name:
            logger.warning("Name conflict while updating '%s' to '%s'", update_item_name, item)
            raise ItemAlreadyExists()
        index=items_db.index(update_item_name)
        items_db[index]=item.name
        

    @staticmethod
    def delete_item(item:str):
        if item not in items_db:
            logger.warning("Attempted delete of non-existent item: %s", item)
            raise ItemNotFound()
        items_db.remove(item)