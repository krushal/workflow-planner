from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.schemas import ActionPlan
from app.llm import generate_action_plan
from app.rule_engine import rule_based_plan

import os

USE_RULE_ENGINE_ONLY = os.getenv("USE_RULE_ENGINE_ONLY", "false").lower() == "true"


app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
def read_index():
    return FileResponse(os.path.join("static", "index.html"))


class UserInput(BaseModel):
    problem_statement: str


@app.post("/generate-plan", response_model=ActionPlan)
def generate_plan(data: UserInput):
    if not data.problem_statement.strip():
        raise HTTPException(status_code=400, detail="Problem statement is required")
    

    if USE_RULE_ENGINE_ONLY:
        return ActionPlan(**rule_based_plan(data.problem_statement))


    # Try LLM first (Option A)
    try:
        result = generate_action_plan(data.problem_statement)
        return ActionPlan(**result)

    # Fallback to Option B
    except Exception:
        fallback = rule_based_plan(data.problem_statement)
        return ActionPlan(**fallback)
