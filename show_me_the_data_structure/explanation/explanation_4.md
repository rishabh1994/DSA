Here groups can have multiple people added to it directly. A group can also have multipl groups added to it.
We need to find if user belongs to a particular group or not quickly.

We will basically first search the direct users of a group, followed by all recursive indirect users of a
group which are acquired by group addition.

Time Complexity : Worst case : O(n) where n are the total number of people in the group.
Space Complexity : O(1) because the 2 arrays storing users and groups are there as part of input itself.
                    We just iterate over existing arrays to get the count.