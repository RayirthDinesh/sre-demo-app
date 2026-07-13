"""Tests for src.ingestion."""

import math
import os

import pytest

from src.ingestion import parse_transactions

CSV_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "sample_transactions.csv"
)


def test_returns_list():
    result = parse_transactions(CSV_PATH)
    assert isinstance(result, list)


def test_correct_length():
    result = parse_transactions(CSV_PATH)
    assert len(result) == 5


def test_amounts_are_floats():
    result = parse_transactions(CSV_PATH)
    assert all(isinstance(amount, float) for amount in result)


def test_no_null_amounts():
    result = parse_transactions(CSV_PATH)
    assert all(not math.isnan(amount) for amount in result)


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        parse_transactions("does_not_exist.csv")
