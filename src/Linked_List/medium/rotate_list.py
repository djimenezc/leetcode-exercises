"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, is_same_list_node, build_list_node


class Solution:
    def rotateRigthOne(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev_curr = None
        # find latest ListNode
        while curr.next:
            prev_curr = curr
            curr = curr.next

        if prev_curr:
            prev_curr.next = None
            curr.next = head

        return curr

    # Time Limit Exceeded
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        for _ in range(k):
            head = self.rotateRigthOne(head)

        return head

    def findKthNode(self, head, k):
        temp = head
        while k > 1:
            temp = temp.next
            k -= 1
        return temp

    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Calculate length and find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize rotations
        k %= length
        if k == 0:
            return head

        # Step 3: Form a circular linked list
        tail.next = head

        # Step 4: Find the new head and tail
        newTail = self.findKthNode(head, length - k)
        newHead = newTail.next
        newTail.next = None  # Break the circular link

        # Step 5: Return the new head
        return newHead


@pytest.mark.parametrize('head, k, expected_output', [
    (build_list_node([1, 2, 3]), 2000000000, build_list_node([2, 3, 1])),
    ([], 1, []),
    (build_list_node([1]), 1, build_list_node([1])),
    (build_list_node([1, 2, 3, 4, 5]), 1, build_list_node([5, 1, 2, 3, 4])),
    (build_list_node([1, 2, 3, 4, 5]), 2, build_list_node([4, 5, 1, 2, 3])),
    (build_list_node([0, 1, 2]), 4, build_list_node([2, 0, 1])),
])
def test_merge2(head, k, expected_output):
    solution = Solution()
    output = solution.rotateRight2(head, k)

    assert is_same_list_node(output, expected_output)


@pytest.mark.parametrize('head, k, expected_output', [
    ([], 1, []),
    (build_list_node([1, 2, 3]), 2000000000, build_list_node([2, 3, 1])),
    (build_list_node([1]), 1, build_list_node([1])),
    (build_list_node([1, 2, 3, 4, 5]), 1, build_list_node([5, 1, 2, 3, 4])),
    (build_list_node([1, 2, 3, 4, 5]), 2, build_list_node([4, 5, 1, 2, 3])),
    (build_list_node([0, 1, 2]), 4, build_list_node([2, 0, 1])),
])
def test_merge(head, k, expected_output):
    solution = Solution()
    output = solution.rotateRight(head, k)

    assert is_same_list_node(output, expected_output)
