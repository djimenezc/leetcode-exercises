"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i],
 you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
from typing import List

import pytest


class Solution:

    # Intuition :
    # At any position ( i ), the maximum range we can reach is ( i + nums[i] ).
    # Using a greedy strategy, we try to jump as far as possible within our current range before
    # incrementing the jump count.
    # Track the maximum range we can reach in the current jump window. When we exhaust this range,
    # it means we must take another jump.
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

    # We have to find the minimum number of jumps required to reach the end of a given array of non-negative
    # integers i.e the shortest number of jumps needed to reach the end of an array of numbers.
    # Time complexity : O(n)
    # Space complexity: O(1)
    # We are using a search algorithm that works by moving forward in steps and counting each step as a jump.
    # The algorithm keeps track of the farthest reachable position at each step and updates the number of
    # jumps needed to reach that farthest position.
    # The algorithm returns the minimum number of jumps needed to reach the end of the array.
    def jump2(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:  # Visited all the items on the current level
                ans += 1  # Increment the level
                end = farthest  # Make the queue size for the next level

        return ans


@pytest.mark.parametrize('nums, expected_output', [
    ([2, 3, 1, 1, 4], 2),
    ([3, 2, 0, 1, 4], 2),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.jump(nums)

    assert output == expected_output
    output = solution.jump2(nums)

    assert output == expected_output
