Get union and intersection of 2 linked lists.

Iterated the linked list to convert it to a map with key as key of linked list and value as the repeat counts. Using
the lookup map, easily derive the union and the intersection of the list.

Time Complexity : O(n) since we need to iterate over each element of linked list once to put in the map. Afterwords, the 
                    map complexities involved are all O(1)
Space Complexity : O(n) for the map