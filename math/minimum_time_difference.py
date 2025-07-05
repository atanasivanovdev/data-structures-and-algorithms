# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

"""
Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""

def findMinDifference(timePoints):
    """
    :type timePoints: List[str]
    :rtype: int
    """
    minutes = []
    for time in timePoints:
        h, m = map(int, time.split(':'))
        total_minutes = h * 60 + m
        minutes.append(total_minutes)

    minutes.sort()
    min_diff = float('inf')

    for i in range(1, len(minutes)):
        diff = minutes[i] - minutes[i - 1]
        min_diff = min(min_diff, diff)

    wrap_around_diff = (minutes[0] + 1440) - minutes[-1]
    min_diff = min(min_diff, wrap_around_diff)

    return min_diff


assert findMinDifference(["23:59", "00:00"]) == 1
assert findMinDifference(["00:00", "23:59", "00:00"]) == 0

print("All test cases passed!")