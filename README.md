# AI Office Hours Helper

A lightweight web application that converts a free-form workflow pain point into a **structured, actionable plan**.

Built using **Python + FastAPI** with a simple frontend, this project demonstrates API design, schema validation, deterministic fallbacks, and free public deployment.

---

## 🚀 Project Goal

The goal of this project is to:

- Accept a free-form description of a workflow problem
- Generate a structured action plan
- Display the plan in:
  - A **human-readable format**
  - The **raw JSON output**
- Support **two execution modes**:
  - LLM-based (Option A)
  - Deterministic, rule-based (Option B – no external calls)

---

## 🧩 Features

- ✅ Free-form text input
- ✅ API call on **Generate Plan**
- ✅ Strict schema-validated output
- ✅ Human-readable plan view
- ✅ Raw JSON view
- ✅ Loading and error handling
- ✅ Deterministic offline mode (Option B)
- ✅ Free public deployment

---

## 📐 Output Schema

The API always returns the following structure:

```json
{
  "problem_statement": "string",
  "clarifying_questions": ["string"],
  "proposed_approach": ["string"],
  "recommended_tools": ["string"],
  "risks_and_privacy": ["string"],
  "next_steps": ["string"]
}
