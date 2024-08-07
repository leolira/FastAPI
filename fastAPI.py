from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

def id_generator():
    return max(user.id for user in users)+1

class User(BaseModel):
    id: int = Field(default_factory=id_generator)
    name: str
    lastname: str
    age: int


users = [
    User(id=1, name="Leonardo", lastname="Amorim", age=42),
    User(id=2, name="Luana", lastname="Menezes", age=35)
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

#create user route
@app.post("/users")
async def create_user(user: User):
    user.id = id_generator()
    users.append(user)
    return {"message":"User successfully created!"}



