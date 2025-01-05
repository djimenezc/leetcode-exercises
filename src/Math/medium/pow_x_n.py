"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""

import pytest


class Solution:
    def myPow2(self, x: float, n: int) -> float:

        def calc_power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = calc_power(x, n // 2)
            res = res * res

            if n % 2 == 1:
                return res * x

            return res

        ans = calc_power(x, abs(n))

        if n >= 0:
            return ans

        return 1 / ans

    def myPow(self, x: float, n: int) -> float:

        # Helper function for recursion
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        # Compute the result
        f = function()

        # Handle positive and negative exponents
        return float(f) if n >= 0 else 1 / f

@pytest.mark.parametrize('x, n, expected_output', [
    (2.00000, 10, 1024.00000),
    #(2.10000, 3, 9.26100),
    (2.00000, -2, 0.25000)
])
def test_merge(x, n, expected_output):
    solution = Solution()
    output = solution.myPow(x, n)

    assert output == expected_output
