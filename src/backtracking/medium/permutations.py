"""
Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List

import pytest


class Solution:
    # Using backtracking to create all possible combinations
    # Complexity
    # Time complexity: O(n * n!)
    #
    # Recursive Calls: The permute function is called recursively, and each time it generates permutations for
    # a smaller list by removing one element. In the worst case, the recursion depth is equal to the length of the
    # input list nums, which is n.
    #
    # Permutation Generation: For each index, we are generating permutations for the remaining elements and appending
    # the removed element at the end. This involves recursive calls and list manipulations. In general time complexity
    # of permutation should be O(n!)
    #
    # Space complexity: O(n)
    #
    # Recursion Depth: The depth of recursion goes up to the number of elements in the input list. So, the maximum
    # recursion depth is O(n).
    #
    # Additional Memory: The additional memory usage includes the res list, the n variable, and the space used in
    # each recursive call.
    #
    # Considering these factors, the space complexity is O(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)

            res.extend(perms)
            nums.append(n)

        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res


@pytest.mark.parametrize('nums, expected_output', [
    ([0, 1], [[0, 1], [1, 0]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([1], [[1]])
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.permute(nums)

    output.sort()

    assert output == expected_output
    output = solution.permute2(nums)

    output.sort()

    assert output == expected_output
