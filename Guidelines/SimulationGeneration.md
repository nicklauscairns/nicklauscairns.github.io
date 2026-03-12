# NGSS Simulation Generation Guidelines

This document provides advice, best practices, and guidelines for AI agents when designing and coding new High School Next Generation Science Standards (NGSS) simulations.

## 1. Ground the Simulation in the Dimensions
Every NGSS simulation must be driven by the **three dimensions** outlined in the Evidence Statements (e.g., `NGSS/HighSchoolPhysicalSciencesEvidenceStatements.md`).
*   **Disciplinary Core Ideas (DCIs):** The scientific content must be accurate. Ensure the underlying logic engine reflects the fundamental laws described in the DCI.
*   **Crosscutting Concepts (CCCs):** Highlight the CCC explicitly. If the CCC is "Patterns", build UI that allows the student to compare multiple variables side-by-side to discover the pattern.
*   **Science and Engineering Practices (SEPs):** This is where many simulations fail. *Students must "do" the science.* If the SEP is "Developing and Using Models," the student should be able to manipulate, build, or adjust the model—not just click "play" and observe an animation. Allow students to set parameters, hypothesize, and test.

## 2. Design for "Observable Features"
Do not guess what the student needs to learn; read the "Observable features of the student performance" list in the Evidence Statement markdown files.
*   If an observable feature states: "Students predict the number and types of bonds...", your simulation must include a specific UI element (like a quiz prompt, a prediction slider, or a sandbox area) that tests or allows this prediction before showing the answer.
*   Check off every sub-point (e.g., 1.a.i, 3.b.ii) in your simulation logic.

## 3. Phenomena-Driven Design
Simulations should act as **Phenomena** (refer to `NGSS/PhenomenaNGSS.md`).
*   **Investigable:** The phenomenon should not be immediately obvious. Students should have to manipulate variables to figure out *why* something is happening.
*   **Cultural and Personal Relevance (Criterion 1):** Frame the simulation around real-world contexts that matter to high schoolers. Don't just simulate "Heat Transfer"; simulate "Why does a metal slide burn your leg in the summer while the plastic swing doesn't?"
*   **Mystery Elements:** Including "Mystery Materials" or "Unknown Variables" is a highly effective way to encourage investigation and challenge assumptions.

## 4. Technical Constraints & UI/UX Best Practices
*   **Single File:** Simulations must be completely contained within a single standalone HTML file. Do not rely on external CSS/JS files (except trusted CDNs like Tailwind CSS or Chart.js).
*   **Styling:** Use Tailwind CSS for all styling. Ensure the UI is responsive, clean, and modern. Use a `glass-panel` aesthetic or structured cards to separate controls from the canvas.
*   **Graphics:** Use the HTML5 `<canvas>` element for complex, performant animations (like particle systems, planetary orbits, or molecule interactions).
*   **No LaTeX:** Do not use `$$` or MathJax. Render math using standard HTML tags (`<sup>`, `<sub>`) and HTML entities (`&ge;`, `&Delta;`).
*   **SEO & Metadata:** Include the standard `<head>` metadata, Open Graph tags, and Schema.org `LearningResource` JSON-LD to ensure the simulation is indexable.

## 5. Testability
Your simulation must be testable by Python Playwright scripts.
*   **Decouple Logic:** Separate your mathematical/simulation engine from the DOM/Canvas rendering. Expose the `updateSimulation()` function or specific state variables to the global `window` object so Playwright can verify the internal state without relying entirely on visual pixels.
*   **Event Listeners:** Ensure UI controls trigger standard DOM events (`change`, `input`, `click`) so Playwright's `page.evaluate()` can interact with them reliably.