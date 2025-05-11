# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

"""
Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
"""

def findTargetSumWays(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    total = sum(nums)

    if total < target or (total + target) % 2 != 0:
        return 0
    
    s = (total + target) // 2
    dp = [0] * (s + 1)
    dp[0] = 1

    for num in nums:
        for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
            
    return dp[s]


assert findTargetSumWays([1, 1, 1, 1, 1], 3) == 5, "Test Case 1 Failed"
assert findTargetSumWays([1], 1) == 1, "Test Case 2 Failed"

print("All test cases passed!")