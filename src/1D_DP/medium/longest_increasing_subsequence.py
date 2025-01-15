"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List

import pytest


class Solution:
    # Keep elements in ascending order.
    # res is always sorted in ascending order, so we can use binary search to find right place.
    #
    # Let me explain why we need to replace numbers by binary search.
    # Complexity
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we will return length of res
        res = []

        def binary_search(res, n):
            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n

        return len(res)


@pytest.mark.parametrize('nums, expected_output', [
    ([1, 5, 6, 3, 10, 4], 4),
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.lengthOfLIS(nums)

    assert output == expected_output
