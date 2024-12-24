"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1
"""

import pytest


class Solution:
    # Binary Search:
    # Initialize two pointers: left at 0 and right at ( x ).
    # Perform binary search:
    # Calculate the middle point mid.
    # If mid * mid is equal to ( x ), return mid.
    # If mid * mid is less than ( x ), move the left pointer to mid + 1.
    # If mid * mid is greater than ( x ), move the right pointer to mid - 1.
    # The loop ends when left is greater than right. The integer square root of ( x ) will be in the variable right.
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    # If x is 0, return 0.
    # Initialize first to 1 and last to x.
    # While first is less than or equal to last, do the following:
    # a. Compute mid as first + (last - first) / 2.
    # b. If mid * mid equals x, return mid.
    # c. If mid * mid is greater than x, update last to mid - 1.
    # d. If mid * mid is less than x, update first to mid + 1.
    # Return last.
    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last


@pytest.mark.parametrize('x, expected_output', [
    (4, 2),
    (8, 2),
])
def test_merge(x, expected_output):
    solution = Solution()
    output = solution.mySqrt(x)

    assert output == expected_output
    output = solution.mySqrt2(x)

    assert output == expected_output
