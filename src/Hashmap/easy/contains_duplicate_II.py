"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
import math
import re
from collections import Counter
from typing import List

import pytest


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:

        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited and abs(i - visited[nums[i]]) <= k:
                return True
            visited[nums[i]] = i

        return False


@pytest.mark.parametrize('nums, k, expected_output', [
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False),
])
def test_merge(nums, k, expected_output):
    solution = Solution()
    output = solution.containsNearbyDuplicate(nums, k)

    assert output == expected_output
    output = solution.containsNearbyDuplicate2(nums, k)

    assert output == expected_output
