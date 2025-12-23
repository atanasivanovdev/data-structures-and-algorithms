# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

"""
Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""

def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    n = len(words)
    masks = [0] * n
    lengths = [len(word) for word in words]

    for i, word in enumerate(words):
        mask = 0
        for ch in word:
            mask |= 1 << (ord(ch) - ord('a'))
        masks[i] = mask

    max_product = 0

    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                max_product = max(
                    max_product,
                    lengths[i] * lengths[j]
                )

    return max_product


assert maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16
assert maxProduct(["a","ab","abc","d","cd","bcd","abcd"]) == 4
assert maxProduct(["a","aa","aaa","aaaa"]) == 0

print("All test cases passed!")