# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

"""
Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]"
"""

from typing import List


def findWords(words: List[str]) -> List[str]:
    first_row = set("qwertyuiop")
    second_row = set("asdfghjkl")
    third_row = set("zxcvbnm")
    
    result = []
    for word in words:
        word_set = set(word.lower())
        if word_set.issubset(first_row) or word_set.issubset(second_row) or word_set.issubset(third_row):
            result.append(word)
    
    return result


assert findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"], f"Test case 1 failed: {findWords(['Hello', 'Alaska', 'Dad', 'Peace'])} != ['Alaska', 'Dad']"

assert findWords(["omk"]) == [], f"Test case 2 failed: {findWords(['omk'])} != []"

print("All test cases passed!")