# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 
"""
Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]
"""

def singleNumber(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num

    diff_bit = xor_all & -xor_all  

    num1, num2 = 0, 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


# Test case 1
nums = [1, 2, 1, 3, 2, 5]
assert sorted(singleNumber(nums)) == sorted([3, 5]), "Test case 1 failed"

# Test case 2
nums = [-1, 0]
assert sorted(singleNumber(nums)) == sorted([-1, 0]), "Test case 2 failed"

# Test case 3
nums = [0, 1]
assert sorted(singleNumber(nums)) == sorted([1, 0]), "Test case 3 failed"

print("All test cases passed!")