# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

"""
Example 1:
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
"""

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indices = [i for i, num in enumerate(self.nums) if num == target]
        return random.choice(indices)


solution = Solution([1, 2, 3, 3, 3])

result1 = solution.pick(3)
assert result1 in [2, 3, 4], f"Expected index 2, 3, or 4 but got {result1}"

result2 = solution.pick(1)
assert result2 == 0, f"Expected index 0 but got {result2}"

result3 = solution.pick(3)
assert result3 in [2, 3, 4], f"Expected index 2, 3, or 4 but got {result3}"

print("All test cases passed!")