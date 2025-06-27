# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

"""
Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

from collections import Counter

def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
    result = ''.join(char * count for char, count in sorted_chars)
    return result


assert frequencySort("tree") == "eert" or frequencySort("tree") == "eetr"
assert frequencySort("cccaaa") == "cccaaa" or frequencySort("cccaaa") == "aaaccc"
assert frequencySort("Aabb") == "bbAa" or frequencySort("Aabb") == "bbaA"

print("All test cases passed!")