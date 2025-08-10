# Given a string s and an integer k, return true if you can use all the characters in s to construct non-empty k palindrome strings or false otherwise.

"""
Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
"""

def canConstruct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: bool
    """
    if k > len(s):
        return False
    
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)

    return odd_count <= k


assert canConstruct("annabelle", 2) == True
assert canConstruct("leetcode", 3) == False
assert canConstruct("true", 4) == True

print("All tests passed!")