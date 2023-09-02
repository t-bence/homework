from datetime import datetime

class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.events = []


    def parse_time(self, timestamp: str) -> datetime:
        """
        Parse a datetime from a formatted string
        Input string format: 2023-01-31T08:18:36.000Z
        """

        # this is basically an ISO format
        # we just need to remove the Z from the end
        return datetime.fromisoformat(timestamp[:-1])



    def add_event(self, user: str, direction: str, event_time: str) -> None:
        """Store a check-in event"""
        is_check_in = direction.lower() == "gate_in"
        time = self.parse_time(event_time)

        self.events.append((user, is_check_in, time))
        pass