"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
import re

with open("texts.csv", "r") as f, open("calls.csv", "r") as c:
    reader_texts = csv.reader(f)
    reader_calls = csv.reader(c)
    texts = list(reader_texts)
    calls = list(reader_calls)


call_list = {data[0] for data in calls}
call_receivers_list = {data[1] for data in calls}
message_senders_list = {data[0] for data in texts}
message_receivers_list = {data[1] for data in texts}

list_telemarketers = []

for call_telemarketer in call_list:
    if (
        call_telemarketer not in call_receivers_list
        and call_telemarketer not in message_senders_list
        and call_telemarketer not in message_receivers_list
    ):
        list_telemarketers.append(call_telemarketer)

list_telemarketers.sort()

print("These numbers could be telemarketers:")
for telemarketer in list_telemarketers:
    print(telemarketer)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
