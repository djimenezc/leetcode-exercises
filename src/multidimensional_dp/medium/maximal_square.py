"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List

import pytest


class Solution:

    # n define a 2D array dp where dp[i][j] represents the maximum size of a square that can be formed at
    # position (i, j) such that all its elements are 1's. We can fill this array using the following recurrence relation:
    #
    # dp[i][j] = 0 if matrix[i][j] == '0'
    # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i][j] == '1'
    # The first condition means that if the current cell has a value of 0, we can't form a square with it.
    # The second condition means that if the current cell has a value of 1, we can form a square with it,
    # but we need to check the values of the cells to the left, top, and top-left of it to determine
    # the maximum size of the square.
    #
    # We also need to keep track of the maximum size of the square seen so far, and return its area.
    # Time complexity:
    # Beats
    # 88.37% O(m*n), where m and n are the dimensions of the matrix.
    #
    # Space complexity:
    # Beats
    # 88.43% O(m*n), where m and n are the dimensions of the matrix,
    # since we are using a 2D array of the same size as the matrix to store the dp values.
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        if m * n == 1:
            return int(matrix[0][0])

        max_size = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # First row or column, so the maximum size of the square is 1
                        dp[i][j] = 1
                    else:
                        # Check the values of the cells to the left, top, and top-left of the current cell
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                        # Update the max size of the square seen so far
                    max_size = max(max_size, dp[i][j])

        return max_size * max_size


@pytest.mark.parametrize('matrix, expected_output', [
    # ([["0"]], 0),
    ([["0", "1"],
      ["1", "0"]],
     1),
    ([["1", "0", "1", "0", "0"],
      ["1", "0", "1", "1", "1"],
      ["1", "1", "1", "1", "1"],
      ["1", "0", "0", "1", "0"]],
     4),
])
def test_merge(matrix, expected_output):
    solution = Solution()
    output = solution.maximalSquare(matrix)

    assert output == expected_output
