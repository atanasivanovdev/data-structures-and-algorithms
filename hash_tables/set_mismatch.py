# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 
"""
Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]"
"""

from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

    actual_sum = sum(nums)
    actual_square_sum = sum(x * x for x in nums)

    sum_diff = actual_sum - expected_sum
    square_sum_diff = actual_square_sum - expected_square_sum

    sum_xy = square_sum_diff // sum_diff 

    duplicate = (sum_diff + sum_xy) // 2
    missing = duplicate - sum_diff

    return [duplicate, missing]


assert findErrorNums([1, 2, 2, 4]) == [2, 3]

assert findErrorNums([1, 1]) == [1, 2]

print("All test cases passed!")