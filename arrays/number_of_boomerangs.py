# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Return the number of boomerangs.

"""
Example 1:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:
Input: points = [[1,1]]
Output: 0
"""

from collections import defaultdict

def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """

    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    count = 0
    for i in points:
        dist_count = defaultdict(int)
        for j in points:
            if i != j:
                dist = distance(i, j)
                dist_count[dist] += 1
        for k in dist_count.values():
            count += k * (k - 1)

    return count


assert numberOfBoomerangs([[0,0],[1,0],[2,0]]) == 2, "Test Case 1 Failed"
assert numberOfBoomerangs([[1,1],[2,2],[3,3]]) == 2, "Test Case 2 Failed"
assert numberOfBoomerangs([[1,1]]) == 0, "Test Case 3 Failed"

print("All test cases passed!")