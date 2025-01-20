"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not
a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, build_list_node, is_same_list_node, print_node, print_list_node


class Solution:
    # Reverse a segment of ( k ) nodes at a time:
    # This can be done iteratively by adjusting the next pointers within each group.
    # Handle edge cases:
    # If there are fewer than ( k ) nodes remaining, skip reversing for that segment.
    # Ensure the list is correctly reconnected after each segment is reversed
    #
    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 1:
            return head

        for i in range(k -1):
            print(f'i: {i} - {head.val}')
            new_head = head.next
            prev_head = head
            prev_head.next = new_head.next
            new_head.next = prev_head
            head = new_head

        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        # Count the number of nodes in the list
        count = 0
        while curr:
            count += 1
            curr = curr.next

        # Reverse k nodes at a time
        while count >= k:
            curr = prev.next
            nxt = curr.next

            # Reverse k nodes
            for _ in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next

            prev = curr
            count -= k

        return dummy.next


@pytest.mark.parametrize('head, k, expected_output', [
    (build_list_node([1, 2, 3]), 1,
     build_list_node([1, 2, 3])),
    (build_list_node([1, 2, 3]), 2,
     build_list_node([2, 1, 3])),
    (build_list_node([1, 2, 3, 4, 5]), 2,
     build_list_node([2, 1, 4, 3, 5])),
    (build_list_node([1, 2, 3, 4, 5]), 3,
     build_list_node([3, 2, 1, 4, 5])),
])
def test_merge(head, k, expected_output):
    solution = Solution()
    output = solution.reverseKGroup(head, k)

    print_list_node(output)

    assert is_same_list_node(output, expected_output)
