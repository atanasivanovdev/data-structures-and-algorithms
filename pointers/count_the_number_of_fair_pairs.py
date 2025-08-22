# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:
#
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper

"""
Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
"""

def countFairPairs(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if lower <= nums[i] + nums[j] <= upper:
                count += 1
                
    return count


assert countFairPairs([0,1,7,4,4,5], 3, 6) == 6
assert countFairPairs([1,7,9,2,5], 11, 11) == 1

print("All test cases passed!")