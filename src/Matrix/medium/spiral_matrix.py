"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

import pytest


class Solution:
    # Time complexity: O(n∗m)
    # Space complexity: O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(m * n):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y + dy][x + dx] == ".":
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res

    # Spiral Traversal Order:
    #
    # Start from the top row, move left to right.
    # Then move down along the right column.
    # Next, move right to left along the bottom row.
    # Finally, move up along the left column.
    # Repeat these steps while narrowing the boundaries of the matrix (top, bottom, left, and right).
    #
    # Stop when all elements of the matrix are visited.
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row (if valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse left column (if valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


@pytest.mark.parametrize('matrix, expected_output', [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
])
def test_merge(matrix, expected_output):
    solution = Solution()
    output = solution.spiralOrder2(matrix)

    assert output == expected_output
    output = solution.spiralOrder(matrix)

    assert output == expected_output

