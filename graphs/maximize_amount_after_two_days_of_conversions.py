# You are given a string initialCurrency, and you start with 1.0 of initialCurrency.

# You are also given four arrays with currency pairs (strings) and rates (real numbers):

# pairs1[i] = [startCurrencyi, targetCurrencyi] denotes that you can convert from startCurrencyi to targetCurrencyi at a rate of rates1[i] on day 1.
# pairs2[i] = [startCurrencyi, targetCurrencyi] denotes that you can convert from startCurrencyi to targetCurrencyi at a rate of rates2[i] on day 2.
# Also, each targetCurrency can be converted back to its corresponding startCurrency at a rate of 1 / rate.
# You can perform any number of conversions, including zero, using rates1 on day 1, followed by any number of additional conversions, including zero, using rates2 on day 2.

# Return the maximum amount of initialCurrency you can have after performing any number of conversions on both days in order.

# Note: Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.

"""
Example 1:
Input: initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]
Output: 720.00000
Explanation:
To get the maximum amount of EUR, starting with 1.0 EUR:
On Day 1:
Convert EUR to USD to get 2.0 USD.
Convert USD to JPY to get 6.0 JPY.
On Day 2:
Convert JPY to USD to get 24.0 USD.
Convert USD to CHF to get 120.0 CHF.
Finally, convert CHF to EUR to get 720.0 EUR.

Example 2:
Input: initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]
Output: 1.50000
Explanation:
Converting NGN to EUR on day 1 and EUR to NGN using the inverse rate on day 2 gives the maximum amount.

Example 3:
Input: initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]
Output: 1.00000
Explanation:
In this example, there is no need to make any conversions on either day.
"""

from collections import defaultdict, deque

def maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2):
    """
    :type initialCurrency: str
    :type pairs1: List[List[str]]
    :type rates1: List[float]
    :type pairs2: List[List[str]]
    :type rates2: List[float]
    :rtype: float
    """
    def build_graph(pairs, rates):
        graph = defaultdict(list)
        for (u, v), r in zip(pairs, rates):
            graph[u].append((v, r))
            graph[v].append((u, 1.0 / r))
        return graph

    def max_conversion(start_amounts, graph):
        amount = dict(start_amounts)
        q = deque(start_amounts.keys())

        while q:
            u = q.popleft()
            for v, rate in graph[u]:
                new_val = amount[u] * rate
                if new_val > amount.get(v, 0):
                    amount[v] = new_val
                    q.append(v)
        return amount

    graph1 = build_graph(pairs1, rates1)
    day1_amounts = max_conversion({initialCurrency: 1.0}, graph1)

    graph2 = build_graph(pairs2, rates2)
    day2_amounts = max_conversion(day1_amounts, graph2)

    return day2_amounts.get(initialCurrency, 0.0)


assert maxAmount("EUR", [["EUR","USD"],["USD","JPY"]], [2.0,3.0], [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], [4.0,5.0,6.0]) == 720.0
assert maxAmount("NGN", [["NGN","EUR"]], [9.0], [["NGN","EUR"]], [6.0]) == 1.5
assert maxAmount("USD", [["USD","EUR"]], [1.0], [["EUR","JPY"]], [10.0]) == 1.0

print("All test cases passed!")