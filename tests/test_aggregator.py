"""Tests for src.aggregator."""

import pytest

from src.aggregator import (
    average_value,
    max_value,
    total_value,
    transaction_count,
)

SAMPLE = [100.0, 250.0, 300.0, 350.0, 500.0]  # sums to 1500.0


def test_total_value_correct():
    assert total_value(SAMPLE) == 1500.0


def test_total_value_single_item():
    assert total_value([42.0]) == 42.0


def test_total_value_empty_raises():
    with pytest.raises(ValueError):
        total_value([])


def test_average_value_correct():
    assert average_value(SAMPLE) == 300.0


def test_max_value_correct():
    assert max_value(SAMPLE) == 500.0


def test_transaction_count_correct():
    assert transaction_count(SAMPLE) == 5
