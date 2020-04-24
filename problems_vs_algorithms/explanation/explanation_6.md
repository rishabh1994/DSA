PROBLEM
Find the minimum and maximum element in the input list in linear time.

APPROACH
We check if the input list is empty, if so return None and None as the max and min. Else we assign the first
number as the min and max. Now we iterate over the 2nd element to end of array. If the number is bigger
then our maximum number, we update the maximum. If the number is slower then the minimum number found till
now, we update the minimum number.

Once we iterate over the entire array, we return the minimum and the maximum number.

TIME COMPLEXITY
Since we are iterating over each array element and only doing 2 comparison with min and max element till now,
so time complexity is O(N) assuming N is the input list size.

SPACE COMPLEXITY
Since we are not using any additional storage, we only use 2 integers to be returned as the answer, space
complexity is constant that is O(1). 