# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

'''
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

from collections import defaultdict

# Time complexity: O(n)
# Space complexity: O(1)
def characterReplacement(s: str, k: int) -> int:
    left = right = 0
    longest_sequence = 0
    char_count = defaultdict(int)
    while right < len(s):
        char_count[s[right]] += 1
        while ((right - left) + 1) - max(char_count.values()) > k:
            char_count[s[left]] -= 1
            left += 1
        longest_sequence = max(longest_sequence, ((right - left) + 1))
        right += 1
    return longest_sequence


# Test cases
input1 = "ABAB"
k1 = 2
output1 = characterReplacement(input1, k1)
assert output1 == 4, f"Test case 1 failed: {output1}"

input2 = "AABABBA"
k2 = 1
output2 = characterReplacement(input2, k2)
assert output2 == 4, f"Test case 2 failed: {output2}"

input3 = "ABAA"
k3 = 1
output3 = characterReplacement(input3, k3)
assert output3 == 4, f"Test case 3 failed: {output3}"

input4 = "AAAA"
k4 = 2
output4 = characterReplacement(input4, k4)
assert output4 == 4, f"Test case 4 failed: {output4}"

input5 = "AABA"
k5 = 0
output5 = characterReplacement(input5, k5)
assert output5 == 2, f"Test case 5 failed: {output5}"

print("All test cases passed!")
