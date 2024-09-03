# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

'''
Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
'''

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    sum_window = sum(nums[:k])
    max_sum = sum_window
    
    for i in range(k, len(nums)):
        sum_window += nums[i] - nums[i - k]
        max_sum = max(max_sum, sum_window)

    return max_sum / k



# Example 1
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
expected_output1 = 12.75
assert findMaxAverage(nums1, k1) == expected_output1, f"Expected {expected_output1} but got {findMaxAverage(nums1, k1)}"

# Example 2
nums2 = [5]
k2 = 1
expected_output2 = 5.0
assert findMaxAverage(nums2, k2) == expected_output2, f"Expected {expected_output2} but got {findMaxAverage(nums2, k2)}"

print("All test cases passed!")