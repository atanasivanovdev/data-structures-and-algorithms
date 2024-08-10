# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

"""
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List

nums1 = [1, 2, 3, 4]
output1= [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3 ,3]
output2 = [0, 0, 9, 0, 0]

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)

    prefix = [0] * n
    postfix = [0] * n
    output = []

    prefix[0] = nums[0]
    postfix[n - 1] = nums[n - 1]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i]

    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i+1] * nums[i]

    for i in range(n):
        if i == 0:
            output.append(postfix[i])
        elif i == n - 1:
            output.append(prefix[i - 1])
        else:
            output.append(prefix[i - 1] * postfix[i + 1])

    return output

assert productExceptSelf(nums1) == output1
assert productExceptSelf(nums2) == output2

def productExceptSelf1(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n
    
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output

assert productExceptSelf1(nums1) == output1
assert productExceptSelf1(nums2) == output2
