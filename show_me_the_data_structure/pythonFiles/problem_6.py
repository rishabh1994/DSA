class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    keyToCount = {}
    updateLookupMap(llist_1, keyToCount)
    updateLookupMap(llist_2, keyToCount)

    unionList = []
    for key in keyToCount:
        unionList.append(key)

    return unionList


def intersection(llist_1, llist_2):
    firstKeyToCount = {}
    updateLookupMap(llist_1, firstKeyToCount)

    secondKeyToCount = {}
    updateLookupMap(llist_2, secondKeyToCount)

    intersectionList = []
    for key in firstKeyToCount.keys():
        if secondKeyToCount.get(key):
            intersectionList.append(key)
    return intersectionList

def updateLookupMap(list, keyToCount):
    currentNode = list.head

    while currentNode:
        value = currentNode.value
        if value in keyToCount.keys():
            keyToCount[value] += 1
        else:
            keyToCount[value] = 1
        currentNode = currentNode.next


def first_test_case():

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    # Here one of the list is empty. So union would be same as list element_2 and intersection will be empty.
    element_1 = []
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


def second_test_case():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    # Both lists are empty. So union and intersection are also empty.
    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


def third_test_case():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    # Union and intersection of same list with itself will be the same list
    element_1 = [1,2,3,4]
    element_2 = [1,2,3,4]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


first_test_case()
second_test_case()
third_test_case()