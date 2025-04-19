# You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.
# Return an n x m matrix representing the box after the rotation described above.

 
"""
Example 1:
Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
"""

def rotateTheBox(boxGrid):
    """
    :type boxGrid: List[List[str]]
    :rtype: List[List[str]]
    """
    m, n = len(boxGrid), len(boxGrid[0])

    for row in boxGrid:
        write_idx = n - 1
        for col in range(n - 1, -1, -1):
            if row[col] == '*':
                write_idx = col - 1
            elif row[col] == '#':
                if col != write_idx:
                    row[write_idx], row[col] = row[col], '.'
                write_idx -= 1

    rotated = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated[j][m - 1 - i] = boxGrid[i][j]

    return rotated

assert rotateTheBox([["#", ".", "#"]]) == [["."], ["#"], ["#"]], "Test Case 1 Failed"

assert rotateTheBox([
    ["#", ".", "*", "."],
    ["#", "#", "*", "."]
]) == [
    ["#", "."],
    ["#", "#"],
    ["*", "*"],
    [".", "."]
], "Test Case 2 Failed"

assert rotateTheBox([
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."]
]) == [
    [".", "#", "#"],
    [".", "#", "#"],
    ["#", "#", "*"],
    ["#", "*", "."],
    ["#", ".", "*"],
    ["#", ".", "."]
], "Test Case 3 Failed"

print("All test cases passed!")