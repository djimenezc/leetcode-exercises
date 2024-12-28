"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List

import pytest


class Solution:


    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged_intervals = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged_intervals.append(prev)
                prev = interval

        merged_intervals.append(prev)

        return merged_intervals


@pytest.mark.parametrize('intervals, expected_output', [
    ([[1, 4], [5, 6]], [[1, 4], [5, 6]]),
    ([[1, 3]], [[1, 3]]),
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]])
])
def test_merge(intervals, expected_output):
    solution = Solution()
    output = solution.merge(intervals)

    assert output == expected_output
