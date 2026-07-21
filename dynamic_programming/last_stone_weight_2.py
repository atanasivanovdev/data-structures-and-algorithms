# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

"""
Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5
"""

def lastStoneWeightII(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    total = sum(stones)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for stone in stones:
        for s in range(target, stone - 1, -1):
            dp[s] = dp[s] or dp[s - stone]

    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2 * s

    return 0


assert lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1, "Test Case 1 Failed"
assert lastStoneWeightII([31, 26, 33, 21, 40]) == 5, "Test Case 2 Failed"

print("All test cases passed!")
