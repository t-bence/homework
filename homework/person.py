from datetime import datetime, timedelta
from typing import List, Tuple
from .time_objects import OfficeStay, SessionCounter


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.events: List[Tuple[bool, datetime]] = []
        self.office_stays: List[OfficeStay] = []

    def add_event(self, direction: str, timestamp: str) -> None:
        """Store a check-in or check-out event"""

        is_check_in = direction.lower() == "gate_in"

        # timestamp is basically an ISO format
        # we just need to remove the Z from the end
        event_time = datetime.fromisoformat(timestamp[:-1])

        self.events.append((is_check_in, event_time))

    def compute_office_stays(self) -> None:
        """
        Compute stays in the office from the events.
        Uses a small state machine to keep track of people in and out, to make sure we notice errors.
        """
        last_check_in = None  # datetime of last checkin, if checked in currently, else None

        # sort the events for the sake of safety
        self.events.sort(key=lambda x: x[1])

        for is_check_in, event_time in self.events:
            # if last check-in time is None, person is not checked in
            if is_check_in and last_check_in is None:
                last_check_in = event_time

            # if last check-in time is not None, user is checked in
            elif not is_check_in and last_check_in is not None:
                # checking out, office stay ends now
                self.add_office_stay(last_check_in, event_time)
                last_check_in = None

            # every other case must be an error
            else:
                raise ValueError(f"Inconsistent checking by {self.name} at {event_time}")

    def add_office_stay(self, start: datetime, end: datetime) -> None:
        """
        This function adds an office stay to the Person's list.
        If the office stay goes over midnight, we might get it in two pieces for the two days.
        """

        office_stays = OfficeStay.create(start, end)

        for stay in office_stays:
            self.office_stays.append(stay)

    def get_stays_in_month(self, month: int) -> List[OfficeStay]:
        """Return only the stays which are in specified month"""
        return list(filter(lambda stay: stay.is_in_month(month), self.office_stays))

    def get_stats_for_month(self, month: int) -> Tuple[str, float, int, float]:
        """
        Gets statistics for a person: name, number of hours, days stayed in office in a given month.
        Plus average hours per day.
        """
        self.compute_office_stays()

        # consider only those in the selected month
        stays = self.get_stays_in_month(month)

        time = sum(stay.length_in_hours for stay in stays)
        days = len(set(stay.day_of_month for stay in stays))  # number of unique days in the month
        average_per_day = time / days

        return self.name, time, days, average_per_day

    def get_longest_session_hours(self, month: int) -> float:
        """
        Compute the length of the longest session in a given month in hours.
        A session is a stay with <2 hours break(s) in it.
        Only sessions starting in given month are to be considered.
        Note: if a session starts in February but ends in March, only its part in
        February is considered as a February session.
        """

        # consider only those in the selected month
        feb_stays = self.get_stays_in_month(month)

        # the limit is two hours
        two_hours = timedelta(hours=2)

        session_counter = SessionCounter(two_hours)

        lengths = session_counter.compute_length_in_hours(feb_stays)

        return max(lengths)
