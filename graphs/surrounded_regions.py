# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.


"""
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
"""

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    if not board or not board[0]:
        return
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        """Mark all 'O' cells connected to border as safe (change to 'S')"""
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            board[r][c] != 'O'):
            return
        
        board[r][c] = 'S'
        
        dfs(r + 1, c) 
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for c in range(cols):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[rows-1][c] == 'O':
            dfs(rows-1, c)
    
    for r in range(rows):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][cols-1] == 'O':
            dfs(r, cols-1)
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'
    

# Test case 1
board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expected1 = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
solve(board1)
assert board1 == expected1, f"Test 1 failed: got {board1}, expected {expected1}"

# Test case 2
board2 = [["X"]]
expected2 = [["X"]]
solve(board2)
assert board2 == expected2, f"Test 2 failed: got {board2}, expected {expected2}"

print("All test cases passed!")