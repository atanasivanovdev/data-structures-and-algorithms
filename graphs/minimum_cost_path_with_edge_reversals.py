# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

"""
Example 1:
Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
Output: 5
Explanation:
Use the path 0 → 1 (cost 3).
At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
Total cost is 3 + 2 = 5.

Example 2:
Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
Output: 3
Explanation:
No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
Total cost is 1 + 1 + 1 = 3.
"""

import heapq
from collections import defaultdict

def minCost(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    out_edges = defaultdict(list)
    in_edges = defaultdict(list)
    
    for u, v, w in edges:
        out_edges[u].append((v, w))
        in_edges[v].append((u, w))
    
    INF = float('inf')
    dist = [[INF, INF] for _ in range(n)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    while pq:
        cost, u, used = heapq.heappop(pq)
        
        if cost > dist[u][used]:
            continue
        
        for v, w in out_edges[u]:
            new_cost = cost + w
            if new_cost < dist[v][used]:
                dist[v][used] = new_cost
                heapq.heappush(pq, (new_cost, v, used))
        
        if used == 0:
            for v, w in in_edges[u]:
                new_cost = cost + 2 * w
                if new_cost < dist[v][1]:
                    dist[v][1] = new_cost
                    heapq.heappush(pq, (new_cost, v, 1))
    
    ans = min(dist[n-1])
    return ans if ans < INF else -1


assert minCost(4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]) == 5
assert minCost(4, [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]) == 3

print("All test cases passed!")