# SRE Demo App

A small Python data-processing backend used as the test subject for the
[Self-Healing Autonomous SRE Agent](https://github.com/RayirthDinesh/Self-Healing-Autonomous-DevOps-Agent).
Every push to `main` or a `bug/*` branch runs the pytest suite in CI; on
failure, CI POSTs the logs to the agent's webhook, which diagnoses the bug,
writes a fix, validates it, and opens a pull request here automatically.

## The application

1. **Ingestion** — reads transaction data from a CSV into a list of amounts.
2. **Validation** — checks amounts and transaction records.
3. **Aggregation** — totals, averages, max, and counts.
4. **Reporting** — formats a human-readable report and a summary dict.

## Layout

```
.
├── .github/workflows/ci.yml   # pip install + pytest on every push, result POSTed to the agent
├── src/
│   ├── ingestion.py           # parse_transactions(filepath) -> list[float]
│   ├── validation.py          # validate_amount, validate_transaction
│   ├── aggregator.py          # total/average/max/count
│   └── reporter.py            # format_report, generate_summary
├── tests/                     # pytest suite, all green on main
├── data/sample_transactions.csv
├── requirements.txt
└── README.md
```

## Run locally

```bash
pip install -r requirements.txt
pytest -v --tb=long
```

## Branches (intentional bugs)

`main` is the clean baseline — all tests pass. Four branches each introduce a
single, isolated bug for the agent to diagnose and fix:

| Branch            | Failure mode                                              |
|-------------------|----------------------------------------------------------|
| `bug/dependency`  | `pandas` pinned to `0.24.0` — install fails / ImportError |
| `bug/logic-error` | `total_value` sums `transactions[1:]` — wrong total      |
| `bug/type-error`  | `validate_amount` drops the cast — TypeError on strings   |
| `bug/edge-case`   | blank amount in CSV — null propagates through parsing     |

## Wiring to the agent

CI needs two Actions secrets (Settings → Secrets and variables → Actions):

| Secret           | Value                                       |
|------------------|---------------------------------------------|
| `WEBHOOK_URL`    | `http://<agent-server-ip>:8000/webhook`     |
| `WEBHOOK_SECRET` | must match the agent server's `.env`        |
