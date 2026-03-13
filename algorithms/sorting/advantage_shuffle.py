# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# Return any permutation of nums1 that maximizes its advantage with respect to nums2.

"""
Example 1:
Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]
"""

def advantageCount(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    n = len(nums1)
    nums1.sort()

    sorted_idx = sorted(range(n), key=lambda i: nums2[i], reverse=True)

    res = [0] * n
    left, right = 0, n - 1

    for idx in sorted_idx:
        if nums1[right] > nums2[idx]:
            res[idx] = nums1[right]
            right -= 1
        else:
            res[idx] = nums1[left]
            left += 1

    return res


assert advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
assert advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12]

print("All test cases passed!")