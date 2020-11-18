"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


def extract_area_code(call_list):
    area_codes = call_list[1]

    if area_codes[:2] == "(0":
        return area_codes.split(sep=")")[0] + ")"
    if area_codes.startswith("140"):
        return area_codes[:3]
    else:
        return area_codes[:4]


"""
Allowed bangalore_call_prefix to contain duplicate area codes
That way, each entry represents a phone call, so the number
of entries is same as the number of calls made from a (080) to any number
"""

bangalore_call_prefix = [
    extract_area_code(call) for call in calls if call[0][0:5] == "(080)"
]

"""
 Removed the sorting here
"""
bangalore_call_prefix_count = bangalore_call_prefix.count("(080)")

print("The numbers called by people in Bangalore have codes:")
"""
Used casting to a set then sorting here, so that I can use
bangalore_call_prefix with no problems for percentage
"""
for prefix in sorted(set(bangalore_call_prefix)):
    print(prefix)

print(
    round(bangalore_call_prefix_count / len(bangalore_call_prefix) * 100, 2),
    "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.",
)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
