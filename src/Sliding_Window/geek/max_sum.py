"""

"""
from typing import List

import pytest


class Solution:
    # O(n) solution for finding
    # maximum sum of a subarray of size k
    # Auxiliary Space: O(1)
    def max_sum(self, nums: List[int], k: int):
        # length of the array
        n = len(nums)

        # n must be greater than k
        if n <= k:
            print("Invalid")
            return -1

        # Compute sum of first window of size k
        window_sum = sum(nums[:k])

        # first sum available
        max_sum = window_sum

        # Compute the sums of remaining windows by
        # removing first element of previous
        # window and adding last element of
        # the current window.
        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(window_sum, max_sum)

        return max_sum


@pytest.mark.parametrize('nums, k, expected_output', [
    ([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 24),
])
def test_merge(nums, k, expected_output):
    solution = Solution()
    output = solution.max_sum(nums, k)

    assert output == expected_output
