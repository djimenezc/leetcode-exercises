"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, build_list_node, is_same_list_node


class Solution:

    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # If the linked list is empty (not head) or left is equal to right,
        # return the original head as there is no reversal needed.
        if not head or left == right:
            return head

        # This dummy node helps in handling the case when left is 1.
        dummy = ListNode(0, head)
        prev = dummy

        # Traverse the list to find the (left-1)-th node.
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the portion of the linked list from the left-th node to the right-th node.
        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        # Return the new head of the modified linked list.
        return dummy.next


@pytest.mark.parametrize('head, left, right, expected_output', [
    (build_list_node([1, 2, 3, 4, 5]), 2, 4, build_list_node([1, 4, 3, 2, 5])),
    (build_list_node([5]), 1, 1, build_list_node([5])),
])
def test_merge(head, left, right, expected_output):
    solution = Solution()
    output = solution.reverseBetween(head, left, right)

    assert is_same_list_node(output, expected_output)
