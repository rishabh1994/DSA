def sort_012(input_list):
    left = 0
    mid = 0
    right = len(input_list) - 1

    while mid <= right:

        element = input_list[mid]

        if element == 0:
            swap(input_list, left, mid)
            left += 1
            mid += 1
        elif element == 1:
            mid += 1
        elif element == 2:
            swap(input_list, mid, right)
            right -= 1
            pass
        else:
            print("INVALID INPUT")
            return

    return input_list


def swap(input_list, firtIndex, secondIndex):
    temp = input_list[firtIndex]
    input_list[firtIndex] = input_list[secondIndex]
    input_list[secondIndex] = temp


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


def first_test_case():
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


def second_test_case():
    # Empty array, even after sorting will remain empty.
    test_function([])


def third_test_case():
    # Array with only 0's/1's/2's. Again the answer will be same.
    test_function([0, 0, 0, 0, 0, 0])
    test_function([1, 1, 1, 1, 1, 1])
    test_function([2, 2, 2, 2, 2, 2])


def fourth_tese_case():
    # Array with alternating pattern of 0,1,2. Again answer will be all 0s' followed by 1's and 2's.
    test_function([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])


def fifth_tetst_case():
    # Return empty Array. Invalid input. Input only supposed to have 0,1,2.
    test_function([0, 1, 2, 3, 4, 5])


first_test_case()
second_test_case()
third_test_case()
fourth_tese_case()
fifth_tetst_case()
