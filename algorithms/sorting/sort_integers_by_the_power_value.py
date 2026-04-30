# The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:
# - If x is even, divide it by 2.
# - If x is odd, multiply it by 3 and then add 1.
# For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

# Given three integers lo, hi and k. You are asked to sort all integers in the range [lo, hi] by the power value in ascending order, starting with the smallest power value.
# For integers with the same power value, sort them in ascending order by number itself.
# Return the k-th smallest integer in the range [lo, hi] sorted by the power value.

"""
Example 1:
Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation:
The power values of 12, 13, 14 and 15 are 9, 9, 17 and 4, respectively.
The sorted array representing these integers is [15, 12, 13, 14].
The second strongest number is 12.

Example 2:
Input: lo = 7, hi = 11, k = 4
Output: 7
Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.

Example 3:
Input: lo = 10, hi = 20, k = 5
Output: 13
Explanation:
The power values of 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 are 6, 3, 9, 9, 17, 4, 4, 13, 9, 8, 7 respectively.
The sorted array is [11, 15, 16, 10, 18, 20, 12, 13, 19, 14, 17].
The fifth number in the sorted array is 13.
"""

def getKth(lo, hi, k):
    """
    :type lo: int
    :type hi: int
    :type k: int
    :rtype: int
    """
    def power(x):
        steps = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            steps += 1
        return steps

    numbers = [(power(i), i) for i in range(lo, hi + 1)]
    numbers.sort(key=lambda x: (x[0], x[1]))

    return numbers[k - 1][1] if k <= len(numbers) else -1


assert getKth(12, 15, 2) == 13
assert getKth(7, 11, 4) == 7
assert getKth(10, 20, 5) == 13

print("All test cases passed!")
