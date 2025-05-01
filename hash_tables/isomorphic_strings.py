# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
"""

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for sc, tc in zip(s, t):
        if (s_to_t.get(sc) != tc) or (t_to_s.get(tc) != sc):
            if sc in s_to_t or tc in t_to_s:
                return False
            s_to_t[sc] = tc
            t_to_s[tc] = sc

    return True


assert isIsomorphic("egg", "add") == True, "Test Case 1 Failed"
assert isIsomorphic("foo", "bar") == False, "Test Case 2 Failed"
assert isIsomorphic("paper", "title") == True, "Test Case 3 Failed"

print("All test cases passed!")