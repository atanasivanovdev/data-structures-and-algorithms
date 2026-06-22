# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row
# or leftmost column and going in the bottom-right direction until reaching the matrix's end.

"""
Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example 2:
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
"""

def diagonalSort(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    if not mat or not mat[0]:
        return mat
    
    m, n = len(mat), len(mat[0])
    
    diagonals = {}
    
    for i in range(m):
        for j in range(n):
            diagonal_key = i - j
            if diagonal_key not in diagonals:
                diagonals[diagonal_key] = []
            diagonals[diagonal_key].append(mat[i][j])
    
    for key in diagonals:
        diagonals[key].sort()
    
    for i in range(m):
        for j in range(n):
            diagonal_key = i - j
            mat[i][j] = diagonals[diagonal_key].pop(0)
    
    return mat


assert diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
assert diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]) == [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

print("All test cases passed!")
