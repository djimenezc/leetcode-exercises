"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square
that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
from typing import List

import pytest


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return 0

        n = len(grid)
        m = len(grid[0])

        # Create an array dp of size cols to store the number of unique paths for each column.
        dp = [0] * m
        # 1, representing the number of ways to reach the starting cell (0, 0).
        dp[0] = 1

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    # indicating that there are no paths to reach this obstacle cell.
                    dp[c] = 0
                else:
                    # not in the leftmost column
                    if c > 0:
                        dp[c] += dp[c - 1]

        # number of unique paths to reach the bottom-right cell (rows - 1, cols - 1).
        return dp[m - 1]


@pytest.mark.parametrize('grid, expected_output', [
    ([[0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]], 2),
    ([[0, 1], [0, 0]], 1),
])
def test_merge(grid, expected_output):
    solution = Solution()
    output = solution.uniquePathsWithObstacles(grid)

    assert output == expected_output
