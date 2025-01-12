from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any
from app.auth.generate_token import generate_token

# Create a router for the API
router = APIRouter()

# Pydantic model for input
class LoginRequest(BaseModel):
    username: str
    password: str

# Pydantic model for output
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# Dummy function to validate user credentials
def validate_user(username: str, password: str) -> bool:
    # Replace with actual validation logic
    return username == "testuser" and password == "testpass"

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest) -> Any:
    """
    Accepts user credentials, validates them, and generates a JWT token.

    :param credentials: The user credentials for login.
    :return: A JWT token if the credentials are valid.
    :raises HTTPException: If the credentials are invalid.
    """
    if not validate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT token
    secret_key = "your_secret_key"  # Replace with your actual secret key
    token = generate_token(user_id=credentials.username, secret_key=secret_key)

    return TokenResponse(access_token=token, token_type="bearer")
