from fastapi import FastAPI

app = FastAPI()

food_items = {
    'indian': ["samosa", "dosa"],
    'american': ["hot dog", "apple pie"],
    'italian': ["ravioli", "pizza"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: str):
    return {"items": food_items.get(cuisine.lower(), ["Not found"])}
