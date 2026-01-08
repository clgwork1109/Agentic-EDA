import uuid
from fastapi import APIRouter
from app.agents.orchestrator import run_eda_pipeline
from app.utils.json_sanitizer import sanitize_for_json

router = APIRouter()

EDA_JOBS = {}


@router.post("/eda/run")
def run_eda(dataset_id: str):
    job_id = f"job_{uuid.uuid4().hex[:8]}"

    result = run_eda_pipeline(dataset_id)

    # ✅ sanitize BEFORE storing
    safe_result = sanitize_for_json(result)

    EDA_JOBS[job_id] = {
        "status": "completed",
        "result": safe_result
    }

    return {
        "job_id": job_id,
        "status": "completed"
    }


@router.get("/eda/results/{job_id}")
def get_results(job_id: str):
    job = EDA_JOBS.get(job_id)

    if not job:
        return {"status": "not_found"}

    # ✅ already sanitized, safe to return
    return job
