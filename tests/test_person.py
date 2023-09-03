"""
To run tests, use: python -m unittest -v
"""

import unittest
from src.person import Person


class PersonTests(unittest.TestCase):

    def test_person_time_parsing(self):
        person = Person("Bela")

        person.add_event("GATE_IN", "2023-01-31T08:18:36.000Z")

        direction, time = person.events[0]

        self.assertEqual(direction, True)

        self.assertEqual(time.year, 2023)
        self.assertEqual(time.month, 1)
        self.assertEqual(time.day, 31)
        self.assertEqual(time.hour, 8)
        self.assertEqual(time.minute, 18)
        self.assertEqual(time.second, 36)
        self.assertEqual(time.microsecond, 0)

    def test_person_office_stay_calculation(self):
        person = Person("Bela")

        person.add_event("GATE_IN", "2023-01-31T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-01-31T09:18:36.000Z")

        person.compute_office_stays()

        stay = person.office_stays[0]

        self.assertEqual(stay.length_in_hours, 1.0)

        self.assertEqual(stay.check_in.year, 2023)
        self.assertEqual(stay.check_in.month, 1)
        self.assertEqual(stay.check_in.day, 31)
        self.assertEqual(stay.check_in.hour, 8)
        self.assertEqual(stay.check_in.minute, 18)
        self.assertEqual(stay.check_in.second, 36)
        self.assertEqual(stay.check_in.microsecond, 0)

    def test_person_stats_in_February(self):
        person = Person("Bela")

        person.add_event("GATE_IN", "2023-02-15T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-02-15T09:18:36.000Z")

        person.add_event("GATE_IN", "2023-02-16T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-02-16T10:18:36.000Z")

        stats = person.get_stats_for_month(2)

        self.assertEqual(stats[0], "Bela")
        self.assertEqual(stats[1], 3.0)  # number of hours
        self.assertEqual(stats[2], 2)  # number of days
        self.assertEqual(stats[3], 1.5)  # avg. hours per day


if __name__ == '__main__':
    unittest.main()
