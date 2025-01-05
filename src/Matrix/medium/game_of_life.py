"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches upon the border of the array (i.e., live cells reach the border).
How would you address these problems?
"""
from typing import List

import pytest


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ## RC ##
        ## APPROACH : IN-PLACE MANIPULATION ##
        #  when the value needs to be updated, we do not just change  0 to 1 / 1 to 0
        #  but we do in increments and decrements of 2. (table explains)
        ##   previous value state change  current state   current value
        ##   0              no change     dead            0
        ##   1              no change     live            1
        ##   0              changed (+2)  live            2
        ##   1              changed (-2)  dead            -1

		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(1) ##

        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0                # live neighbors count
                for x, y in directions: # check and count neighbors in all directions
                    if ( i + x < len(board) and i + x >= 0 ) and ( j + y < len(board[0]) and j + y >=0 ) and abs(board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):     # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:                  # Rule 4
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if(board[i][j] > 0) else 0
        return board


@pytest.mark.parametrize('board, expected_output', [
    ([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]),
    ([[1,1],[1,0]], [[1,1],[1,1]])
])
def test_merge(board, expected_output):
    solution = Solution()
    solution.gameOfLife(board)

    assert board == expected_output
