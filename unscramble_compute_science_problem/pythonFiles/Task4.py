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


def getNumbersWithAtleastOneOutgoingCall(calls):
    numbersWithAtleastOneOutgoingCall = set()
    for record in calls:
        callingNumber, receivingNumber, startTimestamp, duration = record
        numbersWithAtleastOneOutgoingCall.add(callingNumber)

    return numbersWithAtleastOneOutgoingCall


def getNumbersWithAtleastOneIncomingCall(calls):
    numbersWithAtleastOneIncomingCall = set()
    for record in calls:
        callingNumber, receivingNumber, startTimestamp, duration = record
        numbersWithAtleastOneIncomingCall.add(receivingNumber)

    return numbersWithAtleastOneIncomingCall


def getNumbersWithAtleastOneOutgoingText(texts):
    numbersWithAtleastOneOutgoingText = set()
    for record in texts:
        sendingNumber, receivingNumber, timestamp = record
        numbersWithAtleastOneOutgoingText.add(sendingNumber)

    return numbersWithAtleastOneOutgoingText


def getNumbersWithAtleastOneIncomingText(texts):
    numbersWithAtleastOneIncomingText = set()
    for record in texts:
        sendingNumber, receivingNumber, timestamp = record
        numbersWithAtleastOneIncomingText.add(receivingNumber)

    return numbersWithAtleastOneIncomingText


def getTelephoneMarketingNumbers(texts, calls):
    numbersWithAtleastOneOutgoingCall = getNumbersWithAtleastOneOutgoingCall(calls)
    numbersWithAtleastOneIncomingCall = getNumbersWithAtleastOneIncomingCall(calls)
    numbersWithAtleastOneOutgoingText = getNumbersWithAtleastOneOutgoingText(texts)
    numbersWithAtleastOneIncomingText = getNumbersWithAtleastOneIncomingText(texts)

    nonTelephoneMarketingNumbers = numbersWithAtleastOneIncomingCall.union(numbersWithAtleastOneOutgoingText,
                                                                          numbersWithAtleastOneIncomingText)

    return sorted(numbersWithAtleastOneOutgoingCall.difference(nonTelephoneMarketingNumbers))


marketingNumbers = getTelephoneMarketingNumbers(texts, calls)

print("These numbers could be telemarketers: ")
for number in marketingNumbers:
    print(number)
