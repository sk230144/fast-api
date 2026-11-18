from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {"id": 1, "name": "Amit Sharma", "email": "amit@example.com", "age": 28, "city": "Delhi"},
    {"id": 2, "name": "Priya Singh", "email": "priya@example.com", "age": 24, "city": "Mumbai"},
    {"id": 3, "name": "Rahul Verma", "email": "rahul@example.com", "age": 31, "city": "Bangalore"},
    {"id": 4, "name": "Sneha Patel", "email": "sneha@example.com", "age": 27, "city": "Ahmedabad"},
    {"id": 5, "name": "Vikram Rao", "email": "vikram@example.com", "age": 35, "city": "Hyderabad"},
]

@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) 
def home():
    return f"<h1>{posts[0]['name']}</h1>"


@app.get("/api/posts")
def get_posts():
    return {"data": posts}