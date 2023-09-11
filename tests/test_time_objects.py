import unittest
from datetime import timedelta, datetime

from homework.time_objects import OfficeStay, SessionCounter


class SessionTests(unittest.TestCase):

    def test_session_simplest(self):
        """Tests that a simple session length is computed well."""
        sc = SessionCounter(timedelta(hours=1))

        stays = [OfficeStay(datetime(2023, 2, 15, 20),
                            datetime(2023, 2, 15, 21, 30))]

        lengths = sc.compute_length_in_hours(stays)

        self.assertAlmostEqual(lengths[0], 1.5)

    def test_compute_longest_session(self):
        """Tests that sessions from parts are computed well."""
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

        self.assertAlmostEqual(lengths[0], 5.0)
        self.assertAlmostEqual(lengths[1], 3.0)

    def test_too_long_officestay_raises(self):
        """Tests that a ValueError is raised when an OfficeStay is longer than one day"""
        start = datetime(2023, 2, 15, 20, 0)
        end = datetime(2023, 2, 16, 21, 30)

        self.assertRaises(ValueError, OfficeStay.create, start, end)

    def test_sessioncounter_no_event_raises(self):
        """Tests that a ValueError is raised when no OfficeStay is given to SessionCounter"""
        sc = SessionCounter(timedelta(hours=2.0))
        self.assertRaises(ValueError, sc.compute_length_in_hours, [])


if __name__ == '__main__':
    unittest.main()
