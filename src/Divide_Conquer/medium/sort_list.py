"""
Given the head of a linked list, return the list after sorting it in ascending order.



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


Why O(n log n)? know this ?
A linked list cannot use random access (as arrays can), so efficient algorithms like merge sort or bottom-up merge
sort are ideal for this problem.




"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, build_list_node, is_same_list_node


class Solution:

    """
    Algorithm Steps :
        Divide:

        Use a slow and fast pointer approach to find the middle of the linked list.
        Split the list into two halves.
        Conquer:

        Recursively sort both halves.
        Combine:

        Use a merge function to combine the sorted halves into one sorted list.
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next

@pytest.mark.parametrize('head, expected_output', [
    (build_list_node([4, 2, 1, 3]), build_list_node([1, 2, 3, 4])),
    (build_list_node([-1, 5, 3, 4, 0]), build_list_node([-1, 0, 3, 4, 5])),
    ([], [])
])
def test_merge(head, expected_output):
    solution = Solution()
    output = solution.sortList(head)

    assert is_same_list_node(output, expected_output)
