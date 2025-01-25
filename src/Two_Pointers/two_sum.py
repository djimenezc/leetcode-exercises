"""

"""
from typing import List

import pytest


class Solution:

    # Naive Method – O(n^2) Time and O(1) Space
    # The very basic approach is to generate all the possible pairs and check if any of them add up to the target value.
    # To generate all pairs, we simply run two nested loops.
    def two_sum(self, nums: List[int], target):
        n = len(nums)

        # Iterate through each element in the array
        for i in range(n):

            # For each element arr[i], check every
            # other element arr[j] that comes after it
            for j in range(i + 1, n):

                # Check if the sum of the current pair
                # equals the target
                if nums[i] + nums[j] == target:
                    return True

        # If no pair is found after checking
        # all possibilities
        return False

    # Time Complexity: O(n) as the loops runs at most n times. We either increase left,
    # or decrease right or stop the loop.
    # Auxiliary Space: O(1)
    def two_sum2(self, arr: List[int], target):
        # Sort the array
        arr.sort()

        left, right = 0, len(arr) - 1

        # Iterate while left pointer is less than right
        while left < right:
            sum = arr[left] + arr[right]

            # Check if the sum matches the target
            if sum == target:
                return True
            elif sum < target:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left

        # If no pair is found
        return False


@pytest.mark.parametrize('s, t, expected_output', [
    ([0, -1, 2, -3, 1], -2, True),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.two_sum(s, t)

    assert output == expected_output
    output = solution.two_sum2(s, t)

    assert output == expected_output
