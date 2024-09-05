# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''

def reverse(x: int) -> int:
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        pop = x % 10
        x //= 10

        result = result * 10 + pop
    
    result *= sign

    if result < -pow(2, 31) or result > pow(2, 31) - 1:
        return 0

    return result


# Example 1
x = 123
expected_output = 321
assert reverse(x) == expected_output, f"Expected {expected_output} but got {reverse(x)}"

# Example 2
x = -123
expected_output = -321
assert reverse(x) == expected_output, f"Expected {expected_output} but got {reverse(x)}"

# Example 3
x = 120
expected_output = 21
assert reverse(x) == expected_output, f"Expected {expected_output} but got {reverse(x)}"

print("All test cases passed!")