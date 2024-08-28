# Given an integer x, return true if x is a palindrome, and false otherwise.

'''
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    x_string = str(x)
    start = 0
    end = len(x_string) - 1
    while start < len(x_string):
        if x_string[start] != x_string[end]:
            return False
        start += 1
        end -= 1
    return True


# Example 1
x = 121
expected_output = True
assert isPalindrome(x) == expected_output, f"Test failed for input {x}. Expected {expected_output} but got {isPalindrome(x)}."

# Example 2
x = -121
expected_output = False
assert isPalindrome(x) == expected_output, f"Test failed for input {x}. Expected {expected_output} but got {isPalindrome(x)}."

# Example 3
x = 10
expected_output = False
assert isPalindrome(x) == expected_output, f"Test failed for input {x}. Expected {expected_output} but got {isPalindrome(x)}."

print("All test cases passed!")