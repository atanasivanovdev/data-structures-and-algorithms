# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicate(nums: List[int]) -> bool:
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
        else:
            unique_nums.add(num)
    return False

assert containsDuplicate(nums1) == True
assert containsDuplicate(nums2) == False
assert containsDuplicate(nums3) == True