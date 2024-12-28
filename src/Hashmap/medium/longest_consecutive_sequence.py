"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from collections import defaultdict
from typing import List

import pytest


class Solution:
    # Time complexity O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_len = 0
        tbl = dict()
        for num in nums:
            # get the length for num - 1 sequence formed so far
            l = tbl.get(num - 1, 0)
            # get the length for num + 1 sequence formed so far
            r = tbl.get(num + 1, 0)
            # calculate the current sequnce length possible
            curr_len = r + l + 1
            # set the sequence length for starting index
            # to find starting index just subtract current num - l
            # think: each step was 1 and we just moved l*1 from num to get the start
            tbl[num - l] = curr_len
            # similar for the rightmost
            tbl[num + r] = curr_len
            longest_len = max(curr_len, longest_len)
        return longest_len


@pytest.mark.parametrize('nums, expected_output', [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.longestConsecutive(nums)

    assert output == expected_output
    output = solution.longestConsecutive2(nums)

    assert output == expected_output
