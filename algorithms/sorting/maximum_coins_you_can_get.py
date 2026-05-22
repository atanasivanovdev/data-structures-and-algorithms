# There are 3n piles of coins of varying size. You and your friends will take piles of coins as follows:

# In each step, you will choose any 3 piles of coins and take one of them. The friend with you will take the pile with the maximum coins, and your friend will take the pile with the min coins. You will take the last pile.

# Repeat the process until there are no more piles of coins.

# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins you can get.

"""
Example 1:
Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice picks the pile with 8 coins, you pick the pile with 7 coins and Bob picks the last one.
Choose the triplet (1, 2, 4), Alice picks the pile with 4 coins, you pick the pile with 2 coins and Bob picks the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.

Example 2:
Input: piles = [2,4,5]
Output: 4
Explanation: Choose the triplet (2, 4, 5), Alice picks 5, you pick 4, Bob picks 2.

Example 3:
Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18
Explanation: Optimal selection of triplets to maximize your coins.
"""

def maxCoins(piles):
    """
    :type piles: List[int]
    :rtype: int
    """
    piles.sort(reverse=True)
    
    n = len(piles) // 3
    coins = 0
    
    for i in range(1, 2 * n, 2):
        coins += piles[i]
    
    return coins


assert maxCoins([2,4,1,2,7,8]) == 9
assert maxCoins([2,4,5]) == 4
assert maxCoins([9,8,7,6,5,1,2,3,4]) == 18

print("All test cases passed!")
