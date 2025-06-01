# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

"""
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""

def findDiagonalOrder(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    for d in range(m + n - 1):
        if d % 2 == 0: 
            row = min(d, m - 1)
            col = d - row
            while row >= 0 and col < n:
                result.append(mat[row][col])
                row -= 1
                col += 1
        else:
            col = min(d, n - 1)
            row = d - col
            while col >= 0 and row < m:
                result.append(mat[row][col])
                row += 1
                col -= 1

    return result

assert findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
assert findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]

print("All test cases passed!")