# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
"""
Example 1:
Input: nums = [1,2,3,1]
Output: 4

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12

Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
        
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = 0, 0
    for num in nums:
        temp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = temp
    
    return prev1


# Example 1
assert rob([1,2,3,1]) == 4  # Rob house 1 and 3

# Example 2
assert rob([2,7,9,3,1]) == 12  # Rob house 1, 3, and 5

# Example 3
assert rob([2,1,1,2]) == 4  # Rob house 1 and 4

print("All test cases passed!")