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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def fetchParticularRecord(inputList, indexNumber):
    sizeOfList = len(inputList)
    if(sizeOfList>0 and sizeOfList>indexNumber):
        return inputList[indexNumber]
    return None


firstTextRecord = fetchParticularRecord(texts, 0)
lastCallRecord = fetchParticularRecord(calls, len(calls)-1)

if firstTextRecord is not None:
    incomingNumberForText, answeringNumberForText, timeForText=firstTextRecord
    print(F"First record of texts, {incomingNumberForText} texts {answeringNumberForText} at time {timeForText}")

if lastCallRecord is not None:
    incomingNumberForCall, answeringNumberForCall, timeForCall, durationInSeconds=lastCallRecord
    print(F"Last record of calls, {incomingNumberForCall} calls {answeringNumberForCall} at time {timeForCall}, lasting {durationInSeconds} seconds")