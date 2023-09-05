import unittest
from datetime import timedelta, datetime

from src.time_objects import OfficeStay, SessionCounter


class SessionTests(unittest.TestCase):

    def test_session_simplest(self):
        sc = SessionCounter(timedelta(hours=1))

        stays = [OfficeStay(datetime(2023, 2, 15, 20),
                           datetime(2023, 2, 15, 21, 30))]

        lengths = sc.compute_length_in_hours(stays)

        self.assertEqual(lengths[0], 1.5)

    def test_compute_longest_session(self):
        # create a counter with 2 hours of max break
        sc = SessionCounter(timedelta(hours=2))

        stays = [
            # add a long session from two parts with <2 hours break:
            # 20-21.30 and 23-1 at next day, total: 5 hours
            OfficeStay(
                datetime(2023, 2, 15, 20),
                datetime(2023, 2, 15, 21, 30)),
            OfficeStay(
                datetime(2023, 2, 15, 23),
                datetime(2023, 2, 16, 1)),

            # and add one session that is shorter than the total,
            # but longer then each segment separately
            OfficeStay(
                datetime(2023, 2, 16, 23),
                datetime(2023, 2, 17, 2))
        ]

        lengths = sc.compute_length_in_hours(stays)

        self.assertEqual(lengths, [5.0, 3.0])


if __name__ == '__main__':
    unittest.main()
