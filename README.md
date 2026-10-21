# Enterprise Demo

A small Python repository for demonstrating commits, pull requests, CODEOWNERS,
GitHub Actions, CodeQL, and Dependabot.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
python main.py
```

## GitHub setup

- Replace the example team in `CODEOWNERS` with a team that exists in your organization.
- Create the repository in your GitHub Enterprise organization, then push the `main` branch.
- Enable GitHub Advanced Security and CodeQL code scanning in the repository settings if your enterprise requires it.
- Configure repository rulesets in the repository or organization settings; rulesets are managed on GitHub, not in this repository.
- Dependabot checks the Python requirements and GitHub Actions weekly.

The workflows run on pushes to `main` and pull requests targeting `main`.