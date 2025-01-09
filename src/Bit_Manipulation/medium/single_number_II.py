"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""
from collections import defaultdict
from typing import List

import pytest


class Solution:
    #brute force
    def singleNumber1(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for x in nums:
            count[x] += 1

        for x, freq in count.items():
            if freq == 1:
                return x

        return -1

    # Bit Manipulation
    # The logical thinking behind this approach is to count the number of 1s at each bit position for all the numbers.
    # Since each number appears three times except for the single number, the sum of 1s at each bit position should be
    # divisible by 3 for a balanced line. Any number of 1s that is not divisible by 3 indicates an unbalanced line,
    # which means the single number contributes to that particular bit position.
    #
    # By masking the positions of the unbalanced lines with 1s in ans, we effectively isolate the bits that are part of
    # the single number. Finally, the resulting value in ans represents the binary representation of the single number.
    def singleNumber2(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Convert the number to two's complement representation to handle large test case
                if num < 0:
                    num = num & (2 ** 32 - 1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            ans |= bit_sum << i

        # Convert the result back to two's complement representation if it's negative to handle large test case
        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans

    # Core Idea :
    # Instead of counting occurrences of numbers, we count occurrences of bits.
    #
    # For each bit position (0 to 31), count how many times the bit is set (1) across all numbers in the array.
    # If the count of a bit is not a multiple of 3, then the single number must have that bit set.
    # Key Bitwise Operations :
    # &: Bitwise AND
    # ~: Bitwise NOT
    # |: Bitwise OR
    # ^: Bitwise XOR  is true if and only if the inputs differ (one is true, one is false)
    def singleNumber3(self, nums: List[int]) -> int:
        ones, twos = 0, 0

        for num in nums:
            # Update ones and twos
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones  # The single number remains in "ones"

@pytest.mark.parametrize('nums, expected_output', [
    ([2,2,3,2], 3),
    ([0,1,0,1,0,1,99], 99)
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.singleNumber1(nums)

    assert output == expected_output

    output = solution.singleNumber2(nums)

    assert output == expected_output

    output = solution.singleNumber3(nums)

    assert output == expected_output
