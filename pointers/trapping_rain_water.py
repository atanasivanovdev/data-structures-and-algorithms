# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List

# Time complexity: O(n^2)
# Space complexity: O(1)
def trap(height: List[int]) -> int:
    left, right = 0, 0
    result = 0
    while right < len(height):
        right += 1
        total = 0
        while left != right:
            if left == len(height) - 1:
                break
            elif height[right] >= height[left]:
                left = right
            elif right == len(height) - 1:
                left += 1
                right = left + 1
                total = 0
            elif height[right] < height[left]:
                total += (height[left] - height[right])
                right += 1

        result += total 
    return result

# Test cases
input1 = [0,1,0,2,1,0,1,3,2,1,2,1]
output1 = trap(input1)
assert output1 == 6, f"Test case 1 failed: {output1}"

input2 = [4,2,0,3,2,5]
output2 = trap(input2)
assert output2 == 9, f"Test case 2 failed: {output2}"

print("All test cases passed!")


from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
def trap_improved(height: List[int]) -> int:
    length = len(height)
    left, right = 0, len(height) - 1
    maxLeftArray, maxRightArray = [0] * length, [0] * length
    maxLeft, maxRight = height[left], height[right]
    result = 0

    while left < length:
        maxLeft = max(maxLeft, height[left])
        maxRight = max(maxRight, height[right])

        maxLeftArray[left] = maxLeft
        maxRightArray[right] = maxRight   

        left += 1
        right -= 1
         
    for i in range(len(height)):
        total_water = min(maxLeftArray[i], maxRightArray[i]) - height[i]
        if total_water > 0:
            result += total_water
            
    return result

# Test cases
input1 = [0,1,0,2,1,0,1,3,2,1,2,1]
output1 = trap_improved(input1)
assert output1 == 6, f"Test case 1 failed: {output1}"

input2 = [4,2,0,3,2,5]
output2 = trap_improved(input2)
assert output2 == 9, f"Test case 2 failed: {output2}"

print("All test cases passed!")