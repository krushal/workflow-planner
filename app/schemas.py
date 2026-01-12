from pydantic import BaseModel, Field
from typing import List

class ActionPlan(BaseModel):
    problem_statement: str

    clarifying_questions: List[str] = Field(min_items=3, max_items=5)
    proposed_approach: List[str] = Field(min_items=4, max_items=7)
    recommended_tools: List[str]
    risks_and_privacy: List[str] = Field(min_items=1)
    next_steps: List[str]
