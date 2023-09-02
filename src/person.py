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
        return datetime.now()



    def add_event(self, user: str, direction: str, event_time: str) -> None:
        """Store a check-in event"""
        is_check_in = direction.lower() == "gate_in"
        time = None

        self.events.append((user, is_check_in, time))
        pass