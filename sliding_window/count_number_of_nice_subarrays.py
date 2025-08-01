# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

"""
Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

from collections import defaultdict

def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    prefix = defaultdict(int)
    prefix[0] = 1
    odd_count = 0

    for num in nums:
        if num % 2 == 1:
            odd_count += 1
        count += prefix[odd_count - k]
        prefix[odd_count] += 1

    return count


assert numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert numberOfSubarrays([2, 4, 6], 1) == 0
assert numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16

print("All test cases passed!")