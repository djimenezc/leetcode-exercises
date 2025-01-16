"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""
from typing import List

import pytest


class Solution:
    # O(mn) since we visit each cell once.
    # The space complexity is also O(mn) since we use the dp array to store the intermediate results.
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # dp = grid[::]

        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]

        return grid[n - 1][m - 1]


@pytest.mark.parametrize('grid, expected_output', [
    ([[1, 3, 1],
      [1, 5, 1],
      [4, 2, 1]], 7),
    ([[1, 2, 3],
      [4, 5, 6]], 12),
])
def test_merge(grid, expected_output):
    solution = Solution()
    output = solution.minPathSum(grid)

    assert output == expected_output
