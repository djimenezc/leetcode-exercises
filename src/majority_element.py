'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        map_counter = {}
        k = 0

        for x in nums:
            if map_counter.get(x, None) is None:
                map_counter[x] = 1
            else:
                map_counter[x] = map_counter[x] + 1
            if map_counter[x] >= map_counter.get(k, 0):
                k = x

        return k
