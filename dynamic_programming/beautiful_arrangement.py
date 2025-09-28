# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

"""
Example 1:
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:
Input: n = 1
Output: 1
"""

def countArrangement(n):
    """
    :type n: int
    :rtype: int
    """
    used = [False] * (n + 1)
    count = 0

    def backtrack(i):
        nonlocal count
        if i > n:
            count += 1
            return
        for num in range(1, n + 1):
            if not used[num] and (num % i == 0 or i % num == 0):
                used[num] = True
                backtrack(i + 1)
                used[num] = False
    
    backtrack(1)
    return count

assert countArrangement(2) == 2
assert countArrangement(1) == 1

print("All test cases passed!")