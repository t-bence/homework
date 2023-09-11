"""
This is my solution to the homework task.
It was developed for Python 3.9.1 using the standard library.
"""

from typing import List, Tuple
from homework.person import Person, Stat


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


def print_stats(stats: List[Stat]) -> None:
    """Write the solution of the first task to file"""
    line_end = "\n"
    lines = ["user_id,time,days,average_per_day,rank" + line_end]  # header

    for rank, data in enumerate(stats):
        rank_as_str = str(rank + 1)  # start from 1
        line = str(data) + "," + rank_as_str + line_end
        lines.append(line)

    with open("output/first.csv", "w") as file:
        file.writelines(lines)


def print_longest_session(name: str, session_length: float) -> None:
    """Write the solution of the second task to file"""
    lines = ["user_id,session_length\n",  # header
             f"{name},{session_length}\n"]  # content

    with open("output/second.csv", "w") as file:
        file.writelines(lines)


def compute_break_lengths(persons: List[Person]) -> Tuple[float, float]:
    """Compute average lunch break and non-lunch break lengths"""
    lunch_breaks: List[float] = []
    non_lunch_breaks: List[float] = []
    for p in persons:
        lb, nlb = p.get_break_lengths()
        lunch_breaks += lb
        non_lunch_breaks += nlb

    def avg(lst: List[float]) -> float:
        return sum(lst) / len(lst)

    return avg(lunch_breaks), avg(non_lunch_breaks)


def main() -> None:
    # noinspection SpellCheckingInspection
    input_lines = read_file("input/datapao_homework_2023.csv")

    # parse persons and events from text file
    persons = parse_persons(input_lines)

    print(f"Processing {len(persons)} persons")

    february = 2

    # compute statistics for February
    february_stats = [person.get_stats_for_month(february)
                      for person in persons]
    # sort by decreasing avg hours per day
    february_stats.sort(key=lambda s: s.avg_time_per_days, reverse=True)

    # print February stats to file
    print_stats(february_stats)

    # compute longest session
    sessions = [(person.name, person.get_longest_session_hours(february))
                for person in persons]

    # sort by decreasing session length
    sessions.sort(key=lambda x: x[1], reverse=True)
    user_id, length = sessions[0]

    # write second solution to file
    print_longest_session(user_id, length)

    # my idea: compute lunch break and non-lunch break lengths
    lunch_breaks, non_lunch_breaks = compute_break_lengths(persons)
    print(f"Average lunch break length: {lunch_breaks:.2f} hours")
    print(f"Average non-lunch break length: {non_lunch_breaks:.2f} hours")

    print("Done.")


if __name__ == "__main__":
    main()
