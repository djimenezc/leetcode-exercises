"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element
of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i],
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.



Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.


Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
import math
from typing import List

import pytest


class Solution:

    # Complexity
    # Time complexity:
    # O(n)
    #
    # Space complexity:
    # O(1)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max_sum = 0
        curr_min_sum = 0
        max_sum = -math.inf
        min_sum = math.inf

        for x in nums:
            total_sum += x
            curr_max_sum = max(curr_max_sum + x, x)
            curr_min_sum = min(curr_min_sum + x, x)
            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)

        return max_sum if max_sum < 0 else max(max_sum, total_sum - min_sum)


@pytest.mark.parametrize('nums, expected_output', [
    ([1, -2, 3, -2], 3),
    ([5, -3, 5], 10),
    ([-3, -2, -3], -2)
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.maxSubarraySumCircular(nums)

    assert output == expected_output
