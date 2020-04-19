Here we had to find count of files ending with a certain suffix inside a directory. So we list the immediate contents
inside the directory. For all files, check if they end with the suffix, if so increment the count. If it is a folder,
recursively call the same function to get the count and add it to the existing count.

Time Complexity : O(n) where n are the total files inside a directory. More the files, it will take more time.
Space Complexity : Since we are not using any additional data structure to maintain anything. So space complexity is O(1).