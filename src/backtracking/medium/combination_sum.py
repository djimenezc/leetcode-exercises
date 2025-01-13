"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
from typing import List

import pytest


class Solution:

    # Steps:
    # Start with an empty combination and a total sum of 0.
    # For each candidate, decide whether to include it in the current combination.
    # If the current total matches the target, store the combination.
    # If the total exceeds the target, backtrack to explore other possibilities.
    #
    # Decision Tree for candidates = [2, 3, 6, 7] and target = 7:
    #
    #                       []
    #                     /   \
    #                  [2]     []
    #                 /   \      \
    #              [2,2]   [2]    [3]
    #             /   \       \     \
    #         [2,2,2]  [2,2,3]  [3,3] [7]
    # Complexity Analysis
    # Time Complexity: O(2 n) in the worst case, as we explore all subsets of candidates.
    # Space Complexity: O(t/d), where t is the target and d is the smallest candidate,
    # representing the depth of the recursion.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates_len = len(candidates)

        def backtrack(idx, comb, total):

            if total == target:
                res.append(comb[:])
                return
            if total > target or idx >= candidates_len:
                return

            comb.append(candidates[idx])
            backtrack(idx, comb, total + candidates[idx])
            comb.pop()
            backtrack(idx + 1, comb, total)

        backtrack(0, [], 0)

        return res


@pytest.mark.parametrize('candidates, target, expected_output', [
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ([2], 1, [])
])
def test_merge(candidates, target, expected_output):
    solution = Solution()
    output = solution.combinationSum(candidates, target)

    assert output == expected_output
