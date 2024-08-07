from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(__name__)

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

@app.get("/users")
async def list_users():
    return users

if __name__ == "__main__":
    app.run(debug=True)