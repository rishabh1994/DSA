PROBLEM
Sort an array of 0's,1's and 2's in a single iteration.

APPROACH
Since we know that input just has 0's, 1's and 2's. We know output has to be all 0's followed by 1's and 2's.
So we basically divide the array into 4 segments:

1) All 0s.
2) All 1s
3) Unknown
4) All 2's

Now we slowly iterate over each element in the unknown area : if it is a 2, we put it at end with all 2's. If it is a 0,
we put it at start. Else we just increment the 1's area.

TIME COMPLEXITY
Since we are doing a single pass over each element only once, time complexity is linear that is O(N) where N is the number
of elements in the array.

SPACE COMPLEXITY
We are not using any storage here. So space complexity is constant that is O(1).