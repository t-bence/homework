"""
To run tests, use: python -m unittest -v
"""

import unittest
from src.person import Person


class PersonTests(unittest.TestCase):

    def test_person_time_parsing(self):
        person = Person("Bela")

        row = ["2e5d8815-4e59-4302-99c0-6fc9593a2eef,GATE_IN,"]
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


if __name__ == '__main__':
    unittest.main()
