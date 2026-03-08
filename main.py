import json
from pathlib import Path
from typing import Any, Dict
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Marvin Galdamez Skills API", version="1.0.0")

# Path to the skill.json file
SKILL_FILE_PATH = Path(__file__).parent / "skill.json"

def load_skills() -> Dict[str, Any]:
    if not SKILL_FILE_PATH.exists():
        raise FileNotFoundError(f"{SKILL_FILE_PATH} not found.")
    with open(SKILL_FILE_PATH, "r") as f:
        return json.load(f)

@app.get("/v1/profile/skills")
async def get_skills():
    try:
        skills = load_skills()
        return skills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
