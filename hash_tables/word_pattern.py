# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 
"""
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False  # Lengths must match

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False  # Mismatch in mapping
        else:
            if word in word_to_char:
                return False  # One word maps to multiple chars
            char_to_word[char] = word
            word_to_char[word] = char

    return True

# Test case 1
pattern = "abba"
s = "dog cat cat dog"
assert wordPattern(pattern, s) == True, "Test case 1 failed"

# Test case 2
pattern = "abba"
s = "dog cat cat fish"
assert wordPattern(pattern, s) == False, "Test case 2 failed"

# Test case 3
pattern = "aaaa"
s = "dog cat cat dog"
assert wordPattern(pattern, s) == False, "Test case 3 failed"

print("All test cases passed!")