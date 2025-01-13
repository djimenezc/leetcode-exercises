"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List

import pytest


class Solution:
    # Simply check 4 directions from every place and if we find the next target character, then move to that place.
    #
    # But problem is that we don't know current length of path(= word), so every time we move to a new place,
    # count 1 as a length of path, so that when the path length is equal to input word, we can return True.
    def exist1(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, k):
            if k == len(word):
                return True

            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in visited or board[r][c] != word[k]:
                return False

            visited.add((r, c))
            res = dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1)
            visited.remove((r, c))
            return res

        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

    # Complexity
    # Time complexity:
    # O(m∗n∗4
    # l
    #  ), where m and n are the dimensions of the grid and l is the length of the word. The 4
    # l
    #   factor represents the maximum number of recursive calls we may have to make for each starting cell.
    # Space complexity:
    # O(l), where l is the length of the word. The space complexity is primarily due to the recursive stack depth
    # during the DFS traversal.
    def exist2(self, board, word):
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = ''

            if (backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1)
                    or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1)):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False


@pytest.mark.parametrize('board, word, expected_output', [
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCD", False)
])
def test_merge(board, word, expected_output):
    solution = Solution()
    output = solution.exist1(board, word)

    assert output == expected_output
    output = solution.exist2(board, word)

    assert output == expected_output
