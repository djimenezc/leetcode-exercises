"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List

import pytest


class Solution:
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        min_len = 0
        n = len(nums)

        for i in range(len(nums)):
            j = i + 1
            accumulator = nums[i]
            counter = 1
            while j < n:
                if accumulator >= target:
                    min_len = counter if min_len == 0 else min(min_len, counter)
                    if min_len == 1:
                        return 1
                accumulator += nums[j]
                counter += 1
                j += 1
                if accumulator == target:
                    min_len = counter if min_len == 0 else min(min_len, counter)

        return min_len

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0


@pytest.mark.parametrize('target, nums, expected_output', [
    (11, [1, 2, 3, 4, 5], 3),
    # (2, [2, 2, 3], 1),
    # (7, [2, 3, 1, 2, 4, 3], 2),
    # (4, [1, 4, 4], 1),
    # (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
])
def test_merge(target, nums, expected_output):
    solution = Solution()
    output = solution.minSubArrayLen(target, nums)

    assert output == expected_output
