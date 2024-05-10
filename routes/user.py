from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get('/')
async def fetch_users():
    # Return all users
    return conn.execute(users.select()).fetchall()

@user.post('/create')
async def create_user(user: User):
    # Insert a new user
    return conn.execute(users.insert().values(name=user.name, email=user.email, password=user.password))

@user.put('/{id}')
async def update_user(id: int, user: User):
    # Update an existing user by ID
    return conn.execute(users.update().values(name=user.name, email=user.email, password=user.password).where(users.c.id == id))

@user.delete('/{id}')
async def delete_user(id: int):
    # Delete a user by ID
    return conn.execute(users.delete().where(users.c.id == id))

