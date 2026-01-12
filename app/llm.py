import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_action_plan(problem_statement: str) -> dict:
    prompt = f"""
You are an AI workflow consultant.

Return ONLY valid JSON using this schema:
{{
  "problem_statement": "string",
  "clarifying_questions": ["string"],
  "proposed_approach": ["string"],
  "recommended_tools": ["string"],
  "risks_and_privacy": ["string"],
  "next_steps": ["string"]
}}

Rules:
- clarifying_questions: 3–5 items
- proposed_approach: 4–7 items
- next_steps must start with action verbs

Workflow problem:
{problem_statement}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)
