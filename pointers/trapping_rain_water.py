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

def trap(height: List[int]) -> int:
    left, right = 0, 0
    result = 0
    while right < len(height):
        right += 1
        if height[left] < height[right]:
            left = right
            right += 1
            print(height[left])
        else:
            total = 0
            while left != right:
                if left == len(height) - 1:
                    return
                elif right == len(height) - 1:
                    left += 1
                    right = left + 1
                    total = 0
                elif height[right] < height[left]:
                    total += (height[left] - height[right])
                    right += 1
                else:
                    left = right
                    
# Test cases
input1 = [0,1,0,2,1,0,1,3,2,1,2,1]
output1 = trap(input1)
assert output1 == 6, f"Test case 1 failed: {output1}"

input2 = [4,2,0,3,2,5]
output2 = trap(input2)
assert output2 == 9, f"Test case 2 failed: {output2}"

print("All test cases passed!")