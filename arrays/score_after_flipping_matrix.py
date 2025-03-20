# You are given an m x n binary matrix grid.

# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score after making any number of moves (including zero moves).

"""
Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1
"""

from typing import List

def matrixScore(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    for row in range(m):
        if grid[row][0] == 0:
            for col in range(n):
                grid[row][col] ^= 1
    
    for col in range(1, n):
        count_ones = sum(grid[row][col] for row in range(m))
        count_zeros = m - count_ones
        
        if count_zeros > count_ones:
            for row in range(m):
                grid[row][col] ^= 1
    
    score = 0
    for row in grid:
        row_value = int("".join(map(str, row)), 2)
        score += row_value
    
    return score


assert matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39, f"Test case 1 failed: {matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])} != 39"

assert matrixScore([[0]]) == 1, f"Test case 2 failed: {matrixScore([[0]])} != 1"

print("All test cases passed!")