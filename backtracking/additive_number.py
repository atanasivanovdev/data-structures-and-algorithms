# An additive number is a string whose digits can form an additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
# Given a string containing only digits, return true if it is an additive number or false otherwise.
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

"""
Example 1:
Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199
"""

def isAdditiveNumber(num):
    """
    :type num: str
    :rtype: bool
    """
    def is_valid_sequence(first, second, remaining):
        if not remaining:
            return True
        next_num = str(int(first) + int(second))
        if remaining.startswith(next_num):
            return is_valid_sequence(second, next_num, remaining[len(next_num):])
        return False

    n = len(num)
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n - i + 1):
            first = num[:i]
            second = num[i:j]
            if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                continue
            if is_valid_sequence(first, second, num[j:]):
                return True
    return False

assert isAdditiveNumber("112358") == True
assert isAdditiveNumber("199100199") == True

print("All test cases passed!")