class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtTail(self, newNode):

        self.size += 1

        if self.head:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = newNode
            self.tail = newNode

    def removeHead(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            if self.head:
                self.head.prev = None
            return value
        return None

    def moveNodeToTail(self, node):
        if node and self.size > 1:
            if node == self.head:
                self.head = self.head.next
                self.head.prev = None
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = self.tail.next


class LRU_Cache(object):

    # Initialize class variables
    def __init__(self, capacity):
        self.doublyLinkedList = DoublyLinkedList()
        self.keyToAddress = dict()
        self.capacity = capacity
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.keyToAddress.get(key):
            node = self.keyToAddress.get(key)
            self.doublyLinkedList.moveNodeToTail(node)
            return self.keyToAddress.get(key).value
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        doublyLinkedListSize = self.doublyLinkedList.size
        if doublyLinkedListSize >= self.capacity:
            removedValue = self.doublyLinkedList.removeHead()
            self.keyToAddress.pop(removedValue)
        newNode = Node(value)
        self.doublyLinkedList.insertAtTail(newNode)
        self.keyToAddress[key] = newNode


def first_test_case():
    our_cache = LRU_Cache(5)
    print(our_cache.get(1))  # returns -1 because of empty cache.


def second_test_case():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(1))  # Cache size exceeded 5 with our last insert. So 1 was removed.


def third_test_case():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    print(our_cache.get(1))
    print(our_cache.get(2))
    print(our_cache.get(3))
    print(our_cache.get(4))
    print(our_cache.get(5))
    # Cache is full. However no eviction yet. When get performed on all 5 values, getting desired values.


first_test_case()
second_test_case()
third_test_case()
