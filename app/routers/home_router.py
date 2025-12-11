from fastapi import APIRouter


router=APIRouter(
    
    tags=["Random Playground"],
)

@router.get("/")
async def home():
    return {"message":"Welcome to the Randomizer API"}