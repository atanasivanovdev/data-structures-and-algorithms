# Given an m x n matrix, return all elements of the matrix in spiral order.

'''
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    while matrix:
        result += matrix.pop(0)
        
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        
        if matrix:
            result += matrix.pop()[::-1]
        
        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0))
    
    return result

# Test cases
# Example 1
matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
output = spiralOrder(matrix)
assert output == expected, f"Expected {expected} but got {output}"

# Example 2
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
expected = [1,2,3,4,8,12,11,10,9,5,6,7]
output = spiralOrder(matrix)
assert output == expected, f"Expected {expected} but got {output}"

print("All test cases passed!")