# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
from typing import List

# Time complexity: O(n)
# Space complexity: O(1)
def maxProfit(prices: List[int]) -> int:
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[left] >= prices[right]:
            left = right
        else:
            max_profit = max(max_profit, (prices[right] - prices[left]))
            
        right += 1

    return max_profit


# Test cases
input1 = [7, 1, 5, 3, 6, 4]
output1 = maxProfit(input1)
assert output1 == 5, f"Test case 1 failed: {output1}"

input2 = [7, 6, 4, 3, 1]
output2 = maxProfit(input2)
assert output2 == 0, f"Test case 2 failed: {output2}"

input3 = [2, 4, 1]
output3 = maxProfit(input3)
assert output3 == 2, f"Test case 3 failed: {output3}"

input4 = [1, 2, 3, 4, 5]
output4 = maxProfit(input4)
assert output4 == 4, f"Test case 4 failed: {output4}"

input5 = [3, 2, 6, 5, 0, 3]
output5 = maxProfit(input5)
assert output5 == 4, f"Test case 5 failed: {output5}"

print("All test cases passed!")