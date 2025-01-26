"""
Finding the maximum element in the array:
We can use Divide and Conquer Algorithm to find the maximum element in the array by dividing the array into two equal
sized subarrays, finding the maximum of those two individual halves by again dividing them into two smaller halves.
This is done till we reach subarrays of size 1. After reaching the elements, we return the maximum element and combine
the subarrays by returning the maximum in each subarray.
"""

import pytest


class Solution:
    def find_max(self, a, lo, hi):
        # If lo becomes greater than hi, then return minimum
        # integer possible
        if lo > hi:
            return float('-inf')
        # If the subarray has only one element, return the element
        if lo == hi:
            return a[lo]
        mid = (lo + hi) // 2
        # Get the maximum element from the left half
        left_max = self.find_max(a, lo, mid)
        # Get the maximum element from the right half
        right_max = self.find_max(a, mid + 1, hi)
        # Return the maximum element from the left and right half

        return max(left_max, right_max)


@pytest.mark.parametrize('nums, expected_output', [
    ([1, 5, 2, 30, 10], 30),
    ([1, 5, 2, 31, 30, 10], 31),
    ([1, 5, 2, 30, 10, 40], 40),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.find_max(nums, 0, len(nums)-1)

    assert output == expected_output
