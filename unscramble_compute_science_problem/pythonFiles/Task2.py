"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def getTelephoneNumberToTimeSpent(calls):
    telephoneNumberToTimeSpent = {}
    for record in calls:
        callingNumber, receivingNumber, startTimestamp, duration = record
        for telephoneNumber in (callingNumber, receivingNumber):
            if telephoneNumber in telephoneNumberToTimeSpent.keys():
                telephoneNumberToTimeSpent[telephoneNumber] += int(duration)
            else:
                telephoneNumberToTimeSpent[telephoneNumber] = int(duration)

    return telephoneNumberToTimeSpent


mobileNumberToTimeSpent = getTelephoneNumberToTimeSpent(calls)
mobileNumberWithMaxTimeSpent = max(mobileNumberToTimeSpent, key=mobileNumberToTimeSpent.get)
maxTimeSpent = mobileNumberToTimeSpent.get(mobileNumberWithMaxTimeSpent)

print(F"{mobileNumberWithMaxTimeSpent} spent the longest time, {maxTimeSpent} "
      F"seconds, on the phone during September 2016.")
