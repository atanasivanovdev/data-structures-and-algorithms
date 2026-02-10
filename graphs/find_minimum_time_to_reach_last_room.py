# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds after which the room opens and can be moved to. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

# Return the minimum time to reach the room (n - 1, m - 1).

# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

"""
Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.

Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 3
"""

import heapq

def minTimeToReach(moveTime):
    """
    :type moveTime: List[List[int]]
    :rtype: int
    """
    n, m = len(moveTime), len(moveTime[0])
    
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0
    
    heap = [(0, 0, 0)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while heap:
        time, x, y = heapq.heappop(heap)
        
        if x == n - 1 and y == m - 1:
            return time
        
        if time > dist[x][y]:
            continue
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                next_time = max(time, moveTime[nx][ny]) + 1
                if next_time < dist[nx][ny]:
                    dist[nx][ny] = next_time
                    heapq.heappush(heap, (next_time, nx, ny))
    
    return -1


assert minTimeToReach([[0,4],[4,4]]) == 6
assert minTimeToReach([[0,0,0],[0,0,0]]) == 3
assert minTimeToReach([[0,1],[1,2]]) == 3

print("All test cases passed!")