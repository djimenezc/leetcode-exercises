"""
Let’s say you have a set of coins with values [1, 2, 5, 10] and you need to
 give minimum number of coin to someone change for 39.
"""
from typing import List

import pytest


class Solution:
    # Greedy approach
    def min_coins(self, coins: List[int], target: int) -> int:

        coins.sort()
        acc = 0
        min_coins = 0

        for i in range(len(coins) - 1, -1, -1):
            while acc != target:
                if target - acc >= coins[i]:
                    acc += coins[i]
                    min_coins += 1
                else:
                    break
            if acc == target:
                return min_coins

        return min_coins

    def min_coins2(self, coins: list[int], amount: int):
        n = len(coins)
        coins.sort()
        res = 0

        # Start from the coin with the highest denomination
        for i in range(n - 1, -1, -1):
            if amount >= coins[i]:
                # Find the maximum number of ith coin we can use
                cnt = amount // coins[i]

                # Add the count to result
                res += cnt

                # Subtract the corresponding amount from the total amount
                amount -= cnt * coins[i]

            # Break if there is no amount left
            if amount == 0:
                break

        return res


@pytest.mark.parametrize('coins, target, expected_output', [
    ([1, 2, 5, 10], 39, 6),
])
def test_merge(coins, target, expected_output):
    solution = Solution()
    output = solution.min_coins(coins, target)

    assert output == expected_output
    output = solution.min_coins2(coins, target)

    assert output == expected_output
