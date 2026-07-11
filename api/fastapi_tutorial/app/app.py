from fastapi import FastAPI,HTTPException

app= FastAPI()

@app.get("/hello_world")
def hello_world():
    return {"message":"hello world!!!"}  #json---> javascript object notation or a dictionary(generally)

text_post={
    1: {"title":"first post","content":"this is the test first post"},
    2: {"title": "morning thoughts", "content": "coffee first, code later"},
    3: {"title": "fastapi tips", "content": "always validate input with pydantic models"},
    4: {"title": "weekend plans", "content": "planning a drive to gulmarg this saturday"},
    5: {"title": "gym log", "content": "hit a new PR on deadlifts today"},
    6: {"title": "book review", "content": "a philosophy of software design is worth a reread"},
    7: {"title": "car care", "content": "changed the civic's engine oil after 8000 km"},
    8: {"title": "learning update", "content": "practiced writing python without any ai help"},
    9: {"title": "random idea", "content": "what if notes apps had built-in spaced repetition"},
    10: {"title": "last post", "content": "wrapping up the test data for the notes api"},
    }

@app.get("/posts")
def get_all_posts(limit: int=None):
    if limit:
        return list(text_post.values())[:limit]
    return text_post

@app.get("/get_post_from_id/{id}")
def get_post_by_id(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="post not found")
    return text_post.get(id)
def apple(number:int):
    print(number)
apple("o")