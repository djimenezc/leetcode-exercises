"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List

import pytest


class Solution:
    # Keep max height on the both side.
    # max height of left and right
    # [2,1,0,1,3,2]
    #  L         R
    #
    # left max = 2
    # right max = 2
    # water = 0
    #
    # L is current left pointer.
    # R is current right pointer.
    # left max is max height of left side we found so far. Initialized with the first number.
    # right max is max height of right side we found so far. Initialized with the last number
    # water is return value.
    # We take smaller max height between left(= 2 height) and right(= 3 height)
    # and handle left side because left max is smaller than right max
    # Complexity
    # Time complexity: O(n)
    # Space complexity: O(1)
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        # store the maximum height encountered from the left and right sides respectively.
        left_max = height[left]
        right_max = height[right]
        # keep track of the total trapped water.
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                # Calculate the water trapped at the current position based on the difference
                # between the maximum height and the current height.
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                # Calculate the water trapped at the current position based on the difference
                # between the maximum height and the current height.
                water += right_max - height[right]

        return water


@pytest.mark.parametrize('height, expected_output', [
    ([1, 0, 2], 1),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
])
def test_merge(height, expected_output):
    solution = Solution()
    output = solution.trap(height)

    assert output == expected_output
