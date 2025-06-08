# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.


"""
Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".
"""

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
    
    if len(v1_parts) < len(v2_parts):
        return -1 if any(v2_parts[len(v1_parts):]) else 0
    elif len(v1_parts) > len(v2_parts):
        return 1 if any(v1_parts[len(v2_parts):]) else 0
    
    return 0

assert compareVersion("1.2", "1.10") == -1
assert compareVersion("1.01", "1.001") == 0
assert compareVersion("1.0", "1.0.0.0") == 0

print("All test cases passed!")