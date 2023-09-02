"""
To run tests, use: python -m unittest -v
"""

import unittest
from src.person import Person

class Tests(unittest.TestCase):

    def test_person_time_parsing(self):
        person = Person("Bela")
        
        time = person.parse_time("2023-01-31T08:18:36.000Z")

        self.assertEqual(time.year, 2023)
        self.assertEqual(time.month, 1)
        self.assertEqual(time.day, 31)
        self.assertEqual(time.hour, 8)
        self.assertEqual(time.minute, 18)
        self.assertEqual(time.second, 36)
        self.assertEqual(time.microsecond, 0)
    

    def test_person_time_parsing2(self):
        person = Person("Bela")
        
        time = person.parse_time("2023-03-03T20:24:54.500Z")
        self.assertEqual(time.year, 2023)
        self.assertEqual(time.month, 3)
        self.assertEqual(time.day, 3)
        self.assertEqual(time.hour, 20)
        self.assertEqual(time.minute, 24)
        self.assertEqual(time.second, 54)
        self.assertEqual(time.microsecond, 500_000)


if __name__ == '__main__':
    unittest.main()