import jwt
from jwt import PyJWTError
from typing import Dict, Any

# Secret key used for encoding and decoding the JWT token
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def verify_token(token: str) -> Dict[str, Any]:
    """
    Verifies the provided JWT token and checks for expiration and validity.

    :param token: The JWT token to verify.
    :return: The decoded token data if the token is valid.
    :raises jwt.ExpiredSignatureError: If the token has expired.
    :raises jwt.InvalidTokenError: If the token is invalid.
    """
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError as e:
        # Let the error raise for invalid or expired tokens
        raise e
