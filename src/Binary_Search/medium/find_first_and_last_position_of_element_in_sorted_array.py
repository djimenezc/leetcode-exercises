"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List

import pytest


class Solution:
    # Using Binary Search twice for left most value and right most value
    # We have a constraint of time complexity O(logn) and a description says "Given an array of integers nums sorted
    # in non-decreasing order", so we can feel this question is solved by binary search.
    #
    # But a challenging point of this question is that we might multiple targets in the input array, because we have to
    # find the starting and ending position of a given target value.
    # We might have multiple targets in the input array.
    # I think it's hard to find the most left index and right index at the same time, so simply we execute binary
    # search twice for the most left index and right index, so that we can focus on one of them.
    # Complexity
    # Time complexity: O(logn)
    # The time complexity of the binary search algorithm is O(logn) where n is the length of the input array nums.
    # The searchRange method calls binary_search twice, so the overall time complexity remains O(logn).
    #
    # Space complexity: O(1)
    # The space complexity is O(1) because the algorithm uses a constant amount of extra space, regardless
    # of the size of the input array. There are no data structures or recursive calls that consume additional space
    # proportional to the input size.
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1

            return idx

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)

        return [left, right]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    break

            return idx

        right = binary_search(nums, target)
        left = right

        list_len = len(nums)
        if right != -1:
            while (right < list_len - 1 and nums[right + 1] == target) \
                    or (left > 0 and nums[left - 1] == target):
                if right < list_len - 1 and nums[right + 1] == target:
                    right += 1
                if left > 0 and nums[left - 1] == target:
                    left -= 1

        return [left, right]


@pytest.mark.parametrize('nums, target, expected_output', [
    ([1], 1, [0, 0]),
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1])
])
def test_merge(nums, target, expected_output):
    solution = Solution()
    output = solution.searchRange(nums, target)

    assert output == expected_output
    output = solution.searchRange2(nums, target)

    assert output == expected_output
