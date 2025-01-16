"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally,
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List

import pytest


class Solution:

    # use a bottom-up dynamic programming approach with an auxiliary array. This method is similar to the in-place
    # solution but uses an extra array to store the minimum path sums. This can make the implementation clearer,
    # especially for understanding and debugging purposes.
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        memo = triangle[row - 1].copy()

        for r in range(row - 2, -1, -1):
            for c in range(r + 1):
                memo[c] = min(memo[c], memo[c + 1]) + triangle[r][c]

        return memo[0]

    # Approach: This approach modifies the triangle from the bottom up. Starting from the second last row,
    # each element is updated with the minimum path sum by adding the minimum of the two adjacent numbers from the row
    # directly below. This process continues until the top element contains the minimum path sum from top to bottom.
    #
    # Time Complexity: O(n^2), where n is the number of rows in the triangle.
    # Space Complexity: O(1), as we are modifying the triangle in place.
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # Start from the second last row and move upwards, from bottom up
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                min_sum = min(triangle[i + 1][j], triangle[i + 1][j + 1])
                current_val = triangle[i][j]
                triangle[i][j] = current_val + min_sum

        return triangle[0][0]


@pytest.mark.parametrize('triangle, expected_output', [
    ([[-1], [2, 3], [1, -1, -3]], -1),
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[-10]], -10),
])
def test_merge2(triangle, expected_output):
    solution = Solution()
    output = solution.minimumTotal2(triangle)

    assert output == expected_output
    output = solution.minimumTotal3(triangle)

    assert output == expected_output
