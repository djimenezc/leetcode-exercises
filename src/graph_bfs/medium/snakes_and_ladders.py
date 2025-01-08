"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.



Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1


Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.
"""
import collections
from typing import List

import pytest


class Solution:

    # Intuition :
    # For each step we do the following:
    #
    # roll dice (and check all 6 possible values, marking each as visited)
    # check if we land on a ladder and take it (no possibility to skip it, we must take it)
    # remember where to continue next time (add the new position to the queue)
    # Now let’s take a look at scenarios:
    #
    # Just step starting from square 1 with a dice where 6 is the best
    # Complexity
    # Time complexity :O(n^2)
    # Space complexity:O(n^2)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def label_to_position(label):
            # The divmod() function returns a tuple containing the quotient  and the remainder when argument1
            # (dividend) is divided by argument2 (divisor).
            r, c = divmod(label - 1, n)
            if r % 2 == 0:
                return n - 1 - r, c
            else:
                return n - 1 - r, n - 1 - c

        seen = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n * n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n * n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step + 1))
        return -1


@pytest.mark.parametrize('board, expected_output', [
    ([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],
     4),
    ([[-1,-1],[-1,3]],1),
])
def test_merge(board, expected_output):
    solution = Solution()
    output = solution.snakesAndLadders(board)

    assert output == expected_output
