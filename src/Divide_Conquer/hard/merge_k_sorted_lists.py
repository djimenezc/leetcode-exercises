"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from typing import List, Optional

import pytest

from src.Linked_List.Utils import ListNode, build_list_node, is_same_list_node


class Solution:
    # Intuition: Use the same logic of "Merge two sorted lists".
    # The code repeatedly merges pairs of linked lists until only one sorted linked list remains.
    # It uses a helper function to merge two sorted linked lists.
    # The process continues in a divide-and-conquer manner, reducing the problem size at each step.
    # Time complexity: O(nlogk)
    # Space complexity: O(n)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp

        return lists[0]

    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node

        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return ans.next


@pytest.mark.parametrize('lists, expected_output', [
    ([build_list_node([1, 4, 5]), build_list_node([1, 3, 4]), build_list_node([2, 6])],
        build_list_node([1, 1, 2, 3, 4, 4, 5, 6])),
    ([build_list_node(None)], build_list_node(None)),
    ([build_list_node([])], build_list_node([])),
])
def test_merge(lists, expected_output):
    solution = Solution()
    output = solution.mergeKLists(lists)

    assert is_same_list_node(output, expected_output)
