def getLookupMap(input_list):
    digitToCount = dict()
    for digit in input_list:
        if digit in digitToCount.keys():
            digitToCount[digit] += 1
        else:
            digitToCount[digit] = 1
    return digitToCount


def getSortedList(digitToCount):
    sortedList = []
    for digit in range(0, 10):
        if digit in digitToCount.keys():
            for j in range(0, digitToCount[digit]):
                sortedList.append(digit)
    return sortedList


def rearrange_digits(input_list):
    digitToCount = getLookupMap(input_list)
    sortedList = getSortedList(digitToCount)

    firstNumber = 0
    secondNumber = 0
    position = len(input_list) - 1
    while position >= 0:
        if position % 2:
            firstNumber = firstNumber * 10 + sortedList[position]
        else:
            secondNumber = secondNumber * 10 + sortedList[position]
        position -= 1
    return firstNumber, secondNumber


def first_test_case():
    # Empty input given. Expected output 0,0.
    firstNumber, secondNumber = rearrange_digits([])
    print(firstNumber, secondNumber)


def second_test_case():
    # Even length test case : Expected output 1111, 1111
    firstNumber, secondNumber = rearrange_digits([1, 1, 1, 1, 1, 1, 1, 1])
    print(firstNumber, secondNumber)


def third_test_case():
    # Odd length test case : Expected output 1111, 11111
    firstNumber, secondNumber = rearrange_digits([1, 1, 1, 1, 1, 1, 1, 1, 1])
    print(firstNumber, secondNumber)


def fourth_test_case():
    # Single length array. Expected output 0 and 5.
    firstNumber, secondNumber = rearrange_digits([5])
    print(firstNumber, secondNumber)


def fifth_test_case():
    # 1 to 9 repeated twice. Expected output 987654321 twice.
    firstNumber, secondNumber = rearrange_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(firstNumber, secondNumber)


first_test_case()
second_test_case()
third_test_case()
fourth_test_case()
fifth_test_case()
