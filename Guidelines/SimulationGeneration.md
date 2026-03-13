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
*   **Investigative Sandboxes:** Do not outright provide the final scientific explanation in the UI. The simulation should serve as an investigative sandbox for students to gather evidence and construct their own explanations, leaving the definitive scientific conclusion for teacher-led follow-up activities.

## 4. Technical Constraints & UI/UX Best Practices
*   **Single File:** Simulations must be completely contained within a single standalone HTML file. Do not rely on external CSS/JS files (except trusted CDNs like Tailwind CSS or Chart.js).
*   **Styling:** Use Tailwind CSS for all styling. Ensure the UI is responsive, clean, and modern. Use a `glass-panel` aesthetic or structured cards to separate controls from the canvas.
*   **Graphics:** Use the HTML5 `<canvas>` element for complex, performant animations (like particle systems, planetary orbits, or molecule interactions). Always cache DOM element queries (e.g., `document.getElementById`) outside of `requestAnimationFrame` loops.
*   **3D Libraries:**
    *   **Three.js:** Avoid continuously destroying and recreating meshes in animation loops; create them once and update properties. When objects must be removed, explicitly call `.dispose()` on their geometry and materials to prevent memory leaks. Note that `PlaneGeometry` default generated vertices traverse the Y-axis from positive to negative.
    *   **3Dmol.js:** When fetching molecules from PubChem, use a direct URL string (e.g., `url:https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/<CID>/SDF`) instead of the `cid:` prefix to prevent 404 errors.
*   **JavaScript Syntax Limitations:**
    *   When writing JavaScript strings inside manipulated HTML, prefer standard string concatenation (e.g., `'hsla(' + value + ')'`) over ES6 template literals (`` `hsla(${value})` ``) to prevent escaping conflicts and `SyntaxError`s caused by backticks and dollar signs.
    *   Use double quotes for string literals or properly escape single quotes if text contains apostrophes.
    *   When using Python scripts to rewrite JS blocks, be cautious with multiline strings containing unescaped backslashes (e.g., `\n`) which can cause 'Invalid or unexpected token' syntax errors. Use properly escaped newlines or raw strings.
*   **No LaTeX:** Do not use `$$` or MathJax. Render math using standard HTML tags (`<sup>`, `<sub>`) and HTML entities (`&ge;`, `&Delta;`).
*   **SEO & Metadata:** Include the standard `<head>` metadata, Open Graph tags, and Schema.org `LearningResource` JSON-LD to ensure the simulation is indexable.

## 5. Testability
Your simulation must be testable by Python Playwright scripts.
*   **Decouple Logic:** Separate your mathematical/simulation engine from the DOM/Canvas rendering. Expose the `updateSimulation()` function or specific state variables to the global `window` object so Playwright can verify the internal state without relying entirely on visual pixels.
*   **Event Listeners:** Ensure UI controls trigger standard DOM events (`change`, `input`, `click`) so Playwright's `page.evaluate()` can interact with them reliably.