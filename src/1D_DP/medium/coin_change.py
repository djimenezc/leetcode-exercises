"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up
by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""
from typing import List

import pytest


class Solution:
    # Intuition
    # Keep minimum number of coins to make up each amount
    # Complexity
    # Time complexity: O(a∗c)
    # a is number of amount and c is number of coins
    #
    # Space complexity: O(a)
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [amount + 1] * amount

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        # After updating min_coins for all amounts from 1 to amount, return min_coins[-1] if it's not equal
        # to amount + 1.
        # If min_coins[-1] is still amount + 1, it means the amount cannot be made up by any combination of coins,
        # so return -1.
        return dp[-1] if dp[-1] != amount + 1 else -1


@pytest.mark.parametrize('coins, amount, expected_output', [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0)
])
def test_merge(coins, amount, expected_output):
    solution = Solution()
    output = solution.coinChange(coins, amount)

    assert output == expected_output
