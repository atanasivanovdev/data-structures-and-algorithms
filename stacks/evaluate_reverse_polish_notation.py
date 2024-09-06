# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

'''
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

from typing import List
from collections import deque

def evalRPN(tokens: List[str]) -> int:
    numbers = deque()

    operations = {
        "+": lambda b, a: a + b,
        "-": lambda b, a: a - b,
        "*": lambda b, a: a * b,
        "/": lambda b, a: int(a / b)
    }

    for token in tokens:
        if token in operations:
            last, previous = numbers.pop(), numbers.pop()
            numbers.append(operations[token](last, previous))
        else:
            numbers.append(int(token))

    return numbers.pop()


# Example 1
tokens1 = ["2", "1", "+", "3", "*"]
expected_output1 = 9
assert evalRPN(tokens1) == expected_output1, f"Test case 1 failed: {evalRPN(tokens1)} != {expected_output1}"

# Example 2
tokens2 = ["4", "13", "5", "/", "+"]
expected_output2 = 6
assert evalRPN(tokens2) == expected_output2, f"Test case 2 failed: {evalRPN(tokens2)} != {expected_output2}"

# Example 3
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
expected_output3 = 22
assert evalRPN(tokens3) == expected_output3, f"Test case 3 failed: {evalRPN(tokens3)} != {expected_output3}"

print("All test cases passed!")