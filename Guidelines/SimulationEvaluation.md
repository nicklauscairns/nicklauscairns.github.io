# NGSS Simulation Evaluation Guidelines

This document provides a structured methodology for AI agents to evaluate the quality, engagement, and alignment of existing NGSS simulations in this repository.

## 1. Grounding the Evaluation
When evaluating an existing simulation, you **must** use two primary sources:
1.  **`NGSS/PhenomenaNGSS.md`:** To determine if the simulation functions effectively as an Anchoring or Investigative phenomenon, and to evaluate it against the 5 criteria for effective phenomena (e.g., Cultural and Personal Relevance, Investigable Through Practices).
2.  **The corresponding Evidence Statements (e.g., `NGSS/HighSchoolPhysicalSciencesEvidenceStatements.md`):** To verify if the simulation actually enables the specific Disciplinary Core Ideas (DCIs), Crosscutting Concepts (CCCs), Science and Engineering Practices (SEPs), and the numbered "Observable Features."

## 2. Formatting the Evaluation
The evaluation must be appended to the simulation's description in the category's `README.md` (e.g., `Simulations/PhysicalSciences/README.md`) as a collapsible HTML `<details>` block. The format is extremely strict so that future AI agents can parse it and act on the feedback.

### The `<summary>` Tag
The summary tag must follow this exact template:
`<summary><b>Evaluation: [Anchor or Investigative] Phenomenon | [Rating]/5 Stars | [YYYY-MM-DD HH:MM:SS]</b></summary>`

### The Internal Content
Inside the `<details><ul>` block, use the following structured list items:

*   **Overview:** Briefly summarize why it is an anchor or investigative phenomenon. Assess its strengths and weaknesses against the `PhenomenaNGSS.md` criteria (specifically noting Criterion 1: Relevance, and Criterion 4: Investigable).
*   **Dimensional Evaluation & Evidence Statements:** Explicitly state how well the simulation supports the target DCI, CCC, and SEP. You **must** list the specific "Observable Features" (e.g., 1.a.i, 3.b.ii) that the simulation successfully demonstrates, and explicitly call out the ones it fails to support.
*   **AI Action Items for Improvement:** This is the most critical section. Translate the pedagogical gaps into explicit, technical directives.
    *   *Bad:* "Make it more interactive so students can use models."
    *   *Good:* "Improve SEP (Developing Models): Add a `<input type='range'>` slider to let students construct the atom dynamically by adding protons/electrons. Bind this to `elementData` so the simulation calculates reactivity based on the user-built valence shell."
*   **Implementation Checklist for AI Agent:** Conclude with a Markdown checklist (`- [ ]`) of strict, technical requirements that a future AI agent can ingest and convert directly into an execution plan.

## Example Evaluation Structure

```html
<details>
  <summary><b>Evaluation: Investigative Phenomenon | 3.5/5 Stars | 2026-03-12 17:47:30</b></summary>
  <ul>
    <li>
      <b>Overview:</b> Visually engaging, but addresses a specific chemistry sub-component... It effectively challenges assumptions by letting students test different metals (Criterion 4)... However, it lacks deep Cultural and Personal Relevance (Criterion 1) out-of-the-box.
    </li>
    <li>
      <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports DCI (PS1.A) and CCC (Patterns)... However, it weakly supports the full SEP (Developing Models); students act as observers rather than developers. It demonstrates 1.a.i-iii, 2.a.i, and parts of 3.b.iii. It fails to support predicting stable ions (3.b.ii).
    </li>
    <li>
      <b>AI Action Items for Improvement:</b>
      <ul>
        <li><b>Fulfill Observable Feature 3.b.ii (Stable Ions):</b> Add a UI button labeled "Form Ion". When clicked, trigger an animation to remove the valence electron(s)...</li>
      </ul>
    </li>
    <li>
      <b>Implementation Checklist for AI Agent:</b>
      <ul>
        <li>[ ] Implement an "Ionize" function and animation in the `aCanvas`...</li>
      </ul>
    </li>
  </ul>
</details>
```

## 3. Finalizing the Evaluation
After updating the `README.md` file, you **must** regenerate the corresponding HTML file by executing the `convert_readme_to_html.py` script from the root directory (`python convert_readme_to_html.py`). This ensures the evaluation is published to the static website.