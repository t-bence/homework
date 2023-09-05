from __future__ import annotations
from datetime import datetime, timedelta
from typing import List


def timedelta_to_hours(td: timedelta) -> float:
    """Convert timedelta to hours. Microseconds are ignored here."""
    return td.days * 24 + td.seconds / 3600


class OfficeStay:
    """
    This class represents a continuous time period between a check-in and a check-out.
    """

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
            # Stays longer than one day may affect three days, this is not currently handled.
            raise ValueError(f"An office stay cannot be longer than one day!")

    def is_followed_within(self, next_stay: OfficeStay, max_break: timedelta) -> bool:
        """Return if the present OfficeStay is followed by next_stay within max_break"""
        return (next_stay.check_in - self.check_out) < max_break

    def hours_spanned_with(self, final_stay: OfficeStay) -> float:
        """
        Return the number of hours in the session starting with the current OfficeStay and
        ending with final_stay. Here breaks are not accounted for.
        """
        length = final_stay.check_out - self.check_in
        return length.total_seconds() / 60 / 60


class SessionCounter:
    """
    This class is responsible for computing session lengths from OfficeStays based on the provided max_break length.
    A session is a bunch of OfficeStays that have < max_break time between.
    """

    def __init__(self, max_break: timedelta) -> None:
        # store the maximum break timedelta
        self.max_break = max_break

    def compute_length_in_hours(self, stays: List[OfficeStay]) -> List[float]:
        """ Computes and returns the length of every session"""

        if not stays:
            raise ValueError("No OfficeStay was provided! Cannot compute length!")

        if len(stays) == 1:
            return [stays[0].length_in_hours]

        # the OfficeStay that starts the current session
        starting_stay = stays[0]

        # session lengths are stored here
        lengths: List[float] = []

        stays.sort(key=lambda s: s.check_in)
        # set the previous stay
        prev_stay = stays[0]

        # loop along the stays beginning from the second
        for stay in stays[1:]:
            # if stay follows prev_stay by less than max_break,
            # it counts as one session
            if prev_stay.is_followed_within(stay, self.max_break):
                # then just move along
                prev_stay = stay

            # if stay follows prev_stay by more than max_break, the session
            # ends, its length is stored and we move on
            else:
                lengths.append(starting_stay.hours_spanned_with(prev_stay))
                starting_stay = stay
                prev_stay = stay

        # close the latest session
        # stay would be unbound if stays[1:] were empty, but then the function
        # would have returned on line 72
        # noinspection PyUnboundLocalVariable
        lengths.append(starting_stay.hours_spanned_with(stay))

        return lengths
