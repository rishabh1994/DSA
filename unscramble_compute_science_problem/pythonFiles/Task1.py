"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def getUniqueMobileNumbers(calls):
    uniqueMobileNumbers = set()

    for dataSet in [texts, calls]:
        for inputRow in dataSet:
            for column in range(2):
                mobileNumber = inputRow[column]
                uniqueMobileNumbers.add(mobileNumber)

    return uniqueMobileNumbers


uniqueMobileNumbers = getUniqueMobileNumbers(calls)
print(F"There are {len(uniqueMobileNumbers)} different telephone numbers in the records.")
