"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List

import pytest


class Solution:

    # The loop continues as long as there are elements in the range [low, high].
    # It uses binary search to quickly narrow down the position of target.
    # If the loop exits without finding target, low will be the index where
    # target can be inserted to maintain the sorted order.
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            print(mid, low, high)
        return low


@pytest.mark.parametrize('nums, target, expected_output', [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
])
def test_merge(nums, target, expected_output):
    solution = Solution()
    output = solution.searchInsert(nums, target)

    assert output == expected_output
