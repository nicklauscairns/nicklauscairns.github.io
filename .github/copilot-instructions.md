# GitHub Copilot / Automated Agent Policy for this repository

Purpose
- This file documents repository-level instructions for GitHub Copilot and any automated assistant or bot that reads repository guidance. Its goal is to ensure no pull requests are created automatically.

Policy (short)
- Do NOT create, open, or propose pull requests in this repository unless a human explicitly asks for one.

What "explicitly asks" means
- An explicit ask is a clear, human-authored instruction naming a PR action and intended target, such as:
  - "Create a pull request from branch feature/x into main with title 'Add X' and body '...'"
  - "Open a PR to merge branch fix/typo into main"
  - "Please make a PR for the changes in branch Y and set reviewers to @nicklauscairns"
- Vague requests like "please fix this" or "suggest changes" are NOT explicit PR requests.

Allowed behavior
- Suggest code snippets, diffs, or commands that a human can review locally.
- Create patches or show git commands (e.g., `git add`, `git commit`, `git format-patch`) for human execution.
- Draft PR text for a human to copy and submit manually — but do NOT submit or create the PR.

Disallowed behavior
- Automatically creating, opening, or submitting pull requests on behalf of a user or system agent.
- Using repository automation to push branches and immediately open PRs without a human explicit request.
- Any silent background action that results in a PR being opened.

How to request a PR (recommended format)
- Use an explicit, human-generated instruction containing:
  - action: "create pull request" / "open PR"
  - source branch
  - target branch
  - PR title (optional but recommended)
  - PR body (optional)
  - reviewers/assignees (optional)
- Example: `Create a pull request from branch feature/gallery into main with title "Add gallery" and body "Implements gallery feature; ready for review."`

Enforcement & recommendations
- This file documents intent but is not an access-control mechanism. To enforce:
  - Enable branch protections (required reviews, restrict who can push).
  - Use a GitHub Action that checks PR creators and fails if a PR was opened by an unauthorized actor (example workflows are available).
  - Limit repo write permissions for automation accounts that should not create PRs.

Contact
- Repo owner: @nicklauscairns
- If a Copilot instance produces a PR without explicit instruction, please report the event and include logs/screenshots.
