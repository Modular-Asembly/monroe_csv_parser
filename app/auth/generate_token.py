import jwt
from datetime import datetime, timedelta
from typing import Dict, Any

def generate_token(user_id: str, secret_key: str, expires_in: int = 3600) -> str:
    """
    Generates a JWT token for a given user.

    :param user_id: The identifier for the user.
    :param secret_key: The secret key used to encode the JWT.
    :param expires_in: The expiration time in seconds for the token. Default is 3600 seconds (1 hour).
    :return: A JWT token as a string.
    """
    expiration = datetime.utcnow() + timedelta(seconds=expires_in)
    payload: Dict[str, Any] = {
        "sub": user_id,
        "exp": int(expiration.timestamp())  # Convert datetime to Unix timestamp
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token
