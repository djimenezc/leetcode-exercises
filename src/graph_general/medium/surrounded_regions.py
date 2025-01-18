"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region
cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to
return anything.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from collections import deque
from typing import List

import pytest


class Solution:
    def solve1(self, board: List[List[str]]) -> None:
        o = "O"

        n = len(board)
        m = len(board[0])

        Q = deque()

        for i in range(n):
            if board[i][0] == o:
                Q.append((i, 0))
            if board[i][m - 1] == o:
                Q.append((i, m - 1))

        for j in range(m):
            if board[0][j] == o:
                Q.append((0, j))
            if board[n - 1][j] == o:
                Q.append((n - 1, j))

        def inBounds(i, j):
            return (0 <= i < n) and (0 <= j < m)

        # BFS
        while Q:
            i, j = Q.popleft()
            board[i][j] = "#"

            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not inBounds(ii, jj):
                    continue
                if board[ii][jj] != o:
                    continue
                Q.append((ii, jj))
                board[ii][jj] = '#'

        for i in range(n):
            for j in range(m):
                if board[i][j] == o:
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = o

    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y):
            board[x][y] = '#'  # mark as protected
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == 'O':
                    dfs(x2, y2)

        # dfs from 'O's on border
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n - 1] == 'O': dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m - 1][j] == 'O': dfs(m - 1, j)

        # flip surrounding regions
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'  # change to 'X'
                elif board[x][y] == '#':
                    board[x][y] = 'O'  # change back to 'O'


@pytest.mark.parametrize('board, expected_output', [
    ([["X"]],
     [["X"]]),
    ([["X", "X", "X", "X"],
      ["X", "O", "O", "X"],
      ["X", "X", "O", "X"],
      ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "O", "X", "X"]]),
])
def test_merge(board, expected_output):
    solution = Solution()
    solution.solve1(board)

    assert board == expected_output
    solution.solve2(board)

    assert board == expected_output
