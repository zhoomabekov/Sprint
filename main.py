from typing import List

from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id="97099d4d-65ba-4f6b-ad90-4a262fdbb4cc",
        first_name="Jamila",
        last_name="Akhmed",
        middle_name="",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id="1640af8d-44c3-4dd1-af08-997ed65a97a3",
        first_name="Alex",
        last_name="Jones",
        middle_name="",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}