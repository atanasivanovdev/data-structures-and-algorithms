# Given an m x n binary matrix mat, return the number of submatrices that have all ones.

"""
Example 1:
Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13

Example 2:
Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
"""

def numSubmat(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    if not mat or not mat[0]:
        return 0

    m, n = len(mat), len(mat[0])

    heights = [0] * n
    count = 0

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += 1

        for j in range(n):
            if heights[j] > 0:
                min_height = heights[j]
                for k in range(j, n):
                    if heights[k] == 0:
                        break
                    min_height = min(min_height, heights[k])
                    count += min_height

    return count


assert numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 13, "Test Case 1 Failed"
assert numSubmat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]) == 24, "Test Case 2 Failed"

print("All test cases passed!")
