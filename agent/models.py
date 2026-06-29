"""Pydantic models for the webhook server.

Defining the request body as a Pydantic model gives us automatic validation:
if GitHub Actions sends a payload missing a field or with the wrong type,
FastAPI rejects it with a 422 before our handler ever runs.
"""

from pydantic import BaseModel


class WebhookPayload(BaseModel):
    """The JSON body GitHub Actions POSTs to /webhook after a CI run."""

    repo: str             # full repo name, e.g. "username/sre-agent-demo"
    branch: str           # branch that was pushed, e.g. "bug/logic-error"
    commit_sha: str       # commit SHA that triggered the run
    workflow_run_id: str  # GitHub Actions run id (string, ids can be large)
    test_logs: str        # full captured pytest/install output
    status: str           # "failure" or "success"
