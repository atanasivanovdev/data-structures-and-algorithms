# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

'''
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

from typing import List
from collections import deque

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = deque()
    result = [0] * len(temperatures)
    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append((temp, index)) 
    return result
        
# Example 1
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
output1 = dailyTemperatures(temperatures1)
assert output1 == [1, 1, 4, 2, 1, 1, 0, 0], f"Test case 1 failed: {output1}"

# Example 2
temperatures2 = [30, 40, 50, 60]
output2 = dailyTemperatures(temperatures2)
assert output2 == [1, 1, 1, 0], f"Test case 2 failed: {output2}"

# Example 3
temperatures3 = [30, 60, 90]
output3 = dailyTemperatures(temperatures3)
assert output3 == [1, 1, 0], f"Test case 3 failed: {output3}"

print("All test cases passed!")