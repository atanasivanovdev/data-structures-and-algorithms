# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

'''
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    left, right = 0, 1

    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]

        right += 1
    return left + 1


# Test 1
nums1 = [1, 1, 2]
expectedNums1 = [1, 2]

k1 = removeDuplicates(nums1)

assert k1 == len(expectedNums1)
for i in range(k1):
    assert nums1[i] == expectedNums1[i]

# Test 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums2 = [0, 1, 2, 3, 4]

k2 = removeDuplicates(nums2)

assert k2 == len(expectedNums2)
for i in range(k2):
    assert nums2[i] == expectedNums2[i]

# Test 3
nums3 = [1, 2, 3, 4, 5]
expectedNums3 = [1, 2, 3, 4, 5]

k3 = removeDuplicates(nums3)

assert k3 == len(expectedNums3)
for i in range(k3):
    assert nums3[i] == expectedNums3[i]

print("All test cases passed!")