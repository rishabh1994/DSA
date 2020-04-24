import queue


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, char):
        if char not in self.children.keys():
            self.children[char] = TrieNode()


class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insert(self, word):
        pointer = self.rootNode
        for char in word:
            if char not in pointer.children.keys():
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.isWord = True

    def find(self, prefix):
        pointer = self.rootNode
        for char in prefix:
            if char not in pointer.children.keys():
                return False
            pointer = pointer.children[char]
        return pointer.isWord

    def suffixes(self, suffix=''):
        pointer = self.rootNode
        for char in suffix:
            if char not in pointer.children.keys():
                return None
            pointer = pointer.children[char]
        listOfSuffixes = []
        if len(pointer.children.keys()) == 0:
            return None
        self.getListOfSuffixes(pointer, "", listOfSuffixes)
        return listOfSuffixes

    def getListOfSuffixes(self, pointer, suffixTillNow, listOfSuffixes):
        for child in pointer.children.keys():
            if pointer.children[child].isWord:
                listOfSuffixes.append(suffixTillNow+child)
            self.getListOfSuffixes(pointer.children[child], suffixTillNow + child, listOfSuffixes)


def first_test_case():
    # So here we have added 10 strings to the trie. We search for all sufixes with string ''. So we should get all 10 strings as answer.
    word_list = ['apple', 'bear', 'goo', 'goos', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
    word_trie = Trie()
    for word in word_list:
        word_trie.insert(word)
    print(word_trie.suffixes(''))

def second_test_case():
    # So here we have added 10 strings to the trie. We search for all sufixes with string 'X'. But there is no string beginning with X. We should get None.
    word_list = ['apple', 'bear', 'goo', 'goos', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
    word_trie = Trie()
    for word in word_list:
        word_trie.insert(word)
    print(word_trie.suffixes('X'))

def third_test_case():
    # We are creating an empty trie and searching for suffixes with empty string. Should get None
    word_list = []
    word_trie = Trie()
    for word in word_list:
        word_trie.insert(word)
    print(word_trie.suffixes(''))

def fourth_test_case():
    # So here we have added 10 strings to the trie. We search for all sufixes with string 'goo'. We get the appropriate 6 elements in the list.
    word_list = ['apple', 'bear', 'goo', 'goos', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
    word_trie = Trie()
    for word in word_list:
        word_trie.insert(word)
    print(word_trie.suffixes('goo'))


first_test_case()
second_test_case()
third_test_case()
fourth_test_case()