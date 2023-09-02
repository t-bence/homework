from datetime import datetime


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.events = []

    def add_event(self, direction: str, timestamp: str) -> None:
        """Store a check-in or check-out event"""

        is_check_in = direction.lower() == "gate_in"

        # timestamp is basically an ISO format
        # we just need to remove the Z from the end
        event_time = datetime.fromisoformat(timestamp[:-1])

        self.events.append((is_check_in, event_time))
