# You are given a positive number n.
# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

"""
Example 1:
Input: n = 5
Output: 7

Explanation:
The binary representation of 7 is "111".

Example 2:
Input: n = 10
Output: 15

Explanation:
The binary representation of 15 is "1111".

Example 3:
Input: n = 3
Output: 3

Explanation:
The binary representation of 3 is "11"."
"""

def smallestNumber(n: int) -> int:
    power = 1
    while power <= n:
        power *= 2
    return power - 1

assert smallestNumber(5) == 7
assert smallestNumber(10) == 15
assert smallestNumber(3) == 3

print("All test cases passed!")
