# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

"""
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    non_zero_index = 0 
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
assert nums == [1, 3, 12, 0, 0], f"Test case 1 failed: {nums} != [1, 3, 12, 0, 0]"

nums = [0]
moveZeroes(nums)
assert nums == [0], f"Test case 2 failed: {nums} != [0]"

print("All test cases passed!")
