# homework
Hi, my name is Bence. This is my solution of the homework.

During the solution, I have made some assumptions: 
1. I assumed that if someone enters the office on
Monday at 23:00 and leaves on Tuesday at 1:00
(at night), then it counts as one hour on Monday
and one hour on Tuesday.
2. I have assumed that between entering and leaving, 
cannot be more time than a day. This is important,
otherwise we could have stays reaching to 3 days.
This is checked and a ValueError is thrown if the
assumption is violated.
3. I assume that both input and output files are small,
as in the example, so I can read them into memory as
strings. If the files were bigger, I would read and
write them line by line.

Thanks for the assignment, I really enjoyed it and learned
some new things as well!

## Run the program

The program should be ran on **Python 3.9**.
It was developed and tested in PyCharm  
on a Windows machine (but that should not matter).

1. Clone the repo
2. Enter the external homework folder: `cd homework`
3. Run the program: `python -m homework`

## Run the unit tests

From the same place, the external homework folder:
`python -m unittest -v`
