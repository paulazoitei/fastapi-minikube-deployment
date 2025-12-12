from fastapi import APIRouter,Query,HTTPException
from app.services.item_service import ItemService,ItemAlreadyExists,ItemNotFound
from app.schemas.item import ItemResponse,Item,ItemListResponse,ItemDeleteResponse,ItemUpdateResponse
from app.services.item_service import items_db

router=APIRouter(
    prefix="/items",
    tags=["Random Items Management"],
)

@router.post("/",response_model=ItemResponse)
async def add_item_endpoint(item:Item):
    try:
        ItemService.add_item(item.name)
    except ItemAlreadyExists:
        raise HTTPException(status_code=400,detail="Item already exists")

    return ItemResponse(
        message="Item added successfully",
        item=item.name
    )

@router.get("/",response_model=ItemListResponse)
async def get_randomized_items_endpoint():
    items = ItemService.get_items()
    
    return ItemListResponse(
        original_order=items,
        randomized_order=ItemService.get_randomized_items(),
        count=len(items_db)
    )


@router.put("/{update_item_name}", response_model=ItemUpdateResponse)
async def update_item_endpoint(update_item_name: str, item: Item):
    try:
        ItemService.update_item(update_item_name, item)
    except ItemNotFound:
        raise HTTPException(status_code=404, detail="Item not found")
    except ItemAlreadyExists:
        raise HTTPException(
            status_code=409,
            detail="An item with that name already exists",
        )

    return ItemUpdateResponse(
        message="Item updated successfully",
        old_item=update_item_name,
        new_item=item.name,
    )
    

@router.delete("/{item}", response_model=ItemDeleteResponse)
async def delete_item_endpoint(item: str):
    try:
        ItemService.delete_item(item)
    except ItemNotFound:
        raise HTTPException(status_code=404, detail="Item not found")

    items = ItemService.get_items()

    return ItemDeleteResponse(
        message="Item deleted successfully",
        deleted_item=item,
        remaining_items_count=len(items),
    )