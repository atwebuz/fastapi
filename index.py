from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow requests from any origin
    allow_credentials=True,  # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=['*'],  # Allow all HTTP methods
    allow_headers=['*'],  # Allow all HTTP headers
)

# Include your router
app.include_router(user)


# from fastapi import FastAPI
# from routes.user import user
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=['*'],
# #     allow_credentials=['*'],
# #     allow_methods=['*'],
# #     allow_headers=['*'],

# # )
# app.include_router(user)