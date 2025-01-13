"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List

import pytest


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for i in range(0, len(nums)):
            end = 0 if i + 1 == len(nums) else i + 1
            if nums[i] > nums[i - 1] and nums[i] > nums[end]:
                return i

        return 0

    # Complexity
    # Time complexity: O(logn)
    # Space complexity: O(1)
    # We have to solve this question with O(logn) time. Let's solve this question with binary search.
    def findPeakElement2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


@pytest.mark.parametrize('nums, expected_output', [
    ([1, 2, 3], 2),
    ([1, 2], 1),
    ([3, 2, 1], 0),
    ([2, 1], 0),
    ([1], 0),
    ([1, 2, 3, 1], 2),
    ([1, 2, 1, 3, 5, 6, 4], 1)
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.findPeakElement(nums)

    assert output == expected_output
    output = solution.findPeakElement2(nums)

    assert output == expected_output
