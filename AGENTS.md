# Agent Directives

Welcome to the NGSS Simulations project. This repository contains interactive science simulations aligned to the Next Generation Science Standards (NGSS) for High School.

The overarching goal is to ensure every NGSS Performance Expectation listed in the repository has at least one high-quality, scientifically accurate, and engaging HTML simulation.

As an AI agent working in this repository, you must adhere to the following best practices and guidelines to ensure code quality, accurate testing, SEO optimization, and pedagogical alignment.

## 1. Simulation Generation and Design
*   **Single-File Architecture:** Simulations must be completely contained within a single standalone HTML file. Do not rely on external CSS/JS files (except trusted CDNs like Tailwind CSS or Chart.js).
*   **Styling:** Use Tailwind CSS for all styling. Ensure the UI is responsive, clean, and modern.
*   **Graphics:** Use the HTML5 `<canvas>` element for complex, performant animations.
*   **No LaTeX:** Do not use `$$` or MathJax. Render math using standard HTML tags (`<sup>`, `<sub>`) and HTML entities (`&ge;`, `&Delta;`).
*   **SEO & Metadata:** Include the standard `<head>` metadata, Open Graph tags, and Schema.org `LearningResource` JSON-LD to ensure the simulation is indexable.
*   **Chart.js Configurations:** When inputs can drastically vary the data outputs, prefer using `suggestedMax` over a hardcoded `max` limit to ensure dynamically generated points remain visible on the chart without getting clipped. Explicitly constrain its visual footprint by setting a `max-height` on the container or ensuring `maintainAspectRatio` is configured when inside flex or grid containers.
*   **Canvas Random Distributions:** When generating uniformly distributed random particles within a circular or elliptical canvas boundary, use polar coordinates with a square-root distribution for the radius (`r = Math.sqrt(Math.random())`) rather than rejection sampling within a square bounding box.
*   **NGSS Alignment:** Read `Guidelines/SimulationGeneration.md` for complete pedagogical guidelines. Ground simulations in Disciplinary Core Ideas (DCIs), Crosscutting Concepts (CCCs), and Science and Engineering Practices (SEPs). Base functionality directly on the "Observable features of the student performance" lists in the Evidence Statements.

## 2. NGSS Documentation Guidelines
*   The NGSS markdown documents act as a core knowledge base. Maintain their strict heading hierarchy: `##` for Performance Expectations (e.g., `## HS-PS1-1`), `###` for expectation statements, and `####` for categorical dividers (e.g., Science and Engineering Practices).
*   **File Naming:** High School performance expectation markdown files are located in the `NGSS/` directory and use verbose naming conventions (e.g., `HighSchoolLifeSciencesPerformanceExpectations.md`) rather than shorthand acronyms.
*   **Evidence Statements Generation:** NGSS Evidence Statement files are supersets of Performance Expectations. When generating new ones, copy the baseline content (practices, ideas, concepts) from the existing Performance Expectations MDs and append the 'Observable features' lists extracted from PDFs.
*   **Spacing:** Use exactly **two blank lines** before every major performance expectation heading (e.g., `## HS-PS...`) to facilitate AI parsing algorithms.
*   **Paragraphs & Lists:** Ensure a blank line explicitly separates bulleted list items and any subsequent headers (`####`), and 'Assessment Boundary:' statements to form independent paragraphs. Under 'Science and Engineering Practices', introductory text is intentionally un-bulleted, while specific practices are bulleted.
*   **Evidence Statement Formatting:** When formatting Evidence Statements, prepend a standard list bullet (e.g., `* a.`, `* i.`) and use exactly 3 spaces of indentation for first-level nested list items and 6 spaces for second-level nested list items to prevent rendering as `<pre>` code blocks. Convert special bullet characters to standard Markdown bullets (`*`).
*   **HTML in Markdown:**
    *   When including literal HTML tags (like `<textarea>`) as display text, always escape them using HTML entities (e.g., `&lt;textarea&gt;`).
    *   When embedding HTML blocks (like `<details>`) inside Markdown list items, the HTML tags must be properly indented (e.g., 2 spaces) to match the list item depth so downstream parsers like `marked` do not swallow headings.
    *   Always ensure there is at least one blank line immediately following a closing HTML block tag (e.g., `</details>`).

## 3. Playwright Testing & Automation
*   **Running Tests:** Test scripts are located in the `tests/` directory and are standard Python scripts. Run them sequentially using: `for f in tests/test_*.py; do python "$f"; done`. Ensure dependencies are installed via `pip install pytest-playwright playwright && playwright install`.
*   **Decouple Logic:** To unit test complex, DOM-coupled logic (like game loops) in standalone HTML simulations, refactor the logic into pure, decoupled functions, expose them globally (e.g., `window.functionName`), and use Python Playwright scripts to execute and assert the logic.
*   **Loading Resources:** Rather than using `page.set_content()`, navigate directly to the dynamically resolved file URI using `page.goto(file_path)` (where `file_path` is resolved via `os.path.join` from `__file__`) to properly load CDNs and maintain layout. To avoid timeout issues from external resources (like Tailwind CSS) in the testing sandbox, block the requests via network interception (e.g., `await page.route('**/*tailwindcss.com*', lambda route: route.abort())`).
*   **Handling File Paths:** Use fallback paths in Python (e.g., checking both `PhysicalScience` and `PhysicalSciences` directories) to gracefully handle discrepancies.
*   **DOM Interaction Workarounds:**
    *   If click interception occurs due to overlapping elements, use `page.evaluate("document.querySelectorAll('selector')[0].click()")`.
    *   When programmatically setting input values (like range sliders), manually dispatch an 'input' or 'change' event (e.g., `element.dispatchEvent(new Event('input'))`).
    *   If dispatching 'input' events causes race conditions, expose the underlying update function to the global `window` object and call it directly via `page.evaluate()`.
    *   When testing HTML5 drag-and-drop functionality, native `page.drag_and_drop()` may fail. Use `page.evaluate()` to manually dispatch 'drop' events on the target zone or handle the JavaScript logic directly.
*   **Animation Verification:**
    *   When testing canvas animations utilizing `requestAnimationFrame` with Playwright in headless Chromium, explicitly override the document visibility state using `page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")` to ensure the animation loop fires.
    *   Calculate and apply a sufficient `page.wait_for_timeout()` to allow the real-time duration of the animation to fully complete before asserting the final state.
    *   Avoid strict equality constraints (e.g., `value == 0`) and instead use bounded comparisons (e.g., `value < 2`) to prevent test flakiness.
    *   When asserting states in chaotic mathematical models, account for intermediate fluctuating/unstable states during recovery phases instead of asserting strict stable endpoints immediately.
*   **WebGL Rendering:** When using Playwright to verify frontend changes involving WebGL or 3D libraries (like `3Dmol.js`) in headless mode, launch the browser with `args=['--use-gl=egl']` to ensure the 3D canvas renders correctly for screenshots.

## 4. Manual Verification & Frontend Workflow
*   When making user-visible modifications to frontend UI, strictly follow the frontend verification workflow by writing a temporary Playwright script to capture screenshots to `/home/jules/verification/`.
*   For temporary verification scripts, use absolute paths (e.g., `file:///app/Simulations/...`) rather than relative paths.
*   Avoid hardcoding screenshot saves within automated test scripts (in `tests/`) to prevent file path or permission errors; reserve screenshot generation strictly for the manual workflow.

## 5. Repository Management & Website Deployment
*   **README and HTML Conversion:** The root `README.md` and category `README.md` files serve as indices. The repository is deployed as a public static website via GitHub Pages.
    *   When updating simulation README.md files, maintain the format `- [Simulation Title](SimulationFile.html) - Brief description.` Ensure individual simulations are only listed in their respective category's README under a single best-fit NGSS standard, avoiding duplicate listings across multiple standards. Note: when adding a new bullet point, ensure it is placed completely after any `<details>` evaluation blocks associated with preceding simulations.
    *   When structuring category READMEs, list all relevant NGSS Performance Expectations as headings (e.g., `### HS-PS1-1`), include their descriptive text directly beneath the heading, and categorize the associated simulation links underneath.
    *   When adding a **new simulation category**, explicitly append the new `README.md` file path to the `readmes` array within `convert_readme_to_html.py`.
    *   Always run `python convert_readme_to_html.py` after updating `README.md` files. This script requires the `marked` CLI utility (`npm install -g marked`).
    *   Internal links in generated HTML files point to extensionless URLs (for NGSS files) and trailing-slash directory URLs (for Simulation categories) to optimize SEO.
*   **Sitemap Generation:** The repository relies on `sitemap.xml` and `robots.txt` in the root directory for SEO. The sitemap explicitly maps out all `.html` files within the `Simulations/` directory and extensionless URLs for `.md` files in the `NGSS/` directory. Run `python generate_sitemap.py` to automatically update the `sitemap.xml` with newly discovered `.html` and `.md` files.
*   **Jekyll overrides:** The site uses the default `jekyll-theme-primer` layout. To inject custom `<head>` snippets (such as Google Analytics tracking) without altering this default appearance, place the snippets in an `_includes/head-custom.html` file. To override the default layout, alter the `_layouts/default.html` file.

## 6. Evaluating Existing Simulations
*   Read `Guidelines/SimulationEvaluation.md` before performing evaluations.
*   Append your evaluation to the simulation's description in the category's `README.md` as a collapsible HTML `<details>` block with a `<summary>` tag following this format: `<summary><b>Evaluation: [Anchor or Investigative] Phenomenon | [Rating]/5 Stars | [YYYY-MM-DD HH:MM:SS]</b></summary>`.
*   Ensure the internal content has structured items including Overview, Dimensional Evaluation & Evidence Statements, AI Action Items for Improvement (with explicit code directives), and an Implementation Checklist.
*   After appending the evaluation, execute `python convert_readme_to_html.py` to publish the evaluation to the static website.

## 7. Improving Existing Simulations
*   Read `Guidelines/Improvement.md` before making any improvements to an existing simulation.
*   This file outlines how to use an existing evaluation to guide improvements, ensuring strong pedagogical alignment and addressing explicit AI action items from the simulation's evaluation block.

## 8. Workflow & Pull Request Directives
*   **Deep Planning:** Always start tasks in a deep planning mode: interact with the user via `request_user_input` or `message_user` to ask questions and clarify requirements. Discourage asking questions that can be derived from code exploration. Once absolutely certain, create the plan using `set_plan`. Ensure verification steps include explicit, actionable commands.
*   **Execution Rule:** When creating simulations for multiple NGSS performance expectations, process them iteratively. Plan, implement, and verify one simulation at a time rather than batch-planning them. Submit PRs in batches of 3 to 5 items rather than individually or as a single massive PR.
*   **Reading Large Files:** When gathering context from large markdown files (like Evidence Statements), standard shell commands like `grep` or `cat` may be truncated by the 1000 character limit. Write a short Python script using `readlines()` to safely extract and print full sections before drafting execution plans.
*   **Text Manipulation:** When using Python's `re` module or bash to inject text containing LaTeX or special sequences (`$`, `\p`), ensure backslashes are properly escaped or use plain text equivalents to avoid `SyntaxWarning` and formatting regressions. If `replace_with_git_merge_diff` fails due to pre-existing markers, use a bash redirection command (`cat << 'EOF' > filename`) to overwrite safely.
*   **Workspace Cleanup:** Before finalizing a task or requesting a code review, always clean up the workspace by removing temporary 'scratchpad' Python scripts used for reconnaissance or generation, as well as generated directories like `__pycache__`.
*   **Performance Optimizations:** Always run tests before PRs, add explanatory comments, and document impact. Never modify `package.json`/`tsconfig.json` without instruction, make breaking changes, optimize prematurely, or sacrifice code readability. Log critical, codebase-specific performance learnings in `.jules/bolt.md` using the format `## YYYY-MM-DD - [Title] \n**Learning:** [Insight] \n**Action:** [Application]`. Do not journal routine work.
*   **PR Titles & Descriptions:**
    *   For a security fix PR, use the title format '🔒 [security fix description]' and sections '🎯 What:', '⚠️ Risk:', and '🛡️ Solution:'.
    *   For a testing improvement PR, use the title format '🧪 [testing improvement description]' and sections '🎯 **What:**', '📊 **Coverage:**', and '✨ **Result:**'.
    *   For a performance optimization PR, use the title format '⚡ Bolt: [performance improvement]' and include a description containing '💡 What', '🎯 Why', '📊 Impact', and '🔬 Measurement'.
