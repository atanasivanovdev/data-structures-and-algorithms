# Given a string s, find the length of the longest substring without repeating characters.

'''
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSubstring(s: str) -> int:
    start, end = 0, 0
    char_set = set()
    longest_length = 0

    while end < len(s):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        longest_length = max(longest_length, (end - start + 1))
        end += 1
    return longest_length

# Test cases
input1 = "abcabcbb"
output1 = lengthOfLongestSubstring(input1)
assert output1 == 3, f"Test case 1 failed: {output1}"

input2 = "bbbbb"
output2 = lengthOfLongestSubstring(input2)
assert output2 == 1, f"Test case 2 failed: {output2}"

input3 = "pwwkew"
output3 = lengthOfLongestSubstring(input3)
assert output3 == 3, f"Test case 3 failed: {output3}"

input4 = "abcdef"
output4 = lengthOfLongestSubstring(input4)
assert output4 == 6, f"Test case 4 failed: {output4}"

input5 = "aab"
output5 = lengthOfLongestSubstring(input5)
assert output5 == 2, f"Test case 5 failed: {output5}"

input6 = "dvdf"
output6 = lengthOfLongestSubstring(input6)
assert output6 == 3, f"Test case 6 failed: {output6}"

print("All test cases passed!")