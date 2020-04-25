def get_min_max(input_list):
    if input_list:
        minimumElement = input_list[0]
        maximumElement = input_list[0]
        for i in range(1, len(input_list)):
            if input_list[i] < minimumElement:
                minimumElement = input_list[i]
            if input_list[i] > maximumElement:
                maximumElement = input_list[i]
        return minimumElement, maximumElement

    return None, None


def first_test_case():
    # Empty list. So min and max are both None as there is no element in the list.
    input_list = []
    print(get_min_max((input_list)))


def second_test_case():
    # Input list with only 1 element. So min and max is the same element.
    input_list = [5]
    print(get_min_max(input_list))


def third_test_case():
    # Input list with order both ascending and descending from numbers from 1,9. Answer being 1 and 9.
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(get_min_max(input_list))
    input_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(get_min_max(input_list))


def fourth_test_case():
    # Input list with 10000 elements from 1 to 10000. So min is 1 and max is 10000.
    input_list = []
    for i in range(1, 10001):
        input_list.append(i)

    print(get_min_max(input_list))


first_test_case()
second_test_case()
third_test_case()
fourth_test_case()
