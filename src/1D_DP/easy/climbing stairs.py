"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

import pytest


class Solution:
    # Why This Approach Works
    # This solution follows the principles of dynamic programming by breaking the problem into smaller overlapping
    # subproblems. By using only three variables, it optimizes memory usage compared to a full
    # array-based implementation.
    def climbStairs(self, n: int) -> int:

        if n <= 3: return n

        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur

    # RECURSION
    # Explanation: The recursive solution uses the concept of Fibonacci numbers to solve the problem. It calculates
    # the number of ways to climb the stairs by recursively calling the climbStairs function for (n-1) and (n-2) steps.
    # However, this solution has exponential time complexity (O(2^n)) due to redundant calculations.
    # Time exceeded
    def climbStairs0(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # Memoization
    # Explanation: The memoization solution improves the recursive solution by introducing memoization,
    # which avoids redundant calculations. We use an unordered map (memo) to store the already computed results
    # for each step n. Before making a recursive call, we check if the result for the given n exists in the memo.
    # If it does, we return the stored value; otherwise, we compute the result recursively and store it in the memo
    # for future reference.
    def climbStairs2(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]

    # Tabulation
    # Explanation: The tabulation solution eliminates recursion and uses a bottom-up approach to solve the problem
    # iteratively. It creates a DP table (dp) of size n+1 to store the number of ways to reach each step.
    # The base cases (0 and 1 steps) are initialized to 1 since there is only one way to reach them. Then,
    # it iterates from 2 to n, filling in the DP table by summing up the values for the previous two steps.
    # Finally, it returns the value in the last cell of the DP table, which represents the total number of
    # ways to reach the top.
    def climbStairs3(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs4(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr


@pytest.mark.parametrize('n, expected_output', [
    (2, 2),
    (3, 3),
])
def test_merge(n, expected_output):
    solution = Solution()
    output = solution.climbStairs(n)

    assert output == expected_output
    output = solution.climbStairs2(n)

    assert output == expected_output
    output = solution.climbStairs3(n)

    assert output == expected_output
    output = solution.climbStairs4(n)

    assert output == expected_output
