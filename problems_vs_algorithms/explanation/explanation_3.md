PROBLEM
Given input array from 0, 9 create 2 numbers of almost similar length with max sum.

APPROACH
So lets say input length is 6, then we know we need to create 2 numbers of length 3. Lets say the two numbers are A and B

A = xyz = 100x  + 10y +z
B = def = 100d + 10e + f

Idea is to maximize the sum from input digits. So we sort the input array and greedily pick the max values and assign them
to x,d,y,e,z and f in that order.

TIME COMPLEXITY
Sorting takes O(n) time here. Because we know the input values are from 0 to 9 only. So we can use a counting sort to sort the input list
in linear time. After that we just pick and assign alternate values from right to left to the 2 numbers.
So total time complexity is O(N) where N is the number of elements in the array.

SPACE COMPLEXITY
O(1) : Even though we are using a map to sort here, but we know the map's size is always 10 in the worst case which is
a constant as there are only 10 digits from 0, 9 in the input.
