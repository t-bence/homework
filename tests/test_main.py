"""
To run tests, use: python -m unittest -v
"""

import unittest
from src.program import parse_persons


class MainTests(unittest.TestCase):

    def test_person_parsing(self):
        row = ["2e5d8815-4e59-4302-99c0-6fc9593a2eef,GATE_IN,2023-01-31T08:18:36.000Z"]
        name = "2e5d8815-4e59-4302-99c0-6fc9593a2eef"

        persons_dict = parse_persons(row)

        person = persons_dict[name]

        self.assertEqual(person.name, name)

        event = person.events[0]
        # direction must be check-in (True)        
        self.assertEqual(event[0], True)
        self.assertEqual(event[1].year, 2023)


if __name__ == '__main__':
    unittest.main()
