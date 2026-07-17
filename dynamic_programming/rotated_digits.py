# An integer x is a good if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. For example:

# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and

# Given an integer n, return the number of good integers in the range [1, n].

"""
Example 1:
Input: n = 10
Output: 4
Explanation: 2, 5, 6, 9 are good.

Example 2:
Input: n = 1
Output: 0

Example 3:
Input: n = 2
Output: 1
"""

def rotatedDigits(n: int) -> int:
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    count = 0

    for i in range(n + 1):
        if i < 10:
            if i in (0, 1, 8):
                dp[i] = 1
            elif i in (2, 5, 6, 9):
                dp[i] = 2
                if i != 0:
                    count += 1
            else:
                dp[i] = 0
        else:
            a = dp[i // 10]
            b = dp[i % 10]

            if a == 0 or b == 0:
                dp[i] = 0
            elif a == 1 and b == 1:
                dp[i] = 1
            else:
                dp[i] = 2
                count += 1

    return count


assert rotatedDigits(10) == 4, "Test Case 1 Failed"
assert rotatedDigits(1) == 0, "Test Case 2 Failed"
assert rotatedDigits(2) == 1, "Test Case 3 Failed"

print("All test cases passed!")
