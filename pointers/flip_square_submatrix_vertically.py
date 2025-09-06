# You are given an m x n integer matrix grid, and three integers x, y, and k.

# The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.

# Your task is to flip the submatrix by reversing the order of its rows vertically.

# Return the updated matrix.

"""
Example 1:
Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3
Output: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

Example 2:
Input: grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2
Output: [[3,4,4,2],[2,3,2,3]]
"""

def reverseSubmatrix(grid, x, y, k):
    """
    :type grid: List[List[int]]
    :type x: int
    :type y: int
    :type k: int
    :rtype: List[List[int]]
    """
    for i in range(k // 2):
        for j in range(k):
            grid[x + i][y + j], grid[x + k - 1 - i][y + j] = grid[x + k - 1 - i][y + j], grid[x + i][y + j]

    return grid


assert reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3) == [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
assert reverseSubmatrix([[3,4,2,3],[2,3,4,2]], 0, 2, 2) == [[3,4,4,2],[2,3,2,3]]

print("All test cases passed!")