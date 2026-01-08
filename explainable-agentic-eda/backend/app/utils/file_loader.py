from pathlib import Path
import pandas as pd
import chardet

DATASET_DIR = Path("datasets")

def load_dataset(dataset_id: str):
    files = list(DATASET_DIR.glob(f"{dataset_id}_*"))
    if not files:
        raise FileNotFoundError("Dataset not found")

    file_path = files[0]

    # Excel support
    if file_path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)

    # Detect encoding for CSV
    with open(file_path, "rb") as f:
        raw = f.read(100_000)
        encoding = chardet.detect(raw)["encoding"] or "utf-8"

    try:
        return pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        raise ValueError(
            f"Failed to load dataset {file_path.name}: {str(e)}"
        )
