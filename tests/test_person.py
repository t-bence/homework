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

        start, length = person.office_stays[0]

        self.assertEqual(length.total_seconds(), 60*60)

        self.assertEqual(start.year, 2023)
        self.assertEqual(start.month, 1)
        self.assertEqual(start.day, 31)
        self.assertEqual(start.hour, 8)
        self.assertEqual(start.minute, 18)
        self.assertEqual(start.second, 36)
        self.assertEqual(start.microsecond, 0)

    def test_person_stays_in_February(self):
        pass


if __name__ == '__main__':
    unittest.main()
