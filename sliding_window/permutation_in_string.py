# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

'''
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    s1_count, s2_count = [0] * 26, [0] * 26
    
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1
    
    if s1_count == s2_count:
        return True
    
    for i in range(len(s1), len(s2)):
        s2_count[ord(s2[i]) - ord('a')] += 1
        s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        if s1_count == s2_count:
            return True
    
    return False


# Test cases
s1_1 = "ab"
s2_1 = "eidbaooo"
output1 = checkInclusion(s1_1, s2_1)
assert output1 == True, f"Test case 1 failed: {output1}"

s1_2 = "ab"
s2_2 = "eidboaoo"
output2 = checkInclusion(s1_2, s2_2)
assert output2 == False, f"Test case 2 failed: {output2}"

s1_3 = "adc"
s2_3 = "dcda"
output3 = checkInclusion(s1_3, s2_3)
assert output3 == True, f"Test case 3 failed: {output3}"

s1_4 = "hello"
s2_4 = "ooolleoooleh"
output4 = checkInclusion(s1_4, s2_4)
assert output4 == False, f"Test case 4 failed: {output4}"

s1_5 = "abc"
s2_5 = "ccccbbbbaaaa"
output5 = checkInclusion(s1_5, s2_5)
assert output5 == False, f"Test case 5 failed: {output5}"

s1_6 = "a"
s2_6 = "a"
output6 = checkInclusion(s1_6, s2_6)
assert output6 == True, f"Test case 6 failed: {output6}"

s1_7 = "abc"
s2_7 = "cbadabac"
output7 = checkInclusion(s1_7, s2_7)
assert output7 == True, f"Test case 7 failed: {output7}"
