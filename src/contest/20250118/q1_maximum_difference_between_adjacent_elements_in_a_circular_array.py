"""
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

 

Example 1:

Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

 

Constraints:

2 <= nums.length <= 100
-100 <= nums[i] <= 100©leetcode
"""
import math
from typing import List

import pytest


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        curr_val = nums[0]
        max_diff = abs(curr_val - nums[-1])

        if len(nums) < 2:
            return 0

        for i in range(1, len(nums)):
            max_diff = max(abs(curr_val - nums[i]), max_diff)
            curr_val = nums[i]

        return max_diff


@pytest.mark.parametrize('nums, expected_output', [
    ([3], 0),
    ([1, 2, 4], 3),
    ([-5, -10, -5], 5)
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.maxAdjacentDistance(nums)

    assert output == expected_output
