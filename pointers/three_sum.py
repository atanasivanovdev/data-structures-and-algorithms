# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

"""
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List

# Time complexity: O(n^2)
# Space complexity: O(1)
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        if num > 0:
            return result
        
        start, end = i + 1, len(nums) - 1
        while start < end:
            total = num + nums[start] + nums[end]

            if total == 0:
                result.append([num, nums[start], nums[end]])
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                start += 1
                end -= 1
            elif total < 0:
                start += 1
            else:
                end -= 1
    return result


# Example 1
input1 = [-1, 0, 1, 2, -1, -4]
output1 = threeSum(input1)
expected1 = [[-1, -1, 2], [-1, 0, 1]]
assert sorted([sorted(triplet) for triplet in output1]) == sorted([sorted(triplet) for triplet in expected1]), f"Test case 1 failed: {output1}"

# Example 2
input2 = [0, 1, 1]
output2 = threeSum(input2)
expected2 = []
assert output2 == expected2, f"Test case 2 failed: {output2}"

# Example 3
input3 = [0, 0, 0]
output3 = threeSum(input3)
expected3 = [[0, 0, 0]]
assert output3 == expected3, f"Test case 3 failed: {output3}"

print("All test cases passed!")