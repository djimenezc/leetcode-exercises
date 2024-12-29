"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.



Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].


Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
"""
from typing import List

import pytest


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        arrows = 1
        points.sort(key=lambda x: x[0])

        end = points[0][1]

        for x in points[1:]:
            if end < x[0]:
                arrows += 1
                end = x[1]
            else:
                end = min(end, x[1])

        return arrows

    # time complexity is O(NlogN), in which N ~ len(points)
    # Python uses Timsort for its list sort() algorithm, so the space complexity should be O(N).
    def findMinArrowShots2(self, points: list[list[int]]) -> int:

        points.sort(key=lambda x: x[1])  # Example:  points = [[2,4],[1,6],[1,3],[7,8]]
        #      points.sort = [[1,3],[2,4],[1,6],[7,8]]
        tally, bow = 1, points[0][1]
        #                     ––––––– [7,9]
        for start, end in points:  # ––––––––––––––––          [1,6]
            if bow < start:  # –––––––                [2,4]
                bow = end  # –––––––                   [1,3]
                tally += 1  # 1  2  3  4  5  6  7  8  9
                #         |                 |
        return tally  # tally = 1         tally = 2


@pytest.mark.parametrize('points, expected_output', [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
])
def test_merge(points, expected_output):
    solution = Solution()
    output = solution.findMinArrowShots(points)

    assert output == expected_output
    output = solution.findMinArrowShots2(points)

    assert output == expected_output
