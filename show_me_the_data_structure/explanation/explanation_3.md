Huffman encode and decode a string

First we create a lookup map of character to repeat count in string. Since this is just iterating over each charchter of
the string once, time complexity for this operation is O(n).

Then we take the map, and create a min heap or a priority queue from it. Inserts take O(logn) time to add a node here.
However the total unique keys possible in the map itself are 256. So this operation just takes constant time.

Now we create the tree from taking 2 min nodes and so on. Here also addition of 2 nodes is done in O(1) time. So total 
time complexity same as before.

Once tree is created, we assign 0 to left, 1 to right and so on assign value to each leaf. Again just iterating the tree.
So O(n).

Now we can easily create lookup map of character to binaryCode and use that to encode the string. 

Time complexity : O(n)
Space complexity : For min heaps, trees and maps : O(n)