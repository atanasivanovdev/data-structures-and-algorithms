# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

"""
Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36."
"""

def integerBreak(n: int) -> int:
    if n <= 3:
        return n - 1
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 2, 3
    for i in range(4, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] * dp[i - j])
    return dp[n]


assert integerBreak(2) == 1
assert integerBreak(10) == 36

print("All test cases passed!")