@echo off
REM Run the backend (Windows)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
