from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.local_items import router as item_router
from app.database_items import router as database_item_router

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can specify specific origins
    allow_credentials=True,
    allow_methods=["*"],    # Allow all HTTP methods
    allow_headers=["*"],    # Allow all HTTP headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}


# Include the item_router in the main FastAPI app
app.include_router(item_router)
app.include_router(database_item_router)
