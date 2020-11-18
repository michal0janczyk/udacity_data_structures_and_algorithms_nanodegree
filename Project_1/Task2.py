"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f, open("calls.csv", "r") as c:
    reader_texts = csv.reader(f)
    reader_calls = csv.reader(c)
    texts = list(reader_texts)
    calls = list(reader_calls)

rec_dict = {}
for call in calls:
    if call[1] not in rec_dict:
        rec_dict.update({call[1]: int(call[3])})
    else:
        rec_dict[call[1]] += int(call[3])

    if call[0] not in rec_dict:
        rec_dict.update({call[0]: int(call[3])})
    else:
        rec_dict[call[0]] += int(call[3])

longest_duration = max(rec_dict.items(), key=lambda x: x[1])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*longest_duration))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
