# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 
"""
Example 1:
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

Example 2:
Input: wall = [[1],[1],[1]]
Output: 3
"""

from collections import defaultdict
from typing import List


def leastBricks(wall: List[List[int]]) -> int:
    edge_count = defaultdict(int)
    max_edges = 0 
    
    for row in wall:
        width = 0  
        for brick in row[:-1]:
            width += brick
            edge_count[width] += 1
            max_edges = max(max_edges, edge_count[width])

    return len(wall) - max_edges


# Test case 1
wall1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
assert leastBricks(wall1) == 2, "Test Case 1 Failed"

# Test case 2
wall2 = [[1],[1],[1]]
assert leastBricks(wall2) == 3, "Test Case 2 Failed"

print("All test cases passed!")