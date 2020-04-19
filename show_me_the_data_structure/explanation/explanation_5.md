Here since the field previous_hash is there which holds the hash of the previous Block, it points us to using towards a 
linked list. Also linked list will be normal singular linked list and not doubly linked list. Since it does not store the
next_hash.


Time complexity : O(1) since adding a node to end of linked list is O(1) where tail pointer is maintained. To go to prev node, we can just use 
the prev_hash field.
Space Complexity : O(N) for n nodes in a linked list.