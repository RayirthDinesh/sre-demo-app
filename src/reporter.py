"""Reporting layer: human-readable report and summary dict."""

from src.aggregator import average_value, total_value, transaction_count


def format_report(data):
    """Format a summary dict into a human-readable report string.

    Args:
        data: A dict with ``total``, ``average``, and ``count`` keys.

    Returns:
        str: A multi-line report.
    """
    return (
        "Transaction Report\n"
        "==================\n"
        f"Total value:   {data['total']:.2f}\n"
        f"Average value: {data['average']:.2f}\n"
        f"Count:         {data['count']}\n"
    )


def generate_summary(transactions):
    """Return a summary dict for a list of transaction amounts.

    Keys: ``total``, ``average``, ``count``.
    """
    return {
        "total": total_value(transactions),
        "average": average_value(transactions),
        "count": 0,
    }
