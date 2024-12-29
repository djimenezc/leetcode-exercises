"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, is_same_list_node, build_list_node


class Solution:
    # Time complexity: O(n)
    # Where n is the number of total nodes in the linkedList
    #
    # Space complexity: O(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                running = curr.next
                num = running.val
                while running and running.val == num:
                    running = running.next
                curr.next = running
            else:
                curr = curr.next

        return dummy.next

    def deleteDuplicates2(self, head):
        fake = ListNode(-1)
        fake.next = head
        # We use prev (for node just before duplications begins), curr (for the last node of the duplication group)...
        curr, prev = head, fake
        while curr:
            # while we have curr.next and its value is equal to curr...
            # It means, that we have one more duplicate...
            while curr.next and curr.val == curr.next.val:
                # So move curr pointer to the right...
                curr = curr.next
            # If it happens, that prev.next equal to curr...
            # It means, that we have only 1 element in the group of duplicated elements...
            if prev.next == curr:
                # Don't need to delete it, we move both pointers to right...
                prev = prev.next
                curr = curr.next
            # Otherwise, we need to skip a group of duplicated elements...
            # set prev.next = curr.next, and curr = prev.next...
            else:
                prev.next = curr.next
                curr = prev.next
        # Return the linked list...
        return fake.next


@pytest.mark.parametrize('head, expected_output', [
    (build_list_node([1, 2, 3, 3, 4, 4, 5]), build_list_node([1, 2, 5])),
    (build_list_node([1, 1, 1, 2, 3]), build_list_node([2, 3])),
])
def test_merge(head, expected_output):
    solution = Solution()
    output = solution.deleteDuplicates(head)

    assert is_same_list_node(output, expected_output)


@pytest.mark.parametrize('head, expected_output', [
    (build_list_node([1, 2, 3, 3, 4, 4, 5]), build_list_node([1, 2, 5])),
    (build_list_node([1, 1, 1, 2, 3]), build_list_node([2, 3])),
])
def test_merge2(head, expected_output):
    solution = Solution()
    output = solution.deleteDuplicates2(head)

    assert is_same_list_node(output, expected_output)
