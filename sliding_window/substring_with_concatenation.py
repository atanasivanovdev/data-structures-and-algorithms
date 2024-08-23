# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 
'''
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
'''
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    result = []
    if not words:
        return result
    
    counter = 0
    left = 0
    right = 0

    while right < len(s):

        right += 1

    return result


# Test case 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
expected_output1 = [0, 9]
assert findSubstring(s1, words1) == expected_output1, f"Test case 1 failed: {findSubstring(s1, words1)} != {expected_output1}"

# Test case 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
expected_output2 = []
assert findSubstring(s2, words2) == expected_output2, f"Test case 2 failed: {findSubstring(s2, words2)} != {expected_output2}"

# Test case 3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
expected_output3 = [6, 9, 12]
assert findSubstring(s3, words3) == expected_output3, f"Test case 3 failed: {findSubstring(s3, words3)} != {expected_output3}"

print("All test cases passed!")