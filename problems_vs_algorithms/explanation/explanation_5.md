PROBLEM
Find all suffixes of a word in input list.

APPROACH
We build trie of all the words in the input list. We add the elements one by one. Now lets say we want to find suffix for the 
string "EXAMPLE".

We try to search if "EXAMPLE" is there in trie or not. If not, we return None. If it is present, we iterate till that trieNode.
From there on, we need to recursively visit every node and append the parents character. If the boolean isWord is true,
then we add the string formed till here to the output list. 

TIME COMPLEXITY
Since in worst case, we might have to find prefixes of '' that is every element in the trie, so we will be visiting each trieNode
once in this case. So worst case is O(W*L) where W is the number of words in the list and L is the average length of the words.

SPACE COMPLEXITY
O(W*L) where W is the number of words in the list and L is the average length of the words for creating the trie.
