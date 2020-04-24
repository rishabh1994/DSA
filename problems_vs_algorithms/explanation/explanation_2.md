PROBLEM 
Search for an element in sorted rotaten array.

APPROACH
Since we need to find the answer in O(logn) time, we need to use binary search as any sorting or other algorithm will need
to itearte over all elements atleast once. So normal binary search only works if array is sorted. However, here we have 
rotated the array. We need to modify the binary search algorithm a little bit to make it work here.

We know that after rotation, there will just be 1 element whose next index's value will be less than its own value. Using this fact,
we can calculate mid and compare its value and decide on which half of the array, we want to proceed. 


TIME COMPLEXITY
O(logn) where n is the total elements in the array. Since we are dividing the total array into 2 equal parts by calculating mid and
doing comparisons with value of mid. After that, we decide if we want to iterate on the left part or right part of mid. We choose only
one side. So size of array is always reduced by half. So time complexity : O(logn)

SPACE COMPLEXITY
Since we are not using any additional storage to hold any state, space complexity is constant that is O(1).