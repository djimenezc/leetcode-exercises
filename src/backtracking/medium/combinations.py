"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List

import pytest


class Solution:

    # Complexity
    # Time complexity: O(n * k)
    # n is the number of elements and k is the size of the subset. The backtrack function is called n times,
    # because there are n possible starting points for the subset. For each starting point, the backtrack function
    # iterates through all k elements. This is because the comb list must contain all k elements in order for it to be
    # a valid subset.
    #
    # Space complexity: O(k)
    # The comb list stores at most k elements. This is because the backtrack function only adds elements to the comb
    # list when the subset is not yet complete.
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        comb = []

        def backtrack(idx):
            if len(comb) == k:
                # create a copy of the list since lists are mutable in Python
                res.append(comb[:])
                return

            for num in range(idx, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)

        return res


@pytest.mark.parametrize('n, k, expected_output', [
    (3, 1, [[1], [2], [3]]),
    (1, 1, [[1]]),
    (2, 2, [[1, 2]]),
    (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
])
def test_merge(n, k, expected_output):
    solution = Solution()
    output = solution.combine(n, k)

    assert output == expected_output
