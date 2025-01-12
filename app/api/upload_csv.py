from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from fastapi.security import OAuth2PasswordBearer
from typing import Any
from app.auth.verify_token import verify_token
from app.api.parse_csv import parse_csv
import jwt

# Define the OAuth2 scheme for token extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a router for the API
router = APIRouter()

@router.post("/upload-csv", status_code=status.HTTP_200_OK)
async def upload_csv(
    token: str = Depends(oauth2_scheme),
    file: UploadFile = File(...)
) -> Any:
    """
    Upload a CSV file, verify the JWT token, and parse the CSV.

    - **token**: JWT token for authentication.
    - **file**: CSV file to be uploaded and processed.
    """
    try:
        # Verify the JWT token
        verify_token(token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Pass the file to the CSV parser function
    await parse_csv(file.file)

    return {"message": "CSV file processed successfully"}
