# You are given two strings s and t of the same length, and two integer arrays nextCost and previousCost.

#In one operation, you can pick any index i of s, and perform either one of the following actions:

#Shift s[i] to the next letter in the alphabet. If s[i] == 'z', you should replace it with 'a'. This operation costs nextCost[j] where j is the index of s[i] in the alphabet.
#Shift s[i] to the previous letter in the alphabet. If s[i] == 'a', you should replace it with 'z'. This operation costs previousCost[j] where j is the index of s[i] in the alphabet.
#The shift distance is the minimum total cost of operations required to transform s into t.

#Return the shift distance from s to t.

 
"""
Example 1:
Input: s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: 2

Explanation:
We choose index i = 0 and shift s[0] 25 times to the previous character for a total cost of 1.
We choose index i = 1 and shift s[1] 25 times to the next character for a total cost of 0.
We choose index i = 2 and shift s[2] 25 times to the previous character for a total cost of 1.
We choose index i = 3 and shift s[3] 25 times to the next character for a total cost of 0.

Example 2:
Input: s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Output: 31

Explanation:
We choose index i = 0 and shift s[0] 9 times to the previous character for a total cost of 9.
We choose index i = 1 and shift s[1] 10 times to the next character for a total cost of 10.
We choose index i = 2 and shift s[2] 1 time to the previous character for a total cost of 1.
We choose index i = 3 and shift s[3] 11 times to the next character for a total cost of 11."
"""

from typing import List

def shiftDistance(s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
    total_cost = 0
    
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        
        start = ord(s[i]) - ord('a')
        target = ord(t[i]) - ord('a')
        
        # Forward shift (nextCost)
        forward_cost = 0
        index = start
        while index != target:
            forward_cost += nextCost[index]
            index = (index + 1) % 26 
        
        # Backward shift (previousCost)
        backward_cost = 0
        index = start
        while index != target:
            index = (index - 1) % 26 
            backward_cost += previousCost[index]
        
        total_cost += min(forward_cost, backward_cost)
    
    return total_cost


assert shiftDistance("leet", "code", [1]*26, [1]*26) == 31

print("All test cases passed!")