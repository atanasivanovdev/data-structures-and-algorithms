# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

 
"""
Example 1:
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Example 2:
Input: nums = [4,14,4]
Output: 4
"""

def totalHammingDistance(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = 0
    n = len(nums)
    
    for bit in range(32): 
        count_ones = sum((num >> bit) & 1 for num in nums)
        count_zeros = n - count_ones
        total += count_ones * count_zeros
    
    return total


# Test case 1
nums = [4, 14, 2]
assert totalHammingDistance(nums) == 6, "Test case 1 failed"

# Test case 2
nums = [4, 14, 4]
assert totalHammingDistance(nums) == 4, "Test case 2 failed"

print("All test cases passed!")