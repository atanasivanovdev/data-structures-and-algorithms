# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

"""
Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
"""

def findSubsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    path = []

    def backtrack(start):
        if len(path) >= 2:
            res.append(path[:])

        used = set()
        for i in range(start, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in used:
                continue
            used.add(nums[i])
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res

assert findSubsequences([4, 6, 7, 7]) == [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
assert findSubsequences([4, 4, 3, 2, 1]) == [[4, 4]]

print("All test cases passed!")