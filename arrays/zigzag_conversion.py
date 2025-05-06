# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 
"""
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    cur_row = 0
    going_down = False

    for char in s:
        rows[cur_row] += char
        if cur_row == 0:
            going_down = True
        elif cur_row == numRows - 1:
            going_down = False
        cur_row += 1 if going_down else -1

    return ''.join(rows)


assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Test Case 1 Failed"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Test Case 2 Failed"
assert convert("A", 1) == "A", "Test Case 3 Failed"

print("All test cases passed!")