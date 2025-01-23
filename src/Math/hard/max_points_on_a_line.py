"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number
of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
import collections
from collections import defaultdict
from math import inf
from typing import List

import pytest


class Solution:
    # Concept: A set of points are on a line each of their pair-wise slopes has the same value.
    # For each point, we iterate through all the other points and find the slope with each of the other
    # points and store the number of pairs which have the same slope and find the max of the number of points.
    #
    # Time Complexity: O(N^2)
    # Space Complexity: O(N) as we track only N-1 lines in total.
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return inf
            return (y1 - y2) / (x1 - x2)

        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i + 1:]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1

    def maxPoints2(self, points: List[List[int]]) -> int:
        # If we only have 1 point then any line passes through it, so we return 1
        # If we only have 2 point then a line is the shortest path through both, so we return 2
        n = len(points)
        if n < 3:
            return n

        # We make a special helper func for finding the slope so we do not divide by 0
        def find_slope(p1, p2):
            # unpack the points into (x, y) coordinate pairs
            x1, y1 = p1
            x2, y2 = p2
            # Find the denominator or change in x
            delta_x = x1 - x2
            # Vertical lines have infinite slope, but python will give a ZeroDivisionError
            # so we check if the denominator is 0, **before dividing**
            if delta_x == 0:
                return float('inf')
            # Now we can safely divide via `Slope = change in y / change in x`
            return (y1 - y2) / delta_x

        # Start the answer at 1
        # since we return `ans + 1`
        # which will be 2 if we have a skewed lattice (i.e. we actively minimize collinearity)
        ans = 1
        for i, p1 in enumerate(points):
            # For each point, create a new counter map: slope -> count of slope occurrences
            slopes = defaultdict(int)
            # Now for fixed `p1`, consider all future `p2`
            # where we only look at future points to avoid double-counting
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)
                # and add one for the respective count
                slopes[slope] += 1
                # Note that we have to update `ans` inside this loop as `slope` changes every iteration
                ans = max(slopes[slope], ans)
        # Add one to account for the point itself (to have 1 line you need 2 points)
        return ans + 1


@pytest.mark.parametrize('points, expected_output', [
    ([[1, 1], [2, 2], [3, 3]], 3),
    ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4)
])
def test_merge(points, expected_output):
    solution = Solution()
    output = solution.maxPoints(points)

    assert output == expected_output
    output = solution.maxPoints2(points)

    assert output == expected_output
