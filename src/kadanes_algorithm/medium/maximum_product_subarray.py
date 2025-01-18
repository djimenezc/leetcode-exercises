"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List

import pytest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = prev_max = prev_min = nums[0]

        for i in range(1, len(nums)):
            curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
            curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            prev_min, prev_max = curr_min, curr_max
            max_prod = max(curr_max, max_prod)

        return max_prod


@pytest.mark.parametrize('nums, expected_output', [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.maxProduct(nums)

    assert output == expected_output
