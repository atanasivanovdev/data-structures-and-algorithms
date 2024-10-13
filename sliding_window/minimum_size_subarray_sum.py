# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

'''
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    sub_array_len = float('inf')
    left = 0
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            sub_array_len = min(sub_array_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if sub_array_len == float('inf') else sub_array_len


# Example 1
assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2

# Example 2
assert minSubArrayLen(4, [1,4,4]) == 1

# Example 3
assert minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0

print("All test cases passed!")