"""
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result
can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?

yes, O(M+N)
"""

from typing import List

import pytest


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        index1 = 0
        index2 = 0

        if m == 0:
            for i in range(0, len(nums2)):
                nums1[i] = nums2[i]
        elif n != 0:
            for i in range(0, n + m):
                if index2 >= n:
                    break
                if (nums1[i] == 0 and index1 >= m) or nums1[i] > nums2[index2]:
                    nums1.insert(i, nums2[index2])
                    index2 = index2 + 1
                    nums1.pop()
                else:
                    index1 = index1 + 1


@pytest.mark.parametrize('nums1,m,nums2,n, expected', [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([3, 3, 4, 5, 0, 0, 0], 4, [1, 1, 1], 3, [1, 1, 1, 3, 3, 4, 5]),
    ([1, 1, 6, 10, 0, 0, 0, 0, 0], 4, [2, 3, 7, 11, 12], 5, [1, 1, 2, 3, 6, 7, 10, 11, 12]),
    ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3])

])
def test_merge(nums1, m, nums2, n, expected):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    assert nums1 == expected