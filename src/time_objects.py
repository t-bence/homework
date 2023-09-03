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

        if start.year == end.year and start.month == end.month and start.day == end.day:
            return [OfficeStay(start, end)]
        elif (end - start).days < 1.0:
            # Separate OfficeStay into two: start day till midnight and next day from midnight
            # The midnight of the starting day is the starting day's 0:0:00 plus one day.
            # This takes care of month's end, leap days etc.
            midnight = datetime(start.year, start.month, start.day, 0, 0, 0, 0) \
                + timedelta(days=1)
            return [OfficeStay(start, midnight), OfficeStay(midnight, end)]
        else:
            # currently not handled
            raise ValueError(f"An office stay cannot be longer than one day!")
