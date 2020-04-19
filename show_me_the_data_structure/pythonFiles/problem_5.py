import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:

    def __init__(self):
        self.lastBlock = None

    def addBlock(self, data):
        if self.lastBlock:
            previous_hash = self.lastBlock
        else:
            previous_hash = None
        block = Block(datetime.time, data, previous_hash)
        self.lastBlock = block


def first_test_case():
    linkedList = LinkedList()
    linkedList.addBlock("ABCD")
    # Added node with value ABCD. That should be the value below.
    print(linkedList.lastBlock.data)


def second_test_case():
    linkedList = LinkedList()
    linkedList.addBlock("ABCD")
    linkedList.addBlock("EFGH")
    print(linkedList.lastBlock.data)
    # Use previous hash to go the node with ABCD data and print that.
    print(linkedList.lastBlock.previous_hash.data)


def third_test_case():
    linkedList = LinkedList()
    if not linkedList.lastBlock:
        # As expected, with no addition last node will be None.
        pass


first_test_case()
second_test_case()
third_test_case()
