"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
from typing import List

import pytest


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True

    def canJump2(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False  # Cannot proceed further
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) - 1:
                return True  # Reached or surpassed last index
        return False


@pytest.mark.parametrize('nums, expected_output', [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.canJump(nums)

    assert output == expected_output
    output = solution.canJump2(nums)

    assert output == expected_output
