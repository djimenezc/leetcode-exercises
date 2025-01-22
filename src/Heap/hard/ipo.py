"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources,
it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total
capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i]
is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be
added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the
final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6


Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109

"""
import heapq
from typing import List

import pytest


class Solution:
    # Intuition
    # The intuition behind this code is to maximize the available capital after selecting up to k projects,
    # by strategically choosing the projects with the highest profit that can be started within the current
    # capital constraints. It does this by sorting projects by their capital requirements to quickly find the most
    # affordable ones, then using a max-heap to efficiently select the highest-profit projects that are currently
    # affordable, updating the available capital with each project's profit. This greedy approach ensures that
    # at each step, the most beneficial project within financial reach is selected to optimize the total capital.
    #
    # Approach
    # Sort Projects by Capital: Begin by sorting the projects based on the capital required to ensure
    # you look at the cheapest projects first.
    #
    # Use Max-Heap for Profits: Employ a max-heap (inverted to a min-heap using negative values)
    # to always have quick access to the project with the highest available profit.
    #
    # Process Projects Within Capital: As long as there are projects you can afford, add their profits
    # (negatively) to the heap.
    #
    # Select Top Profit Projects: For up to k iterations, choose the most profitable project you can afford by popping
    # from the heap, increasing your capital.
    #
    # Resulting Capital: After potentially choosing k projects, the resulting capital is the maximum capital achieved.
    # Complexity
    # Time complexity:
    # O(NLogN+KLogN)
    #
    # Space complexity:
    # O(N)
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        maxHeap = []
        i = 0
        for _ in range(k):
            # if you have enough remaining capital, invest
            while i < n and projects[i][0] <= w:
                # include the profit in your capital gains
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)

        return w


@pytest.mark.parametrize('k, w, profits, capital, expected_output', [
    (2, 0, [1, 2, 3], [0, 1, 1], 4),
    (3, 0, [1, 2, 3], [0, 1, 2], 6)
])
def test_merge(k, w, profits, capital, expected_output):
    solution = Solution()
    output = solution.findMaximizedCapital(k, w, profits, capital)

    assert output == expected_output
