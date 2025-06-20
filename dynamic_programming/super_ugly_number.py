# A super ugly number is a positive integer whose prime factors are in the array primes.
# Given an integer n and an array of integers primes, return the nth super ugly number.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

"""
Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:
Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
"""

import heapq

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly_numbers = [1]
    heap = [(p, p, 0) for p in primes]
    heapq.heapify(heap)

    while len(ugly_numbers) < n:
        next_ugly, prime, index = heapq.heappop(heap)
        if next_ugly != ugly_numbers[-1]:
            ugly_numbers.append(next_ugly)
        heapq.heappush(heap, (prime * ugly_numbers[index + 1], prime, index + 1))

    return ugly_numbers[-1]


assert nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32
assert nthSuperUglyNumber(1, [2, 3, 5]) == 1

print("All test cases passed!")