from datetime import datetime, timedelta
from typing import List, Tuple


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.events = []
        self.office_stays: List[Tuple[datetime, timedelta]] = []

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

        for is_check_in, event_time in self.events:
            if is_check_in and last_check_in is None:
                # checking in
                last_check_in = event_time
            elif not is_check_in and last_check_in is not None:
                # checking out, office stay ends now
                length = last_check_in - event_time
                self.office_stays.append((last_check_in, event_time - last_check_in))
                last_check_in = None
            else:
                raise ValueError(f"Inconsistent checking at {event_time}")

    def get_stats_for_month(self, month: int) -> Tuple[str, float, int, float]:
        """
        Gets statistics for a person: name, number of hours, days stayed in office in a given month.
        Plus average hours per day."""
        self.compute_office_stays()

        stays_in_month = filter(lambda x: x[0].month == month, self.office_stays)

        stays = []

        for stay in stays_in_month:
            stays.append((stay[0].day, stay[1].days * 24 + stay[1].seconds / 3600))

        time = sum(stay[1] for stay in stays)
        days = len(set(stay[0] for stay in stays))
        average_per_day = time / days

        return self.name, time, days, average_per_day
