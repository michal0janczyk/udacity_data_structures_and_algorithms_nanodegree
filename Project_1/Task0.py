"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open("texts.csv", "r") as f:
    first_line_texts = f.readline()
    print(
        "First record of texts",
        first_line_texts.split(",", 2)[0],
        "texts",
        first_line_texts.split(",", 2)[1],
        "at time",
        first_line_texts.split(",", 2)[2],
    )

with open("calls.csv", "r") as c:
    last_line_calls = c.readlines()[-1]
    print(
        "Last record of calls",
        last_line_calls.split(",", 3)[0],
        "calls",
        last_line_calls.split(",", 3)[1],
        "at time",
        last_line_calls.split(",", 3)[2],
        ", lasting",
        last_line_calls.split(",", 3)[3],
        "seconds",
    )

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
