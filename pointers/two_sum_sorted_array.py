# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

"""
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
from typing import List

# Time complexity: O(n)
# Space complexity: O(1)
def twoSum(numbers: List[int], target: int) -> List[int]:
    start, end = 0, len(numbers) - 1
    while start < end:
        total_sum = numbers[start] + numbers[end]
        if total_sum == target:
            return [start + 1, end + 1] 
        elif total_sum < target:
            start += 1
        else:
            end -= 1



# Test cases
input1 = ([2, 7, 11, 15], 9)
output1 = twoSum(*input1)
assert output1 == [1, 2], f"Test case 1 failed: {output1}"

input2 = ([2, 3, 4], 6)
output2 = twoSum(*input2)
assert output2 == [1, 3], f"Test case 2 failed: {output2}"

input3 = ([-1, 0], -1)
output3 = twoSum(*input3)
assert output3 == [1, 2], f"Test case 3 failed: {output3}"

print("All test cases passed!")