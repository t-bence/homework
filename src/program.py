"""
This is my solution to the homework task.
It was developed for Python 3.9.1 using the standard library.
"""

from typing import Dict, List
from person import Person


def read_file(filename: str) -> List[str]:
    """
    Read text file and return its lines in a list.
    Do not return the first row, which is the header.
    It is assumed that tha file fits into a string.
    """
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()[1:]]


def parse_persons(lines: List[str]) -> Dict[str, Person]:
    found = {}

    for line in lines:
        contents = line.split(",")
        name, direction, timestamp = contents

        if name not in found.keys():
            found[name] = Person(name)

        person = found[name]
        person.add_event(direction, timestamp)

    return found


if __name__ == "__main__":
    input_lines = read_file("../input/datapao_homework_2023.csv")

    persons = parse_persons(input_lines)
