'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''
from typing import List

import pytest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        list_len = len(nums)
        k = 0 if list_len == 0 else 1

        while k < list_len:
            if nums[k - 1] == nums[k]:
                nums.pop(k - 1)
                nums.append('_')
            elif nums[k] == '_':
                break
            else:
                k = k + 1

        return k


@pytest.mark.parametrize('nums, k, nums_expect', [
    ([], 0, []),
    ([1, 1, 2], 2, [1, 2, '_']),
    ([0, 0, 1, 1, 1], 2, [0, 1, '_', '_', '_']),
    ([0, 0, 1, 1, 1, 2], 3, [0, 1, 2, '_', '_', '_']),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']),

])
def test_merge(nums, k, nums_expect):
    solution = Solution()
    output = solution.removeDuplicates(nums)

    assert k == output
    for i in range(0, k):
        assert nums[i] == nums_expect[i];