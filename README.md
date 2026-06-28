# Self-Healing Autonomous SRE Agent — Demo Backend

A dummy backend codebase used to exercise a Self-Healing Autonomous SRE Agent.
A CI/CD pipeline (GitHub Actions) monitors this repo. When a build or test
fails, the agent intercepts the failure, diagnoses the root cause, writes a
fix, validates it in a Docker sandbox, and opens a pull request automatically.

## The application

A small Python data-processing pipeline:

1. **Ingestion** — reads transaction data from a CSV into a list of amounts.
2. **Validation** — checks amounts and transaction records.
3. **Aggregation** — totals, averages, max, and counts.
4. **Reporting** — formats a human-readable report and a summary dict.

## Layout

```
.
├── .github/workflows/ci.yml   # runs pip install + pytest on every push
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
