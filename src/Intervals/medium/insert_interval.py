"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an
interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
from typing import List

import pytest


class Solution:

    # Time complexity: O(nlogn)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res

    # Time complexity: O(n)
    # Space complexity: O(n)
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []

        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        res.extend(intervals[i:])

        return res

    # Space complexity: O(sort)
    # def insert3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #
    #     merged_intervals = []
    #     prev = intervals[0]
    #
    #     for interval in intervals[:]:
    #         if newInterval[1] >= interval[0]:
    #             interval[1] = max(interval[1], newInterval[1])
    #
    #         merged_intervals.append(interval)
    #
    #     return merged_intervals


@pytest.mark.parametrize('intervals, newInterval, expected_output', [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
])
def test_merge(intervals, newInterval, expected_output):
    solution = Solution()
    output = solution.insert2(intervals, newInterval)

    assert output == expected_output
    output = solution.insert(intervals, newInterval)

    assert output == expected_output
