"""
Given a rod of length n inches and an array price[]. price[i] denotes the value of a piece of length i. The task is to
determine the maximum value obtainable by cutting up the rod and selling the pieces.

Examples:

Input: price[] =  [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation:  The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.


Input : price[] =  [3, 5, 8, 9, 10, 17, 17, 20]
Output : 24
Explanation : The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.


Input : price[] =  [3]
Output : 3
Explanation: There is only 1 way to pick a piece of length 1.


In the rod cutting problem, the goal is to determine the maximum profit that can be obtained by cutting a rod into
smaller pieces and selling them, given a price list for each possible piece length. The approach involves considering
all possible cuts for the rod and recursively calculating the maximum profit for each cut. For detailed explanation
and approaches, refer to Rod Cutting.
"""

import pytest


class Solution:
    # Python program to find maximum
    # profit from rod of size n, memoization
    # O(n^2) Time and O(n) Space
    def cut_rod_recur(self, i, price, memo):

        # Base case
        if i == 0:
            return 0

        # If value is memoized
        if memo[i - 1] != -1:
            return memo[i - 1]

        ans = 0

        # Find maximum value for each cut.
        # Take value of rod of length j, and
        # recursively find value of rod of
        # length (i-j).
        for j in range(1, i + 1):
            ans = max(ans, price[j - 1] + self.cut_rod_recur(i - j, price, memo))

        memo[i - 1] = ans
        return ans

    def cut_rod(self, price):
        n = len(price)
        memo = [-1] * n
        return self.cut_rod_recur(n, price, memo)

    # Python program to find maximum
    # profit from rod of size n
    # O(n^2) Time and O(n) Space
    def cut_rod_tab(self, price):
        n = len(price)
        dp = [0] * (n + 1)

        # Find maximum value for all
        # rod of length i.
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], price[j - 1] + dp[i - j])

        return dp[n]


@pytest.mark.parametrize('price, expected_output', [
    ([1, 5, 8, 9, 10, 17, 17, 20], 22),
    ([3, 5, 8, 9, 10, 17, 17, 20], 24),
    ([3], 3),
])
def test_merge(price, expected_output):
    solution = Solution()
    output = solution.cut_rod(price)

    assert output == expected_output
    output = solution.cut_rod_tab(price)

    assert output == expected_output
