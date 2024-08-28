# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


'''
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest_target = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[left] + nums[i] + nums[right]
            if abs(total - target) < abs(closest_target - target):
                closest_target = total 

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return target
    return closest_target


# Tests
nums1 = [-1, 2, 1, -4]
target1 = 1
output1 = 2
assert threeSumClosest(nums1, target1) == output1, f"Test case 1 failed: {output1}"

nums2 = [0, 0, 0]
target2 = 1
output2 = 0
assert threeSumClosest(nums2, target2) == output2, f"Test case 2 failed: {output2}"

nums3 = [1, 1, 1, 1]
target3 = 2
output3 = 3  # (1 + 1 + 1 = 3)
assert threeSumClosest(nums3, target3) == output3, f"Test case 3 failed: {output3}"

nums4 = [1, 1, 1, 0]
target4 = -100
output4 = 2  # (1 + 1 + 0 = 2) as it's the closest sum to -100
assert threeSumClosest(nums4, target4) == output4, f"Test case 4 failed: {output4}"

nums5 = [-1, 0, 1, 1]
target5 = 0
output5 = 0  # (-1 + 0 + 1 = 0)
assert threeSumClosest(nums5, target5) == output5, f"Test case 5 failed: {output5}"

nums6 = [1, 2, 3, 4]
target6 = 6
output6 = 6  # (1 + 2 + 3 = 6)
assert threeSumClosest(nums6, target6) == output6, f"Test case 6 failed: {output6}"

nums7 = [-10, -5, -2, 3, 7, 12, 15, 18, 20]
target7 = 25
output7 = 25  # (7 + 12 + 6 = 25)
assert threeSumClosest(nums7, target7) == output7, f"Test case 7 failed: {output7}"

print("All test cases passed!")