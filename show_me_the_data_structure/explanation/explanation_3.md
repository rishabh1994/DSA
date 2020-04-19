Huffman encode and decode a string

First we create a lookup map of character to repeat count in string. Since this is just iterating over each character of
the string once, time complexity for this operation is O(n) where n is the total number of characters in the input string.

Then we take the map, and create a min heap or a priority queue from it. Inserts take O(logn) time to add a node here.
Now assuming there are k keys in the map above that is k unique characters, we will need to do insert operation k times so 
total time complexity here : O(klogn)

Now we create the tree from taking 2 min nodes and so on. Here also addition of 2 nodes is done in O(1) time. So we have k nodes
in the tree. So we might have to do this operation k times. Time complexity to do this O(K)

Once tree is created, we assign 0 to left, 1 to right and so on assign value to each leaf. Again just iterating the tree.
So O(K) where k are the total nodes in the tree.

Now we can easily create lookup map of character to binaryCode and use that to encode the string. 

Time complexity : O(N) + O(klogk) where k unique characters are there in the string and string length is N.
                  However the max value of k can be only 256. So O(N) is the final time complexity with N being the 
                  string length.
Space complexity : For min heaps, trees and maps : O(N) where N is the total string length.