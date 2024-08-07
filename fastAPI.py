from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Users(BaseModel):
    id: int
    name: str
    lastname: str
    age: int

def id_generator():
    return max(user['id'] for user in users)+1

users = [
    Users(id=1, name="Leonardo", lastname="Amorim", age=42),
    Users(id=2, name="Luana", lastname="Menezes", age=35)
]

#list all users route
@app.get("/users")
async def list_users():
    return users

#show a user by id route
@app.get("/users/{user_id}")
async def get_user_byid(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

