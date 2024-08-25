# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

'''
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''
from collections import deque

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    
    closing_brackets = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    stack = deque()
    for bracket in s:
        if bracket in closing_brackets:
            if stack and stack[-1] == closing_brackets[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return True if not stack else False

# Example 1
s1 = "()"
output1 = isValid(s1)
assert output1 == True, f"Test case 1 failed: {output1}"

# Example 2
s2 = "()[]{}"
output2 = isValid(s2)
assert output2 == True, f"Test case 2 failed: {output2}"

# Example 3
s3 = "(]"
output3 = isValid(s3)
assert output3 == False, f"Test case 3 failed: {output3}"

# Example 4
s4 = "([])"
output4 = isValid(s4)
assert output4 == True, f"Test case 4 failed: {output4}"

# Example 5
s5 = "(("
output5 = isValid(s5)
assert output5 == False, f"Test case 5 failed: {output5}"

print("All test cases passed!")