from __future__ import annotations
from datetime import datetime, timedelta
from typing import List


def timedelta_to_hours(td: timedelta) -> float:
    """Convert timedelta to hours. Microseconds are ignored here."""
    return td.days * 24 + td.seconds / 3600


class OfficeStay:
    def __init__(self, check_in: datetime, check_out: datetime) -> None:
        self.check_in = check_in
        self.check_out = check_out
        self.length_in_hours = timedelta_to_hours(check_out - check_in)
        self.day_of_month = check_in.day

    def is_in_month(self, month: int) -> bool:
        return self.check_in.month == month

    @staticmethod
    def create(start: datetime, end: datetime) -> List[OfficeStay]:
        """Create a list of OfficeStay objects from start and end time."""

        return [OfficeStay(start, end)]
