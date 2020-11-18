"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f, open("calls.csv", "r") as c:
    reader_texts = csv.reader(f)
    reader_calls = csv.reader(c)
    texts = list(reader_texts)
    calls = list(reader_calls)

numbers = set()
for row in texts:
    numbers.add(row[0])
    numbers.add(row[1])

for row in calls:
    numbers.add(row[0])
    numbers.add(row[1])

print(
    "There are",
    len(numbers),
    "different telephone numbers in the records.",
)

print(
    "There are",
    len(first_col) + len(second_col),
    "different telephone numbers in the records.",
)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
