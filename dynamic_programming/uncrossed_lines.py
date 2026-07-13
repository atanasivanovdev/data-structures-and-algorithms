# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2
# (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
# - nums1[i] == nums2[j], and
# - the line we draw does not intersect any other connecting (non-horizontal) line.

# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only
# belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

"""
Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
"""

def maxUncrossedLines(nums1: list[int], nums2: list[int]) -> int:
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


assert maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2, "Test Case 1 Failed"
assert maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3, "Test Case 2 Failed"
assert maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2, "Test Case 3 Failed"

print("All test cases passed!")
