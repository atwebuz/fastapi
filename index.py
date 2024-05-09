from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origns=['*'],
    allow_credentials=['*'],
    allow_methods=['*'],
    allow_headers=['*'],

)
app.include_router(user)