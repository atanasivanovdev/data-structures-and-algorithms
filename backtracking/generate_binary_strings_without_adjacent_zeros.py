# You are given a positive integer n.

# A binary string x is valid if all substrings of x of length 2 contain at least one "1".

# Return all valid strings with length n, in any order.

"""
Example 1:
Input: n = 3
Output: ["010","011","101","110","111"]
Explanation:
The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:
Input: n = 1
Output: ["0","1"]
Explanation:
The valid strings of length 1 are: "0" and "1".
"""

def validStrings(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []

    def backtrack(current):
        if len(current) == n:
            result.append(current)
            return

        if not current or current[-1] != '0':
            backtrack(current + '0')
        backtrack(current + '1')

    backtrack("")
    return result


assert validStrings(3) == ["010","011","101","110","111"]
assert validStrings(1) == ["0","1"]

print("All test cases passed!")