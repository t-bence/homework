"""
This is my solution to the homework task.
It was developed for Python 3.9.1 using the standard library.
"""

from typing import Dict, List, Tuple
from person import Person


def read_file(filename: str) -> List[str]:
    """
    Read text file and return its lines in a list.
    Do not return the first row, which is the header.
    It is assumed that tha file fits into a string.
    """
    with open(filename, "r") as file:
        return file.readlines()[1:]


def parse_persons(lines: List[str]) -> List[Person]:
    found = {}

    for line in lines:
        contents = line.strip().split(",")
        name, direction, timestamp = contents

        if name not in found.keys():
            found[name] = Person(name)

        found[name].add_event(direction, timestamp)

    return found.values()


def print_stats(stats: List[Tuple[str, float, int, float]], filename: str) -> None:
    """Write the solution of the first task to file"""
    line_end = "\n"
    lines = ["user_id,time,days,average_per_day,rank" + line_end]  # header

    for rank, data in enumerate(stats):
        line = ",".join((*map(str, data), str(rank + 1))) + line_end
        lines.append(line)

    with open(filename, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    input_lines = read_file("../input/datapao_homework_2023.csv")

    # parse persons and events from text file
    persons = parse_persons(input_lines)

    print(f"Read {len(persons)} persons")

    february = 2

    # compute statistics for February
    february_stats = [person.get_stats_for_month(february)
                      for person in persons]
    february_stats.sort(key=lambda x: x[3], reverse=True)

    # print February stats to file
    print_stats(february_stats, "../output/first.csv")

    # compute longest session
    sessions = [(person.name, person.get_longest_session_hours(february))
                for person in persons]

    sessions.sort(key=lambda x: x[1], reverse=True)

    print(sessions[0])