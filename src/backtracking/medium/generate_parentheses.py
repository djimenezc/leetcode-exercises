"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List

import pytest


class Solution:

    # Increase number of open parentheses until we reach n at first
    # Complexity
    # Time complexity:O(2 2 n)
    # Space complexity: O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_parenthesis, close_parenthesis, comb):
            #  If the number of open and close parentheses are equal and the total length of the string is 2 * n,
            #  it means we have a valid combination.
            if open_parenthesis == close_parenthesis and open_parenthesis + close_parenthesis == 2 * n:
                res.append(comb)
                return

            # If the number of open parentheses used (openP) is less than n, we can add another open parenthesis.
            if open_parenthesis < n:
                backtrack(open_parenthesis + 1, close_parenthesis, comb + "(")

            #  If the number of close parentheses used (closeP) is less than the number of open parentheses,
            #  we can add a close parenthesis to maintain balance
            if close_parenthesis < open_parenthesis:
                backtrack(open_parenthesis, close_parenthesis + 1, comb + ")")

        backtrack(0, 0, "")

        return res


@pytest.mark.parametrize('n, expected_output', [
    (1, ["()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (2, ["(())", "()()"]),
])
def test_merge(n, expected_output):
    solution = Solution()
    output = solution.generateParenthesis(n)

    assert output == expected_output
