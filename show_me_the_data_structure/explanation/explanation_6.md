Get union and intersection of 2 linked lists.

Iterated the linked list to convert it to a map with key as key of linked list and value as the repeat counts. Using
the lookup map, easily derive the union and the intersection of the list.

Union Time Complexity : Lets assume linked lists are of size n1 and n2. For calculating union, we are iterating over each
                        element of the linked list once and updating the lookup map with the frequency. So time involved
                        here would be O(n1+n2). After this we just create a new list with all the keys in the map.
                        So overall time complexity is sum of all the nodes in both the list               

Union Space Complexity : Here we are creating an extra data structure map for keeping track of the keys and counts to remove
                         duplicates in the final answer. So Space complexity is O(n1+n2) where n1 and n2 are the number of
                         nodes in the linked list.   
Intersection Time complexity and space complexity is also same as the union time complexity. Only extra operation that
we do here is check if the key of 1 map also exists in another map. Since lookups in map are O(1), so this does not change 
the time complexity.