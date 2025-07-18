# You have n dice, and each dice has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

"""
Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
"""

def numRollsToTarget(n, k, target):
    """
    :type n: int
    :type k: int
    :type target: int
    :rtype: int
    """
    MOD = 10**9 + 7
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1 

    for dice in range(1, n + 1):
        for t in range(1, target + 1):
            for face in range(1, min(k, t) + 1):
                dp[dice][t] = (dp[dice][t] + dp[dice - 1][t - face]) % MOD

    return dp[n][target]


assert numRollsToTarget(1, 6, 3) == 1
assert numRollsToTarget(2, 6, 7) == 6
assert numRollsToTarget(30, 30, 500) == 222616187

print("All test cases passed!")