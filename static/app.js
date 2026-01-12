async function generatePlan() {
  const text = document.getElementById("problem").value;
  const loading = document.getElementById("loading");
  const error = document.getElementById("error");

  error.innerText = "";
  if (!text.trim()) {
    error.innerText = "Please enter a workflow problem.";
    return;
  }

  loading.hidden = false;

  try {
    const res = await fetch("/generate-plan", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ problem_statement: text })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail);

    renderPlan(data);
    document.getElementById("json").innerText =
      JSON.stringify(data, null, 2);

  } catch (err) {
    error.innerText = err.message;
  } finally {
    loading.hidden = true;
  }
}

function renderPlan(d) {
  document.getElementById("plan").innerHTML = `
    <h3>Problem Statement</h3><p>${d.problem_statement}</p>
    <h3>Clarifying Questions</h3><ul>${d.clarifying_questions.map(q => `<li>${q}</li>`).join("")}</ul>
    <h3>Proposed Approach</h3><ul>${d.proposed_approach.map(p => `<li>${p}</li>`).join("")}</ul>
    <h3>Recommended Tools</h3><p>${d.recommended_tools.join(", ")}</p>
    <h3>Risks & Privacy</h3><ul>${d.risks_and_privacy.map(r => `<li>${r}</li>`).join("")}</ul>
    <h3>Next Steps</h3><ul>${d.next_steps.map(s => `<li>☐ ${s}</li>`).join("")}</ul>
  `;
}
