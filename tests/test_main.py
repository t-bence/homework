import unittest
from src.program import parse_persons


class MainTests(unittest.TestCase):

    def test_person_parsing(self):
        row = ["2e5d8815-4e59-4302-99c0-6fc9593a2eef,GATE_IN,2023-01-31T08:18:36.000Z"]
        name = "2e5d8815-4e59-4302-99c0-6fc9593a2eef"

        persons = parse_persons(row)

        person = list(filter(lambda p: p.name == name, persons))

        self.assertEqual(len(person), 1)

        event = person[0].events[0]
        # direction must be check-in (True)        
        self.assertEqual(event[0], True)
        self.assertEqual(event[1].year, 2023)


if __name__ == '__main__':
    unittest.main()
