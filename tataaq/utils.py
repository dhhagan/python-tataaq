"""Includes helper functions."""

import dateutil


def to_naive_timestamp(timestamp):
    """Convert a timezone aware timestamp (as a string) and return."""
    return dateutil.parser.parse(timestamp).replace(tzinfo=None).isoformat()
