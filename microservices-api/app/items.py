from fastapi import APIRouter

router = APIRouter()

# Sample data
items = [
    {"item_id": 1, "name": "Item 1"},
    {"item_id": 2, "name": "Item 2"}
]

@router.get("/items/")
def get_items():
    return items

@router.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["item_id"] == item_id:
            return item
    return {"error": "Item not found"}

