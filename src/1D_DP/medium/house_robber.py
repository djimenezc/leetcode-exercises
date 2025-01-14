"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
  and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money
you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

The House Robber problem is a classic dynamic programming problem where you must calculate the maximum amount
of money a thief can steal without alerting security systems by robbing two adjacent houses.
 Below are explanations for two approaches to solve this problem, both leveraging Dynamic Programming (DP)
  but with different implementations.
"""
from typing import List

import pytest


class Solution:
    # Dynamic Programming with an Array
    # Key Observations
    # If a thief robs house i, they cannot rob house i-1 due to the constraints.
    # If the thief skips house i, their maximum profit up to house i is the same as the profit for house i-1.
    # Complexity
    # Time Complexity: O(n) — A single loop processes all houses.
    # Space Complexity: O(n) — The dp array stores results for all houses.
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

    # In Solution 1, we used an array dp to store results for all houses. However,
    # only the last two values in the dp array are needed at any time. This insight allows us to
    # reduce space complexity by using two variables to track these values.
    # Complexity
    # Time Complexity: O(n) — A single loop processes all houses.
    # Space Complexity: O(1) — Only two variables are used.
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prev_prev = nums[0]
        prev = max(prev_prev, nums[1])

        for i in range(2, n):
            temp = max(prev, nums[i] + prev_prev)
            prev_prev = prev
            prev = temp

        return prev


@pytest.mark.parametrize('nums, expected_output', [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.rob(nums)

    assert output == expected_output
    output = solution.rob2(nums)

    assert output == expected_output
