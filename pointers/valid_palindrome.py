# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

"""
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

# Time complexity: O(n)
# Space complexity: O(n)
def isPalindrome(s: str) -> bool:
    palindrome = "".join(char.lower() for char in s if isalphanumeric(char))
        
    start = 0
    end = len(palindrome) - 1
    while start < end:
        if palindrome[start] != palindrome[end]:
            return False
        start += 1
        end -= 1
    
    return True

def isalphanumeric(c):
    return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))

# Test cases
input1 = "A man, a plan, a canal: Panama"
output1 = isPalindrome(input1)
assert output1 == True, f"Test case 1 failed: {output1}"

input2 = "race a car"
output2 = isPalindrome(input2)
assert output2 == False, f"Test case 2 failed: {output2}"

input3 = "0P"
output3 = isPalindrome(input3)
assert output3 == False, f"Test case 3 failed: {output3}"

print("All test cases passed!")

# Time complexity: O(n)
# Space complexity: O(1)
def isPalindromeImproved(s: str) -> bool:
    start = 0
    end = len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() == s[end].lower():
            start, end = start + 1, end - 1
        else:
            return False
    return True

# Test cases
input1 = "A man, a plan, a canal: Panama"
output1 = isPalindromeImproved(input1)
assert output1 == True, f"Test case 1 failed: {output1}"

input2 = "race a car"
output2 = isPalindromeImproved(input2)
assert output2 == False, f"Test case 2 failed: {output2}"

input3 = "0P"
output3 = isPalindromeImproved(input3)
assert output3 == False, f"Test case 3 failed: {output3}"

print("All test cases passed!")