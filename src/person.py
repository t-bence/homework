from datetime import datetime
from typing import List, Tuple
from time_objects import OfficeStay


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
        """Compute stays in the office from the events."""
        last_check_in = None  # datetime of last checkin, if checked in currently, else None

        # sort the events for the sake of safety
        self.events.sort(key=lambda x: x[1])

        for is_check_in, event_time in self.events:
            if is_check_in and last_check_in is None:
                # checking in
                last_check_in = event_time
            elif not is_check_in and last_check_in is not None:
                # checking out, office stay ends now
                self.add_office_stay(last_check_in, event_time)
                last_check_in = None
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

    def get_stats_for_month(self, month: int) -> Tuple[str, float, int, float]:
        """
        Gets statistics for a person: name, number of hours, days stayed in office in a given month.
        Plus average hours per day.
        """
        self.compute_office_stays()

        # consider only those in the selected month
        stays = list(filter(lambda stay: stay.is_in_month(month), self.office_stays))

        time = sum(stay.length_in_hours for stay in stays)
        days = len(set(stay.day_of_month for stay in stays))  # number of unique days in the month
        average_per_day = time / days

        return self.name, time, days, average_per_day
