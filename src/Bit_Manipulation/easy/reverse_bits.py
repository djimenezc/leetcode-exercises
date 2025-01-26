"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output
 will be given as a signed integer type. They should not affect your implementation, as the integer's internal
  binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above,
the input represents the signed integer -3 and the output represents the signed integer -1073741825.


Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
so return 3221225471 which its binary representation is 10111111111111111111111111111111.


Constraints:

The input must be a binary string of length 32


Follow up: If this function is called many times, how would you optimize it?

Bit Manipulation:

Extract each bit from the input number ( n ) starting from the least significant bit (LSB) to the most significant
bit (MSB).
Place the extracted bit in the reversed position in the output number.
Use left and right shifts to move bits appropriately.

"""

import pytest


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1  # Extract the least significant bit
            result = (result << 1) | bit  # Append the bit to the result
            n >>= 1  # Right-shift n to process the next bit
        return result

    # Approach
    # Format the given number into a binary format.
    # After formating the length of the string of bites can be less than 32 bits
    # (as zeros before the first 1 don't compute), so the rest of the bits are filled with zeros.
    # Reverse the string of bytes.
    # Turn the string of bytes into an integer in decimal format.
    # Complexity
    # Time complexity:O(n)
    # Space complexity:O(n)
    def reverseBits1(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)

        # reverse the string and convert to int in base 2
        return int(n[::-1], 2)


solution = Solution()


@pytest.mark.parametrize('n, expected_output', [
    (1, 2147483648),
    (43261596, 964176192),
    (4294967293, 3221225471),
])
class TestClass:
    def test_0(self, n, expected_output):
        output = solution.reverseBits(n)

        assert output == expected_output

    def test_1(self, n, expected_output):
        output = solution.reverseBits1(n)

        assert output == expected_output
