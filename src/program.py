"""
This is my solution to the homework task.
It was developed for Python 3.9.1 using the standard library.
"""

from typing import List, Tuple
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

    return list(found.values())


def print_stats(stats: List[Tuple[str, float, int, float]]) -> None:
    """Write the solution of the first task to file"""
    line_end = "\n"
    lines = ["user_id,time,days,average_per_day,rank" + line_end]  # header

    for rank, data in enumerate(stats):
        data_as_strings = map(str, data)
        rank_as_str = str(rank + 1)  # start from 1
        line = ",".join((*data_as_strings, rank_as_str)) + line_end
        lines.append(line)

    with open("../output/first.csv", "w") as file:
        file.writelines(lines)


def print_longest_session(name: str, session_length: float) -> None:
    """Write the solution of the second task to file"""
    lines = ["user_id,session_length\n",  # header
             f"{name},{session_length}"]  # content

    with open("../output/second.csv", "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    input_lines = read_file("../input/datapao_homework_2023.csv")

    # parse persons and events from text file
    persons = parse_persons(input_lines)

    february = 2

    # compute statistics for February
    february_stats = [person.get_stats_for_month(february)
                      for person in persons]
    february_stats.sort(key=lambda x: x[3], reverse=True)

    # print February stats to file
    print_stats(february_stats)

    # compute longest session
    sessions = [(person.name, person.get_longest_session_hours(february))
                for person in persons]

    # sort be decreasing session length
    sessions.sort(key=lambda x: x[1], reverse=True)
    user_id, length = sessions[0]

    print_longest_session(user_id, length)
