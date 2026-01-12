def rule_based_plan(problem_statement: str) -> dict:
    text = problem_statement.lower()

    # --- Clarifying Questions ---
    clarifying_questions = [
        "What teams or roles are involved in this workflow?",
        "How frequently does this problem occur?",
        "What is the current manual effort required?",
        "What systems or tools are currently used?"
    ]

    # --- Proposed Approach ---
    proposed_approach = [
        "Document the current workflow and identify manual steps",
        "Identify bottlenecks or repetitive tasks",
        "Introduce automation for repeatable actions",
        "Define validation or quality checks",
        "Establish ownership and monitoring"
    ]

    # --- Tool Suggestions ---
    recommended_tools = ["Excel", "Email"]

    if "data" in text or "csv" in text:
        recommended_tools.extend(["Python", "Pandas"])

    if "approval" in text or "review" in text:
        recommended_tools.extend(["Workflow tool", "Ticketing system"])

    if "report" in text or "dashboard" in text:
        recommended_tools.extend(["BI Tool", "Database"])

    # --- Risks & Privacy ---
    risks_and_privacy = [
        "Ensure sensitive data is not exposed during automation",
        "Validate access controls and permissions"
    ]

    # --- Next Steps (Action Verbs Only) ---
    next_steps = [
        "Define the scope of the workflow",
        "Review existing tools and integrations",
        "Prototype a simplified solution",
        "Validate results with stakeholders",
        "Iterate based on feedback"
    ]

    return {
        "problem_statement": problem_statement,
        "clarifying_questions": clarifying_questions[:5],
        "proposed_approach": proposed_approach[:7],
        "recommended_tools": list(set(recommended_tools)),
        "risks_and_privacy": risks_and_privacy,
        "next_steps": next_steps
    }
