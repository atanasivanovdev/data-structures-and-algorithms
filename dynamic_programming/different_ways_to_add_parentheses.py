# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

"""
Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

def diffWaysToCompute(expression):
    def compute(left, right, op):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right

    if expression.isdigit():
        return [int(expression)]

    results = []
    for i, char in enumerate(expression):
        if char in "+-*":
            left_results = diffWaysToCompute(expression[:i])
            right_results = diffWaysToCompute(expression[i + 1:])
            for left in left_results:
                for right in right_results:
                    results.append(compute(left, right, char))

    return results


assert sorted(diffWaysToCompute("2-1-1")) == sorted([0, 2])
assert sorted(diffWaysToCompute("2*3-4*5")) == sorted([-34, -14, -10, -10, 10])

print("All test cases passed!")