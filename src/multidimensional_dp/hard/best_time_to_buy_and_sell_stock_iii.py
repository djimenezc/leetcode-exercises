"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions
at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
import math
from collections import defaultdict
from typing import List

import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold_stock, keep_cash = 0, 1

        # dictionary
        # key: state, kth-transaction
        # value: corresponding profit
        dp = defaultdict(int)

        # No free lunch, impossible to have stock before first trading day
        dp[(hold_stock, 0)] = -math.inf
        dp[(hold_stock, 1)] = -math.inf
        dp[(hold_stock, 2)] = -math.inf

        for stock_price in prices:
            ## For 1st transaction:
            # Either we kept cash already, or we just sell out stock today
            dp[keep_cash, 1] = max(dp[keep_cash, 1], dp[hold_stock, 1] + stock_price)

            # Either we had stock already, or we just buy in stock today ( add one more transaction)
            dp[hold_stock, 1] = max(dp[hold_stock, 1], dp[keep_cash, 0] - stock_price)

            ## For 2nd transaction:
            # Either we kept cash already, or we just sell out stock today
            dp[keep_cash, 2] = max(dp[keep_cash, 2], dp[hold_stock, 2] + stock_price)

            # Either we had stock already, or we just buy in stock today ( add one more transaction)
            dp[hold_stock, 2] = max(dp[hold_stock, 2], dp[keep_cash, 1] - stock_price)

        # Maximal profit must be keep_cash on last day
        # (This means we cash out and sell stocks finally)
        return dp[keep_cash, 2]

    # The basic idea is to iterate over the array of stock prices and update four variables:
    #
    # buy1 - the minimum price seen so far for the first transaction
    # sell1 - the maximum profit seen so far for the first transaction
    # buy2 - the minimum price seen so far for the second transaction, taking into account the profit from
    # the first transaction
    # sell2 - the maximum profit seen so far for the second transaction
    # At the end of the iteration, the value of sell2 is returned as the maximum profit achievable with
    # two transactions.
    #
    # Here's how the algorithm works step by step for the input [3,3,5,0,0,3,1,4]:
    #
    # Initialize buy1, buy2, sell1, and sell2 to inf, inf, 0, and 0, respectively.
    # For the first price of 3, update buy1 to 3, sell1 to 0, buy2 to -3, and sell2 to 0.
    # For the second price of 3, update buy1 to 3, sell1 to 0, buy2 to -3, and sell2 to 0 (no change).
    # For the third price of 5, update buy1 to 3, sell1 to 2, buy2 to -1, and sell2 to 2.
    # For the fourth price of 0, update buy1 to 0, sell1 to 2, buy2 to -1, and sell2 to 2 (no change).
    # For the fifth price of 0, update buy1 to 0, sell1 to 2, buy2 to -2, and sell2 to 2 (no change).
    # For the sixth price of 3, update buy1 to 0, sell1 to 3, buy2 to 0, and sell2 to 3.
    # For the seventh price of 1, update buy1 to 0, sell1 to 3, buy2 to -3, and sell2 to 3 (no change).
    # For the eighth price of 4, update buy1 to 0, sell1 to 4, buy2 to 0, and sell2 to 4
    # Complexity
    # Time complexity:
    # Beats
    # O(N)
    #
    # Space complexity:
    # Beats
    # O(1)
    def maxProfit2(self, prices: List[int]) -> int:
        # the input array is empty.
        if not prices:
            return 0

        # initialize variables for first buy, first sell, second buy, and second sell
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0

        # iterate over prices to update buy and sell values
        for price in prices:
            # update first buy and sell values
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            # update second buy and sell values
            # using the profit from your first trade (sell1) to reduce the cost (price in buy2) of your second trade.
            buy2 = min(buy2, price - sell1)
            # is the total profit, not the profit of the current transaction.
            sell2 = max(sell2, price - buy2)

        return sell2

@pytest.mark.parametrize('prices, expected_output', [
    ([3,3,5,0,0,3,1,4], 6),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
])
def test_merge(prices, expected_output):
    solution = Solution()
    output = solution.maxProfit(prices)

    assert output == expected_output
    output = solution.maxProfit2(prices)

    assert output == expected_output
