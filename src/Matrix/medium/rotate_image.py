"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Matrix rotation is a common problem in computer science and competitive programming.

"""
from typing import List

import pytest


class Solution:
    """
    Intuition
To achieve a 90-degree rotation, two key transformations are needed:

Vertical Reversal (Flip along the horizontal axis)
Transpose (Swap rows and columns)
Combining these steps effectively rotates the matrix. Let’s break it down:

1. Vertical Reversal
In this step, we flip the matrix upside down. For every column, the topmost element swaps with the bottommost element, the second topmost swaps with the second bottommost, and so on.

Visualization: Vertical Reversal
Input Matrix:

1  2  3
4  5  6
7  8  9
After Vertical Reversal:

7  8  9
4  5  6
1  2  3
This aligns the rows correctly for the next transformation.

2. Transpose
Transposing a matrix swaps the rows and columns. In simpler terms, we swap matrix[i][j] with matrix[j][i] for every valid pair of indices above the diagonal.

Visualization: Transpose
Matrix after Vertical Reversal:

7  8  9
4  5  6
1  2  3
After Transposing:

7  4  1
8  5  2
9  6  3
This final transformation achieves the desired clockwise rotation.
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            for col in range(edge_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        "we swap matrix[i][j] with matrix[j][i] for every valid pair of indices above the diagonal."
        for row in range(edge_length):
            for col in range(row+1, edge_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        return matrix


@pytest.mark.parametrize('matrix, expected_output', [
    ([[1, 2], [4, 5]], [[4,1],[5,2]]),
    ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
])
def test_merge(matrix, expected_output):
    solution = Solution()
    solution.rotate(matrix)

    assert matrix == expected_output
