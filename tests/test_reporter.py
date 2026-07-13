"""Tests for src.reporter. No bug is ever introduced here."""

from src.reporter import format_report, generate_summary

SAMPLE = [100.0, 250.0, 300.0, 350.0, 500.0]


def test_format_report_returns_string():
    report = format_report({"total": 1500.0, "average": 300.0, "count": 5})
    assert isinstance(report, str)


def test_format_report_contains_total():
    report = format_report({"total": 1500.0, "average": 300.0, "count": 5})
    assert "1500" in report


def test_format_report_contains_count():
    report = format_report({"total": 1500.0, "average": 300.0, "count": 5})
    assert "5" in report


def test_summary_has_expected_keys():
    summary = generate_summary(SAMPLE)
    assert set(summary.keys()) == {"total", "average", "count"}


def test_summary_count_is_correct():
    # Self-consistent: count never depends on a buggy aggregation.
    summary = generate_summary(SAMPLE)
    assert summary["count"] == len(SAMPLE)
