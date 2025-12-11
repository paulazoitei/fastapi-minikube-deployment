from fastapi import APIRouter,Query,HTTPException
from services.item_service import Item_Service,ItemAlreadyExists
from schemas.item import ItemResponse,Item,ItemListResponse,ItemDeleteResponse,ItemUpdateResponse
from main import items_db
router=APIRouter(
    prefix="/items",
    tags=["Random Items Management"],
)

@router.post("/",response_model=ItemResponse)
async def add_item_endpoint(item:Item):
    if item.name in items_db:
        raise HTTPException(status_code=400,detail ="Item already exists")
    try:
        Item_Service.add_item(item.name)
    except ItemAlreadyExists:
        raise HTTPException(status_code=400,detail="Item already exists")

    return ItemResponse(
        message="Item added successfully",
        item=item.name
    )

@router.get("/",response_model=ItemListResponse)
async def get_randomized_items_endpoint():
    
    
    return ItemListResponse(
        original_order=items_db,
        randomized_order=Item_Service.get_randomized_items(),
        count=len(items_db)
    )

@router.put("/{update_item_name}",response_model=ItemUpdateResponse)
async def update_item(update_item_name:str, item:Item):
    if update_item_name not in items_db:
        raise HTTPException(status_code=404,detail="Item not found")
    
   
    if item.name in items_db:
        raise HTTPException(
            status_code=409,
            detail="An item with that name already exists"
        )
    
    Item_Service.update_item(update_item_name,item)

    return ItemUpdateResponse(
        message="Item updated successfully",
        old_item=update_item_name,
        new_item=item.name
    )
    