"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""
from typing import List

import pytest


class Solution:

    # To solve this question we will use Greedy Algorithm.
    #
    # Now if you don't know anything about Greedy algorithm here is the small explanation of the Greedy.
    #
    # Greedy algorithms are a class of algorithms that make locally optimal choices at each step with the hope
    # of finding a global optimum solution. In these algorithms, decisions are made based on the information
    # available at the current moment without considering the consequences of these decisions in the future.
    # The key idea is to select the best possible choice at each step, leading to a solution that may not always
    # be the most optimal but is often good enough for many problems.
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        start = prices[0]
        len1 = len(prices)

        for i in range(0, len1):
            if start < prices[i]:
                max += prices[i] - start
            start = prices[i]

        return max

@pytest.mark.parametrize('nums, output_expected', [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
])
def test_merge(nums, output_expected):
    solution = Solution()
    output = solution.maxProfit(nums)

    assert output == output_expected
