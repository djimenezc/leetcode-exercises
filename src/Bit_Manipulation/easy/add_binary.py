"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


Adding two binary strings is similar to adding decimal numbers but with base 2. We need to consider carrying over 1
when the sum of two digits and a possible carry is greater than or equal to 2. By iterating from the end of both
strings towards the start, we can handle the addition digit by digit.
"""

import pytest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s = str(carry % 2) + s
            carry //= 2

        return s

    # slower
    #  Iterate from the end
    # Time complexity: O(max(a,b))
    # Space complexity: O(max(a,b))
    def addBinary2(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])


solution = Solution()


@pytest.mark.parametrize('a, b, expected_output', [
    ("11", "1", '100'),
    ("1010", "1011", '10101'),
])
class TestCase:
    def test_0(self, a, b, expected_output):
        output = solution.addBinary(a, b)
        assert output == expected_output

    def test_1(self, a, b, expected_output):
        output = solution.addBinary2(a, b)
        assert output == expected_output

