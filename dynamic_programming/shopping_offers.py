# In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.
# You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

# You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

# Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.

"""
Example 1:
Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14

Example 2:
Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
Output: 11
"""

def shoppingOffers(price, special, needs):
    """
    :type price: List[int]
    :type special: List[List[int]]
    :type needs: List[int]
    :rtype: int
    """
    n = len(price)

    valid_special = []
    for offer in special:
        offer_items = offer[:n]
        offer_price = offer[n]
        direct_cost = sum(offer_items[i] * price[i] for i in range(n))
        if offer_price < direct_cost:
            valid_special.append(offer)

    memo = {}

    def dfs(curr_needs):
        key = tuple(curr_needs)
        if key in memo:
            return memo[key]

        best = sum(curr_needs[i] * price[i] for i in range(n))

        for offer in valid_special:
            next_needs = []
            for i in range(n):
                if offer[i] > curr_needs[i]:
                    break
                next_needs.append(curr_needs[i] - offer[i])
            else:
                best = min(best, offer[n] + dfs(next_needs))

        memo[key] = best
        return best

    return dfs(needs)


assert shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]) == 14
assert shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]) == 11

print("All test cases passed!")
