# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

"""
Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1
"""

from collections import Counter

def numTilePossibilities(tiles):
    """
    :type tiles: str
    :rtype: int
    """
    count = Counter(tiles)

    def backtrack(counter):
        total = 0
        for ch in counter:
            if counter[ch] > 0:
                total += 1
                counter[ch] -= 1
                total += backtrack(counter)
                counter[ch] += 1
        return total

    return backtrack(count)


assert numTilePossibilities("AAB") == 8
assert numTilePossibilities("AAABBC") == 188
assert numTilePossibilities("V") == 1

print("All test cases passed!")