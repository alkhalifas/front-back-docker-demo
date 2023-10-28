from fastapi import APIRouter, HTTPException, Body
import datetime
import redis
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Connect to Redis database
redis_client = redis.Redis(host='redis', port=6379, db=0)

# Example data structure for storing questions
questions = []


class QuestionResponse(BaseModel):
    id: int
    title: str
    text: str
    author: str
    date: str
    views: int

class QuestionCreate(BaseModel):
    title: str
    text: str
    author: str

class QuestionUpdate(BaseModel):
    title: str
    text: str
    author: str
    views: int

class Question:
    def __init__(self, id: int, title: str, text: str, author: str):
        self.id = id
        self.title = title
        self.text = text
        self.author = author
        self.date = datetime.datetime.now()
        self.views = 0

@router.post("/questions/", response_model=QuestionResponse)
async def create_question(question: QuestionCreate = Body(...)) -> QuestionResponse:
    question_id = len(redis_client.keys("question:*")) + 1
    redis_key = f"question:{question_id}"
    question_data = {
        "id": question_id,
        "title": question.title,
        "text": question.text,
        "author": question.author,
        "date": str(datetime.datetime.now()),
        "views": 0
    }
    redis_client.hmset(redis_key, question_data)
    return QuestionResponse(**question_data)


@router.get("/questions/", response_model=List[QuestionResponse])
async def get_questions() -> List[QuestionResponse]:
    # Retrieve questions from Redis (example)
    redis_keys = redis_client.keys("question:*")
    question_list = []
    for key in redis_keys:
        question_data = redis_client.hgetall(key)
        question = QuestionResponse(
            id=int(question_data[b'id']),
            title=question_data[b'title'].decode('utf-8'),
            text=question_data[b'text'].decode('utf-8'),
            author=question_data[b'author'].decode('utf-8'),
            date=question_data[b'date'].decode('utf-8'),
            views=int(question_data[b'views'])
        )
        question_list.append(question)
    return question_list

@router.get("/questions/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int) -> QuestionResponse:
    redis_key = f"question:{question_id}"
    question_data = redis_client.hgetall(redis_key)
    if not question_data:
        raise HTTPException(status_code=404, detail="Question not found")

    return QuestionResponse(
        id=int(question_data[b'id']),
        title=question_data[b'title'].decode('utf-8'),
        text=question_data[b'text'].decode('utf-8'),
        author=question_data[b'author'].decode('utf-8'),
        date=question_data[b'date'].decode('utf-8'),
        views=int(question_data[b'views'])
    )

@router.put("/questions/{question_id}", response_model=QuestionResponse)
async def update_question(question_id: int, question_update: QuestionUpdate = Body(...)) -> QuestionResponse:
    redis_key = f"question:{question_id}"
    if not redis_client.exists(redis_key):
        raise HTTPException(status_code=404, detail="Question not found")

    # Update question data in Redis
    redis_client.hmset(redis_key, {
        "id": question_id,
        "title": question_update.title,
        "text": question_update.text,
        "author": question_update.author,
        "date": str(datetime.datetime.now()),
        "views": question_update.views
    })

    # Retrieve updated question data from Redis
    updated_question_data = redis_client.hgetall(redis_key)
    updated_question_response = QuestionResponse(
        id=int(updated_question_data[b'id']),
        title=updated_question_data[b'title'].decode('utf-8'),
        text=updated_question_data[b'text'].decode('utf-8'),
        author=updated_question_data[b'author'].decode('utf-8'),
        date=updated_question_data[b'date'].decode('utf-8'),
        views=int(updated_question_data[b'views'])
    )

    return updated_question_response

@router.delete("/questions/{question_id}", response_model=QuestionResponse)
async def delete_question(question_id: int) -> QuestionResponse:
    redis_key = f"question:{question_id}"
    question_data = redis_client.hgetall(redis_key)
    if not question_data:
        raise HTTPException(status_code=404, detail="Question not found")

    # Delete question from Redis
    redis_client.delete(redis_key)

    # Construct response with deleted question data
    deleted_question_response = QuestionResponse(
        id=int(question_data[b'id']),
        title=question_data[b'title'].decode('utf-8'),
        text=question_data[b'text'].decode('utf-8'),
        author=question_data[b'author'].decode('utf-8'),
        date=question_data[b'date'].decode('utf-8'),
        views=int(question_data[b'views'])
    )

    return deleted_question_response