# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

from typing import List

# Time complexity: O(n)
# Space complexity: O(1)
def maxArea(height: List[int]) -> int:
    start, end = 0, len(height) - 1
    max_amount = 0
    while start < end:
        width = end - start
        area = width * min(height[start], height[end])
        max_amount = max(max_amount, area)
        if height[end] > height[start]:
            start += 1
        elif height[start] > height[end]:
            end -= 1
        else:
            start += 1
            end -= 1
    return max_amount

# Test cases
input1 = [1,8,6,2,5,4,8,3,7]
output1 = maxArea(input1)
assert output1 == 49, f"Test case 1 failed: {output1}"

input2 = [1,1]
output2 = maxArea(input2)
assert output2 == 1, f"Test case 2 failed: {output2}"

input3 = [4,3,2,1,4]
output3 = maxArea(input3)
assert output3 == 16, f"Test case 3 failed: {output3}"

input4 = [1,2,1]
output4 = maxArea(input4)
assert output4 == 2, f"Test case 4 failed: {output4}"

input5 = [2,3,4,5,18,17,6]
output5 = maxArea(input5)
assert output5 == 17, f"Test case 5 failed: {output5}"

print("All test cases passed!")