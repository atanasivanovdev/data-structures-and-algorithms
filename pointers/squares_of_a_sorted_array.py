# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

"""
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([num ** 2 for num in nums])


assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100], f"Test case 1 failed: {sortedSquares([-4, -1, 0, 3, 10])} != [0, 1, 9, 16, 100]"

assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121], f"Test case 2 failed: {sortedSquares([-7, -3, 2, 3, 11])} != [4, 9, 9, 49, 121]"

print("All test cases passed!")