"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List

import pytest


class Solution:
    # Steps Explanation:
    # Reverse the entire array:
    # Example: ( [1,2,3,4,5,6,7] ) → ( [7,6,5,4,3,2,1] )
    # Reverse the first ( k ) elements:
    # Example: ( [7,6,5,4,3,2,1] ) → ( [5,6,7,4,3,2,1] )
    # Reverse the last ( n-k ) elements:
    # Example: ( [5,6,7,4,3,2,1] ) → ( [5,6,7,1,2,3,4] )
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


@pytest.mark.parametrize('nums, k, expected_output', [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
])
def test_merge(nums, k, expected_output):
    solution = Solution()
    solution.rotate(nums, k)

    assert nums == expected_output
