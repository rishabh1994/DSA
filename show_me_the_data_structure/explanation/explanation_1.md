Here we are using a doubly linked list with quick lookup for arbitrary index in list using a map. The idea is that the 
head of the list should be the LRU node and the tail of the list should be MSU node. 

Whenever a get operation is done and its a cache hit, we remove that node from that position and insert at the tail.

Time Complexity : Since we store the lookup addresses in map as well, the above all operations are possible in O(1).
Space Complexity : Linked List and the lookup map for fast access are the additional data structures used. They both have
O(n) space complexity where n is the size of the cache.____