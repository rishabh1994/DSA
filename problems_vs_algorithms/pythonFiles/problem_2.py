def rotated_array_search(input_list, number):
    return binary_search(input_list, 0, len(input_list) - 1, number)


def binary_search(input_list, left, right, number):
    if left > right:
        return -1

    mid = (left + right) // 2
    if input_list[mid] == number:
        return mid

    if input_list[mid] < input_list[left]:

        if input_list[mid] <= number and number <= input_list[right]:
            return binary_search(input_list, mid + 1, right, number)
        else:
            return binary_search(input_list, left, mid - 1, number)

    else:
        if input_list[left] <= number and number <= input_list[mid]:
            return binary_search(input_list, left, mid - 1, number)
        else:
            return binary_search(input_list, mid + 1, right, number)


def first_test_case():
    # Empty list, expecting -1 for any element search.
    print(rotated_array_search([], 5))


def second_test_case():
    # Array still sorted in ascending order after rotating. That is full array sort of got rotated. We should get index 4 here.
    print(rotated_array_search([1, 2, 3, 4, 5], 5))


def third_test_case():
    # Array rotated. Should get index 0 for 6. Answer on the corner.
    print(rotated_array_search([6, 7, 1, 2, 3, 4, 5], 6))


def fourth_test_case():
    # Here 25 is no in the array. We should get -1.
    print(rotated_array_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 4, 5, 6, 7, 8, 9], 25))


first_test_case()
second_test_case()
third_test_case()
fourth_test_case()
