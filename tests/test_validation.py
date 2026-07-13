"""Tests for src.validation."""

import pytest

from src.validation import validate_amount, validate_transaction


def test_valid_amount_passes():
    assert validate_amount(100.0) is True


def test_zero_fails():
    assert validate_amount(0) is False


def test_negative_fails():
    assert validate_amount(-5.0) is False


def test_numeric_string_is_cast():
    # A numeric string must be cast to float, not compared directly.
    assert validate_amount("42.50") is True


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        validate_amount(None)


def test_valid_transaction_passes():
    transaction = {"id": 1, "amount": 100.0, "currency": "USD"}
    assert validate_transaction(transaction) is True


def test_missing_field_fails():
    transaction = {"id": 1, "amount": 100.0}  # no currency
    assert validate_transaction(transaction) is False
