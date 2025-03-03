# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

 
"""
Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
"""
from typing import List

def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for s in strs:
        zero_count = s.count('0')
        one_count = s.count('1')
        
        for i in range(m, zero_count - 1, -1):
            for j in range(n, one_count - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zero_count][j - one_count])
    
    return dp[m][n]

# Test cases
input1 = (["10", "0001", "111001", "1", "0"], 5, 3)
output1 = findMaxForm(*input1)
assert output1 == 4, f"Test case 1 failed: {output1}"

input2 = (["10", "0", "1"], 1, 1)
output2 = findMaxForm(*input2)
assert output2 == 2, f"Test case 2 failed: {output2}"

print("All test cases passed!")