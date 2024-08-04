# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if not char_count.get(char) or char_count.get(char) == 0:
            return False
        else:
            char_count[char] -= 1

    return True

assert isAnagram(s1, t1) == True
assert isAnagram(s2, t2) == False

def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    counts = [0] * 26
    
    offset = ord('a')

    for char_s, char_t in zip(s, t):
        counts[ord(char_s) - offset] += 1
        counts[ord(char_t) - offset] -= 1

    return all(count == 0 for count in counts)

assert isAnagram2(s1, t1) == True
assert isAnagram2(s2, t2) == False
