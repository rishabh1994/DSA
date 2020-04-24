def sqrt(number):
    if number < 0:
        return -1

    if number <= 1:
        return number

    return sqrtHelper(0, number - 1, number)


def sqrtHelper(start, end, number):
    mid = (start + end) // 2
    square = mid * mid
    nextSquare = (mid + 1) * (mid + 1)
    if square == number or (square < number and number < nextSquare):
        return mid
    elif square < number:
        return sqrtHelper(mid + 1, end, number)
    else:
        return sqrtHelper(start, mid - 1, number)


def first_test_case():
    assert sqrt(-200) == -1, "Negative values not allowed"


def second_test_case():
    assert sqrt(0) == 0, "Square root of 0 is 0"
    assert sqrt(1) == 1, "Square root of 1 is 1"


def third_test_case():
    assert sqrt(100000000) == 10000, "Square root of 100000000 is 10000"


first_test_case()
second_test_case()
third_test_case()
