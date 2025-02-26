# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Test cases are designed so that the answer will fit in a 32-bit integer.

 
"""
Example 1:
Input: nums = [1,2,3]
Output: 2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:
Input: nums = [1,10,2,9]
Output: 16
"""

def minMoves2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort() 
    median = nums[len(nums) // 2]
    
    return sum(abs(num - median) for num in nums)


# Test case 1
nums = [1, 2, 3]
assert minMoves2(nums) == 2, "Test case 1 failed"

# Test case 2
nums = [1, 10, 2, 9]
assert minMoves2(nums) == 16, "Test case 2 failed"

print("All test cases passed!")