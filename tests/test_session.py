"""
To run tests, use: python -m unittest -v
"""

import unittest
from datetime import timedelta, datetime

from src.time_objects import OfficeStay, SessionCounter


class SessionTests(unittest.TestCase):

    def test_session_simplest(self):
        sc = SessionCounter(timedelta(hours=1))

        stay = [OfficeStay(datetime(2023, 2, 15, 20),
                           datetime(2023, 2, 15, 21, 30))]

        lengths = sc.compute_length_in_hours(stay)

        self.assertEqual(lengths[0], 1.5)


if __name__ == '__main__':
    unittest.main()
