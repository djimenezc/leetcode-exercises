"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
import math
from collections import deque
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, buildTree, isSameTree


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    #Slow
    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr, s, e):
            if s > e:
                return None
            mid = s + (e - s) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr, s, mid - 1)
            node.right = helper(arr, mid + 1, e)
            return node

        n = len(nums)
        if n == 0:
            return None
        return helper(nums, 0, n - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        nums_len = len(nums)
        middle_point = math.floor(len(nums) / 2)
        root = TreeNode(nums[middle_point])

        stack_left = deque()
        stack_right = deque()
        parent_left = root
        parent_right = root

        k = 1

        for i in range(middle_point, 0, -1):
            if parent_left.left and parent_left.right:
                parent_left = stack_left.pop()
            if not parent_left.left:
                parent_left.left = TreeNode(nums[i - 1])
                stack_left.appendleft(parent_left.left)
            elif not parent_left.right:
                parent_left.right = TreeNode(nums[i - 1])
                stack_left.appendleft(parent_left.right)

            if nums_len - k != middle_point:
                if parent_right.left and parent_right.right:
                    parent_right = stack_right.pop()
                if not parent_right.left:
                    parent_right.left = TreeNode(nums[nums_len - k])
                    stack_right.appendleft(parent_right.left)
                elif not parent_right.right:
                    parent_right.right = TreeNode(nums[nums_len - k])
                    stack_right.appendleft(parent_right.right)

            k += 1

        return root

@pytest.mark.parametrize('nums, expected_output', [
    ([-10, -3, 0, 5, 9], buildTree([0, -3, 9, -10, None, 5])),
    ([1, 3], buildTree([3, 1])),
    ([0, 1, 2], buildTree([1, 0, 2])),
    ([0, 1, 2, 3, 4, 5], buildTree([3, 1, 5, 0, 2, 4])),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.sortedArrayToBST(nums)

    assert isSameTree(output, expected_output)
    output = solution.sortedArrayToBST2(nums)

    assert isSameTree(output, expected_output)
