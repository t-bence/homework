"""
This is my solution to the homework task.
It was developed for Python 3.9.1 using the standard library.
"""

from typing import Dict, List
from person import Person

def read_file(filename: str) -> str:
    """ Read text file and return its lines in a list."""
    with open(filename, "r") as file:
        return file.readlines()


def parse_persons(input: List[str]) -> Dict[str, Person]:
    pass


if __name__ == "__main__":
    input_lines = read_file("../input/datapao_homework_2023.csv")

    persons = parse_persons(input_lines)