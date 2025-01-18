"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide
and conquer approach, which is more subtle.
"""
from typing import List

import pytest


class Solution:
    # O(n) Time and O(1) Space
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_ending = nums[0]

        for i in range(1, len(nums)):
            # Find the maximum sum ending at index i by either extending
            # the maximum sum subarray ending at index i - 1 or by
            # starting a new subarray from index i
            max_ending = max(max_ending + nums[i], nums[i])

            # Update res if maximum subarray sum ending at index i > res
            res = max(res, max_ending)

        return res

    def maxSubArray2(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)

        return res


@pytest.mark.parametrize('nums, expected_output', [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23)
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.maxSubArray(nums)

    assert output == expected_output
    output = solution.maxSubArray2(nums)

    assert output == expected_output
