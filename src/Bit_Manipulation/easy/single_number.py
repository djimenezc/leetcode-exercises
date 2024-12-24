"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

The XOR operation has two useful properties:

( x \oplus x = 0 ): XORing a number with itself results in 0.
( x \oplus 0 = x ): XORing a number with 0 keeps the number unchanged.

By XORing all elements in the array, the elements that appear twice will cancel each other out
(since ( x \oplus x = 0 )), leaving only the single element that appears once.

Approach :
Initialize a variable result to 0.
Iterate through each number in the array:
XOR the number with result.
After the loop, result will contain the single number that doesn’t appear twice.

"""
from typing import List

import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


@pytest.mark.parametrize('nums, expected_output', [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.singleNumber(nums)

    assert output == expected_output
