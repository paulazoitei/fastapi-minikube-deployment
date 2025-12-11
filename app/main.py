
from fastapi import FastAPI
from app.routers.home_router import router as home_router
from app.routers.item_router import router as item_router
from app.routers.random_router import router as random_router
tags_metadata=[
    {
        "name":"Random Playground",
        "description":"Generate random numbers",
    },
    {
        "name":"Random Items Management",
        "description":"Create, shuffle, read, update and delete items",
    },
]
app=FastAPI(
    title="Randomizer API",
    description="Shuffle lists, pick random items, and generate random numbers.",
    version="1.0.0",
    openapi_tags=tags_metadata,
)



app.include_router(home_router)
app.include_router(item_router)
app.include_router(random_router)
