# You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.

# Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.

# Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.

"""
Example 1:
Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
Output: true
Explanation:
It can be done by changing the color of the grid[0][2].

Example 2:
Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
Output: false
Explanation:
It cannot be done by changing at most one cell.

Example 3:
Input: grid = [["B","W","B"],["B","W","W"],["B","W","W"]]
Output: true
Explanation:
The grid already contains a 2 x 2 square of the same color.
"""

from typing import List

def canMakeSquare(grid: List[List[str]]) -> bool:
    for i in range(2):
        for j in range(2):
            subgrid = [grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]
        
            count_B = subgrid.count('B')
            count_W = subgrid.count('W')
            
            if count_B == 4 or count_W == 4 or count_B == 3 or count_W == 3:
                return True
                
    return False

assert canMakeSquare([["B","W","B"],["B","W","W"],["B","W","B"]]) == True
assert canMakeSquare([["B","W","B"],["W","B","W"],["B","W","B"]]) == False
assert canMakeSquare([["B","W","B"],["B","W","W"],["B","W","W"]]) == True

print("All test cases passed!")