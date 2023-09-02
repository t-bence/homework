from datetime import datetime, timedelta


def timedelta_to_hours(td: timedelta) -> float:
    """Convert timedelta to hours. Microseconds are ignored here."""
    return td.days * 24 + td.seconds / 3600


class OfficeStay:
    def __init__(self, check_in: datetime, check_out: datetime) -> None:
        if check_in.year != check_out.year or check_in.month != check_out.month or check_in.day != check_out.day:
            raise ValueError(f"OfficeStay starting at {check_in} covers multiple days!")

        self.check_in = check_in
        self.check_out = check_out
        self.length_in_hours = timedelta_to_hours(check_out - check_in)
        self.day_of_month = check_in.day

    def is_in_month(self, month: int) -> bool:
        return self.check_in.month == month
