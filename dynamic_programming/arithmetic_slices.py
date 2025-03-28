# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.


"""
Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0"
"""


from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:
    if len(nums) < 3:
        return 0

    count = 0
    n = len(nums)
    
    for i in range(n - 2):
        diff = nums[i + 1] - nums[i]
        for j in range(i + 2, n):
            if nums[j] - nums[j - 1] == diff:
                count += 1
            else:
                break 
    
    return count


assert numberOfArithmeticSlices([1, 2, 3, 4]) == 3

assert numberOfArithmeticSlices([1]) == 0

print("All test cases passed!")