"""
Given a positive integer n, write a function that returns the number of
set bits
 in its binary representation (also known as the Hamming weight).



Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.



Constraints:

1 <= n <= 231 - 1


Follow up: If this function is called many times, how would you optimize it?
"""

import pytest


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation = bin(n)[2:]
        output = 0

        for x in binary_representation:
            if x == '1':
                output += 1

        return output

    def hammingWeight2(self, n: int) -> int:

        output = 0

        for _ in range(32):
            bit = n & 1  # Extract the least significant bit
            if bit == 1:
                output += 1
            n >>= 1  # Right-shift n to process the next bit

        return output


@pytest.mark.parametrize('n, expected_output', [
    (11, 3),
    (128, 1),
    (2147483645, 30),
])
def test_merge(n, expected_output):
    solution = Solution()
    output = solution.hammingWeight(n)

    assert output == expected_output
    output = solution.hammingWeight2(n)

    assert output == expected_output
