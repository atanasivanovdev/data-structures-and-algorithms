# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
from typing import List
import heapq

nums1 = [1, 1, 1, 2, 2, 3, 20, 20, 32, 12, 53, 12, 43, 43, 12, 31, 31, 31, 21, 31]
k1 = 2
output1 = [1, 2]

nums2 = [1]
k2 = 1
output2 = [1]

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count_nums = {}
    for num in nums:
        if num not in count_nums:
            count_nums[num] = 1
        else:
            count_nums[num] += 1
            
    min_heap = []
    for num, freq in count_nums.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = [num for freq, num in min_heap]
    return result

topKFrequent(nums1, k1)
# assert topKFrequent(nums1, k1) == output1
# assert topKFrequent(nums2, k2) == output2