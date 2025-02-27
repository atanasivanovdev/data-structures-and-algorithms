# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 
"""
Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]
"""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    
    count1, count2, candidate1, candidate2 = 0, 0, None, None
    
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    
    return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]

# Example 1
assert majorityElement([3,2,3]) == [3]

# Example 2
assert majorityElement([1]) == [1]

# Example 3
assert majorityElement([1,2]) == [1,2]

print("All test cases passed!")
