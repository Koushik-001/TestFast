from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.blog import root

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Adjust this for production.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods.
    allow_headers=["*"],  # Allows all headers.
)

# Include your router
app.include_router(root)
