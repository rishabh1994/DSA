from queue import PriorityQueue
import sys


class Node:
    def __init__(self, character, count):
        self.character = character
        self.count = count
        self.left = None
        self.right = None
        self.binaryCode = None

    def __lt__(self, other):
        return self.count <= other.count


def updateCharacterToBinaryCodeMap(node, characterToBinaryCodeMap):
    if node:
        if not node.character == 'nonLeafNode':
            characterToBinaryCodeMap[node.character] = node.binaryCode
        updateCharacterToBinaryCodeMap(node.left, characterToBinaryCodeMap)
        updateCharacterToBinaryCodeMap(node.right, characterToBinaryCodeMap)


def addNodes(node1, node2):
    if node1 and node2:
        updatedCount = node1.count + node2.count
    elif node1:
        updatedCount = node1.count
    elif node2:
        updatedCount = node2.count
    else:
        return None
    node3 = Node('nonLeafNode', updatedCount)
    node3.left = node1
    node3.right = node2
    return node3


def constructTree(priorityQueue):
    while priorityQueue.qsize():
        firstNode = priorityQueue.get()
        if firstNode.character == 'nonLeafNode' and priorityQueue.qsize() == 0:
            return firstNode

        if priorityQueue.qsize() == 0:
            secondNode = None
        else:
            secondNode = priorityQueue.get()
        combinedNode = addNodes(firstNode, secondNode)
        priorityQueue.put(combinedNode)


def constuctPriorityQueue(inputString):
    characterToCount = dict()
    for char in inputString:
        if char in characterToCount.keys():
            characterToCount[char] += 1
        else:
            characterToCount[char] = 1

    priorityQueue = PriorityQueue()
    for character in characterToCount.keys():
        count = characterToCount[character]
        priorityQueue.put(Node(character, count))
    return priorityQueue


def updateBinaryCode(rootNode):
    if rootNode:
        if rootNode.left:
            updateBinaryCodeHelper(rootNode.left, "0")
        if rootNode.right:
            updateBinaryCodeHelper(rootNode.right, "1")


def updateBinaryCodeHelper(node, parentCode):
    tempNode = node
    if tempNode:
        tempNode.binaryCode = parentCode
        if tempNode.left:
            updateBinaryCodeHelper(tempNode.left, parentCode + "0")
        if tempNode.right:
            updateBinaryCodeHelper(tempNode.right, parentCode + "1")


def huffman_encoding(data):
    queue = constuctPriorityQueue(data)
    rootNode = constructTree(queue)
    updateBinaryCode(rootNode)
    characterToBinaryCodeMap = dict()
    updateCharacterToBinaryCodeMap(rootNode, characterToBinaryCodeMap)

    huffmanEncodedData = ""
    for charcter in data:
        huffmanEncodedData += characterToBinaryCodeMap[charcter]
    return huffmanEncodedData, rootNode


def huffman_decoding(data, rootNode):
    updateBinaryCode(rootNode)
    characterToBinaryCodeMap = dict()
    updateCharacterToBinaryCodeMap(rootNode, characterToBinaryCodeMap)
    newLookupMap = dict()
    for character in characterToBinaryCodeMap:
        binaryCode = characterToBinaryCodeMap[character]
        newLookupMap[binaryCode] = character
        newLookupMap[character] = binaryCode

    decodedString = ''
    combinedCharacter = ''
    for character in data:
        combinedCharacter += character
        if combinedCharacter in newLookupMap.keys():
            decodedString += newLookupMap[combinedCharacter]
            combinedCharacter = ''

    return decodedString


def test_case(a_great_sentence):
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


def empty_string_test_case():
    input = ""
    encoded_data, tree = huffman_encoding(input)
    print(encoded_data)
    # Since our input string is "" that is empty string. Our ouput string is also "". And we compare both below and True is printed.
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data == input)


if __name__ == "__main__":
    test_case("The bird is the word")
    # Test with same character. Here since just 1 character is there. We will just assign it 0 bit and the answer
    # would be the number of times this character occurs in the string which is 15 here. So answer will be 15 0's.
    test_case("AAAAAAAAAAAAAAA")
    test_case("AAAABBBBCCCCDDDD")
