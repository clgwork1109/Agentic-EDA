# Upload endpoint placeholder
# `datasets.py` – endpoint to upload datasets
import uuid
import shutil
from pathlib import Path
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

DATASET_DIR = Path("datasets")
DATASET_DIR.mkdir(exist_ok=True)

@router.post("/datasets")
def upload_dataset(file: UploadFile = File(...)):
    dataset_id = f"ds_{uuid.uuid4().hex[:8]}"
    file_path = DATASET_DIR / f"{dataset_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "dataset_id": dataset_id,
        "filename": file.filename,
        "status": "uploaded"
    }
