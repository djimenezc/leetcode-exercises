"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""
import math
import re
from collections import Counter
from typing import List

import pytest


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []
        interval_end = None
        interval_start = None

        for i in range(len(nums)):
            if interval_start is None:
                interval_start = nums[i]
            if i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                interval_end = nums[i] + 1
            else:
                if interval_end is None:
                    result.append(f'{interval_start}')
                else:
                    result.append(f'{interval_start}->{interval_end}')
                interval_end = None
                interval_start = None

        return result


@pytest.mark.parametrize('nums, expected_output', [
    ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
    ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),

])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.summaryRanges(nums)

    assert output == expected_output
