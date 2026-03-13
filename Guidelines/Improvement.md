# Improving Existing Simulations

This guide outlines the recommended workflow for AI agents to improve existing NGSS interactive science simulations within this repository.

Our goal is to ensure every simulation correctly aligns with its Disciplinary Core Ideas (DCIs), Crosscutting Concepts (CCCs), and Science and Engineering Practices (SEPs), while maintaining code quality, pedagogical value, and testing rigor.

## 1. Review the Evaluation
Before making any changes to an existing simulation, always read its evaluation block. These evaluations are stored in the simulation's corresponding category `README.md` file (e.g., `Simulations/PhysicalSciences/README.md`) within a collapsible `<details>` block under the simulation description.

Pay close attention to two critical sections within the evaluation:
1. **AI Action Items for Improvement:** These translate pedagogical gaps into explicit, technical directives.
2. **Implementation Checklist for AI Agent:** A clear, itemized markdown checklist of strict, technical requirements.

Your primary directive when improving a simulation is to implement all directives from the "Implementation Checklist" and "AI Action Items for Improvement".

## 2. Validate with NGSS Standards
While the evaluation provides direct guidance, always ground your improvements in the actual NGSS Evidence Statements (e.g., `NGSS/HighSchoolPhysicalSciencesEvidenceStatements.md`).

*   Verify that your implementation satisfies the specific "Observable Features" (e.g., 1.a.i, 3.b.ii) identified in the evaluation.
*   Ensure the simulation remains an effective "Investigative Phenomenon" or "Anchoring Phenomenon" according to the criteria in `NGSS/PhenomenaNGSS.md`.

## 3. Implement Best Practices
When refactoring or expanding the simulation, you must adhere strictly to the repository's core guidelines, outlined in `AGENTS.md` and `Guidelines/SimulationGeneration.md`:

*   **Single-File Architecture:** Keep all HTML, CSS, and JS within the same standalone file. Do not rely on external CSS/JS files (except trusted CDNs like Tailwind CSS or Chart.js).
*   **Styling & UI:** Use Tailwind CSS to ensure a responsive, clean, and modern user interface.
*   **Performance:** Use the HTML5 `<canvas>` element for complex or particle-based animations. Ensure canvas logic uses `requestAnimationFrame` for smooth rendering.
*   **Mathematical Accuracy & Display:** Render math using standard HTML tags (`<sup>`, `<sub>`) and HTML entities (`&ge;`, `&Delta;`). Do not use LaTeX (`$$`) or MathJax.

## 4. Testing and Verification
After implementing the improvements, you must verify that the simulation functions correctly and that no regressions were introduced.

1.  **Frontend Verification:** Follow the manual frontend verification workflow. Write a temporary Playwright script to capture screenshots of your changes to `/home/jules/verification/`. Submit the verification.
2.  **Automated Tests:** If the simulation has an associated Python test script in the `tests/` directory, run it locally (`python tests/test_filename.py`) to verify everything passes. If you exposed new global functions (e.g., `window.myFunction`), ensure they are tested.

## 5. Finalizing Improvements
Once improvements are implemented and verified:
1.  **Update the README Description:** Update the simulation's description in its category's `README.md` to briefly reflect the new capabilities, ensuring you append the current date and time `[YYYY-MM-DD HH:MM:SS]` at the end of the new description.
2.  **Publish the Updates:** Regenerate the corresponding HTML file by executing the `convert_readme_to_html.py` script from the repository root (`python convert_readme_to_html.py`). This ensures the updated description and the existing evaluation are published correctly to the static website.
