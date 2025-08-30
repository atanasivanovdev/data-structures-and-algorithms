# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

"""
Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""

def findDifferentBinaryString(nums):
    """
    :type nums: List[str]
    :rtype: str
    """
    n = len(nums)

    all_binaries = {
        format(i, f'0{n}b')
        for i in range(2 ** n)
    }

    unused_binaries = all_binaries - set(nums)

    return unused_binaries.pop()


assert findDifferentBinaryString(["01","10"]) in {"00", "11"}
assert findDifferentBinaryString(["00","01"]) in {"10", "11"}
assert findDifferentBinaryString(["111","011","001"]) in {"000", "010", "100", "110"}

print("All test cases passed!")