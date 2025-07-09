# Given an array of integers arr, sort the array by performing a series of pancake flips.

# In one pancake flip we do the following steps:

# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

"""
Example 1:
Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
"""

def pancakeSort(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    res = []
    n = len(arr)
    
    for size in range(n, 1, -1):
        max_idx = arr.index(max(arr[0:size]))
        
        if max_idx != size - 1:
            if max_idx != 0:
                res.append(max_idx + 1)
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            res.append(size)
            arr[:size] = reversed(arr[:size])
    
    return res


assert pancakeSort([1, 2, 3]) == []

print("All test cases passed!")