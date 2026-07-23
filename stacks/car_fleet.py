# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.

'''
Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
'''

def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    pairs = sorted(zip(position, speed), reverse=True)

    stack = []
    for pos, spd in pairs:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


assert carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3, "Test Case 1 Failed"
assert carFleet(10, [3], [3]) == 1, "Test Case 2 Failed"
assert carFleet(100, [0, 2, 4], [4, 2, 1]) == 1, "Test Case 3 Failed"

print("All test cases passed!")
