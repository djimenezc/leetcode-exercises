"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0


Constraints:

0 <= left <= right <= 231 - 1
"""

import pytest


class Solution:
    # Common Prefix Identification:
    #
    # The function iteratively right-shifts both left and right until they become equal, identifying the common prefix
    # of their binary representations.
    # Counting Shifts:
    #
    # It counts the number of right-shifts performed, storing the count in the variable cnt.
    # Bitwise AND Calculation:
    #
    # After finding the common prefix, it reconstructs the bitwise AND result by left-shifting the common prefix by
    # cnt bits.
    # Time complexity:
    # O(1)
    #
    # Space complexity:
    # O(1)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

@pytest.mark.parametrize('left, right, expected_output', [
    (5, 7, 4),
    (0,0,0),
    (1, 2147483647, 0)
])
def test_merge(left, right, expected_output):
    solution = Solution()
    output = solution.rangeBitwiseAnd(left, right)

    assert output == expected_output
