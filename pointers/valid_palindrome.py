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

def isPalindrome(s: str) -> bool:
    palindrome = "".join(char.lower() for char in s if char.isalnum())
        
    start = 0
    end = len(palindrome) - 1
    while start <= end:
        if palindrome[start] != palindrome[end]:
            return False
        start += 1
        end -= 1
    
    return True

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