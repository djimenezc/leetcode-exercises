"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from collections import Counter
from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            for k in range(0, len(nums)):
                if i != k and nums[i] + nums[k] == target:
                    return [i, k]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            for k in range(i, len(nums)):
                if i != k and nums[i] + nums[k] == target:
                    return [i, k]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:

        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found


@pytest.mark.parametrize('nums, target, expected_output', [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_merge(nums, target, expected_output):
    solution = Solution()
    # output = solution.twoSum(nums, target)
    #
    # assert output == expected_output
    #
    # output = solution.twoSum2(nums, target)
    #
    # assert output == expected_output

    output = solution.twoSum3(nums, target)

    assert output == expected_output

    output = solution.twoSum4(nums, target)

    assert output == expected_output

