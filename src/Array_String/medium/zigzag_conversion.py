"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

import pytest

class Solution:
    # Approach
    # Edge Case Handling:
    #
    # If numRows is 1, the zigzag pattern is essentially a straight line, so we can return the input string s as is.
    # Initialize Rows:
    #
    # Create a list rows with numRows empty strings to collect characters for each row.
    # Simulate Zigzag Traversal:
    #
    # Use two variables, add to keep track of the current row and inc to control the direction of traversal.
    # Iterate through the input string s, appending each character to the appropriate row.
    # Adjust the inc variable to change direction when reaching the top or bottom of the zigzag pattern.
    # Join Rows:
    #
    # After populating all rows, concatenate the rows to form the final zigzag string.
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [''] * numRows
        row, inc = 0, 1

        for i in range(len(s)):
            matrix[row] += s[i]
            if row == 0:
                inc = 1
            elif row == numRows - 1:
                inc = -1

            row += inc

        return "".join(matrix)


@pytest.mark.parametrize('s, numRows, expected_output', [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
    ("BAA", 3, "BAA")
])
def test_merge(s, numRows, expected_output):
    solution = Solution()
    output = solution.convert(s, numRows)

    assert output == expected_output
