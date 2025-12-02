# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

"""
Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

def numRescueBoats(people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0

    while i <= j:

        if people[i] + people[j] <= limit:
            i += 1
            
        j -= 1
        boats += 1

    return boats


assert numRescueBoats([1, 2], 3) == 1
assert numRescueBoats([3, 2, 2, 1], 3) == 3
assert numRescueBoats([3, 5, 3, 4], 5) == 4

print("All test cases passed!")