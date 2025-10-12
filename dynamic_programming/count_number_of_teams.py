# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

"""
Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4
"""

def numTeams(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    n = len(rating)
    count = 0
    
    for j in range(n):
        left_less = left_greater = right_less = right_greater = 0
        
        for i in range(j):
            if rating[i] < rating[j]:
                left_less += 1
            elif rating[i] > rating[j]:
                left_greater += 1
        
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                right_less += 1
            elif rating[k] > rating[j]:
                right_greater += 1
        
        count += left_less * right_greater + left_greater * right_less
    
    return count

assert numTeams([2, 5, 3, 4, 1]) == 3
assert numTeams([2, 1, 3]) == 0
assert numTeams([1, 2, 3, 4]) == 4

print("All test cases passed!")