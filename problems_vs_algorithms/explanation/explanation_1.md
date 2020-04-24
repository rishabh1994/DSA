PROBLEM 
Find square root of a number rounded off to floor integer in O(logn) time.

APPROACH
So when we see the time complexity required being O(logn), we get the hint that we need to use something like binary
search here. So we realize that square root of number can never be more than the number itself. This gives us the lowerbound
as 1 and upperbound as the number itself.

Now we check the mid, if it is the square root, return it. Else depending on the value of mid, we iterate over the left
or right part to find the square root.

TIME COMPLEXITY
Since we are always reducing the range by half in every iteration of the run, there are O(logn) steps.
Also in each step, we are merely calculating the square of number and doing few fixed number of constant comparisons that is
time taken is O(1). So total time complexity is O(logn) where n is the number of elements in the input list.

SPACE COMPLEXITY
Since we are not using any additional storage to hold any state, space complexity is constant that is O(1).