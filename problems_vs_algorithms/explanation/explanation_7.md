PROBLEM
Map a handler to a path using Trie

APPROACH
We take the input path, split it by "/". We get a list of words. We insert the full word in a trie. In addition to normal
trie implementation, we also have a handlerName as part of the trieNode. handlerName will only be populated for the last word
in the list (after splitting by "/"). With regards to  data structure to be used, trie seems to be one of the good data
structure to implement it. Other than this, we could have also used a hashMap to do the same. 

To find a handler name corresponding to a path, we simply split the path by "/" and traverse each word one by one if it exists in the
trie. Then we return the handler name associated with that node. Also to handle the extra "/" at the end, we search for the answer
by removing the trailing "/" if we don't get the answer in the first iteration.

TIME COMPLEXITY
O(N) where N is the number of words in the list after splitting by "/".

SPACE COMPLEXITY
O(W*L) where W is the number of words in the list and L is the average length of the words for creating the trie.
