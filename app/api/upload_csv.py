from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.api.parse_csv import parse_csv

router = APIRouter()

@router.post("/upload-csv", response_class=JSONResponse, summary="Upload a CSV file")
async def upload_csv(file: UploadFile = File(...)) -> JSONResponse:
    """
    Endpoint to upload a CSV file and process it.

    - **file**: CSV file to be uploaded and processed.
    """
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    try:
        # Pass the file to the CSV parser function
        parse_csv(file.file)
        return JSONResponse(content={"message": "CSV file processed successfully."}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
