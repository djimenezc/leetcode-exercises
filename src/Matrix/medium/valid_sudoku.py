"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from collections import defaultdict
from typing import List

import pytest


class Solution:
    # We can't have duplicate numbers at each row, column and box(3 * 3), so it's good idea to have data of each row,
    # column and box whether we check current number is duplicate.
    # Time complexity: O(81) → O(1)
    # rows(9)∗columns(9)=81
    #
    # Space complexity: O(243) → O(1)
    # rows(81)+columns(81)+boxes(81)=243
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True


@pytest.mark.parametrize('board, expected_output', [
    ([["5", "3", ".", ".", "7", ".", ".", ".", "."]
         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True),
    ([["8", "3", ".", ".", "7", ".", ".", ".", "."]
         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False)
])
def test_merge(board, expected_output):
    solution = Solution()
    output = solution.isValidSudoku(board)

    assert output == expected_output
