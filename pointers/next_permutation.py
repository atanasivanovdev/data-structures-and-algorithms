# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

'''
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
'''

from typing import List

def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pivot = -1
    length = len(nums)
    for index in range(length - 2, -1, -1):
        if nums[index] < nums[index + 1]:
            pivot = index
            break

    if pivot == -1:
        nums.reverse()
        return
       
    for index in range(length - 1, pivot, -1):
        if nums[index] > nums[pivot]:
            nums[index], nums[pivot] = nums[pivot], nums[index]
            break

    nums[pivot+1:] = reversed(nums[pivot+1:])
            

# Test case 1
nums1 = [1, 2, 3]
nextPermutation(nums1)
assert nums1 == [1, 3, 2], f"Expected [1, 3, 2] but got {nums1}"

# Test case 2
nums2 = [3, 2, 1]
nextPermutation(nums2)
assert nums2 == [1, 2, 3], f"Expected [1, 2, 3] but got {nums2}"

# Test case 3
nums3 = [1, 1, 5]
nextPermutation(nums3)
assert nums3 == [1, 5, 1], f"Expected [1, 5, 1] but got {nums3}"

# Test case 4
nums4 = [1, 3, 2]
nextPermutation(nums4)
assert nums4 == [2, 1, 3], f"Expected [2, 1, 3] but got {nums4}"