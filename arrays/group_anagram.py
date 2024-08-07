# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
from typing import List
from collections import defaultdict
# Input 1
input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output1 = [["eat","tea","ate"],["tan","nat"],["bat"]]

# Input 2
input2 = [""]
output2 = [[""]]

# Input 3
input3 = ["a"]
output3 = [["a"]]

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for char in str:
            count[ord(char) - ord('a')] += 1
            
        anagrams[tuple(count)].append(str)
    return anagrams.values()

assert groupAnagrams(input1) == output1
assert groupAnagrams(input2) == output2
assert groupAnagrams(input3) == output3