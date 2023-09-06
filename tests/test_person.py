import unittest
from datetime import datetime

from homework.person import Person


class PersonTests(unittest.TestCase):

    def test_person_time_parsing(self):
        """Test parsing input line"""
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
        """Test office stay calculation"""
        person = Person("Bela")

        person.add_event("GATE_IN", "2023-01-31T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-01-31T09:18:36.000Z")

        person.compute_office_stays()

        stay = person.office_stays[0]

        self.assertAlmostEqual(stay.length_in_hours, 1.0)

        self.assertEqual(stay.check_in.year, 2023)
        self.assertEqual(stay.check_in.month, 1)
        self.assertEqual(stay.check_in.day, 31)
        self.assertEqual(stay.check_in.hour, 8)
        self.assertEqual(stay.check_in.minute, 18)
        self.assertEqual(stay.check_in.second, 36)
        self.assertEqual(stay.check_in.microsecond, 0)

    def test_person_stats_in_February(self):
        """Test statistic calculation for a given month"""
        person = Person("Bela")

        person.add_event("GATE_IN", "2023-02-15T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-02-15T09:18:36.000Z")

        person.add_event("GATE_IN", "2023-02-16T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-02-16T10:18:36.000Z")

        person.add_event("GATE_IN", "2023-03-16T08:18:36.000Z")
        person.add_event("GATE_OUT", "2023-03-16T10:18:36.000Z")

        stat = person.get_stats_for_month(2)

        self.assertEqual(stat.name, "Bela")
        self.assertAlmostEqual(stat.time, 3.0)  # number of hours
        self.assertEqual(stat.days, 2)  # number of days
        self.assertAlmostEqual(stat.avg_time_per_days, 1.5)  # avg. hours per day

    def test_work_over_midnight(self):
        """When someone works overnight, it should be noted and added to separate days."""
        person = Person("Bela")

        # person works overnight
        person.add_office_stay(
            datetime(2023, 2, 15, 23),
            datetime(2023, 2, 16, 1))

        # assert that two OfficeStays were created!
        self.assertEqual(len(person.office_stays), 2)

        first_stay = person.office_stays[0]
        second_stay = person.office_stays[1]

        self.assertEqual(first_stay.day_of_month, 15)
        self.assertAlmostEqual(first_stay.length_in_hours, 1.0)
        self.assertEqual(second_stay.day_of_month, 16)
        self.assertAlmostEqual(second_stay.length_in_hours, 1.0)

    def test_break_length_computation(self):
        """Test the computation of break lengths"""
        person = Person("Bela")

        person.add_event("GATE_IN", "2023-02-15T08:00:00.000Z")
        person.add_event("GATE_OUT", "2023-02-15T09:00:00.000Z")

        person.add_event("GATE_IN", "2023-02-15T10:00:00.000Z")
        person.add_event("GATE_OUT", "2023-02-15T11:00:00.000Z")

        person.add_event("GATE_IN", "2023-02-15T14:00:00.000Z")
        person.add_event("GATE_OUT", "2023-02-15T18:00:00.000Z")

        person.add_event("GATE_IN", "2023-02-15T19:00:00.000Z")
        person.add_event("GATE_OUT", "2023-02-15T20:00:00.000Z")

        lunch_breaks, non_lunch_breaks = person.get_break_lengths()

        self.assertEqual(len(lunch_breaks), 1)
        self.assertAlmostEqual(lunch_breaks[0], 3.0)  # between 11-14

        self.assertEqual(len(non_lunch_breaks), 2)
        self.assertAlmostEqual(non_lunch_breaks[0], 1.0)  # between 9-10
        self.assertAlmostEqual(non_lunch_breaks[1], 1.0)  # between 18-19


if __name__ == '__main__':
    unittest.main()
