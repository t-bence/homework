"""
To run tests, use: python -m unittest -v
"""

import unittest
from src.program import Person

class Tests(unittest.TestCase):

    def test_person_greeting(self):
        person = Person()
        self.assertEqual(person.greet(), "Hello")

if __name__ == '__main__':
    unittest.main()