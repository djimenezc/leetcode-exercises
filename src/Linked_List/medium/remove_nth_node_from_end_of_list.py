"""

"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, build_list_node, is_same_list_node


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        counter = 0
        curr = head
        prev_delay_n = None

        while curr:
            if prev_delay_n:
                prev_delay_n = prev_delay_n.next

            if counter == n:
                prev_delay_n = head
            curr = curr.next

            counter += 1

        if prev_delay_n:
            prev_delay_n.next = prev_delay_n.next.next
        else:
            return head.next

        return head

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next


@pytest.mark.parametrize('head, n, expected_output', [
    (build_list_node([1, 2, 3, 4, 5]), 2, build_list_node([1, 2, 3, 5])),
    (build_list_node([1, 2]), 2, build_list_node([2])),
    (build_list_node([1]), 1, []),
    (build_list_node([1, 2]), 1, build_list_node([1])),
])
def test_merge(head, n, expected_output):
    solution = Solution()
    output = solution.removeNthFromEnd(head, n)

    assert is_same_list_node(output, expected_output)


@pytest.mark.parametrize('head, n, expected_output', [
    (build_list_node([1, 2, 3, 4, 5]), 2, build_list_node([1, 2, 3, 5])),
    (build_list_node([1, 2]), 2, build_list_node([2])),
    (build_list_node([1]), 1, []),
    (build_list_node([1, 2]), 1, build_list_node([1])),
])
def test_merge2(head, n, expected_output):
    solution = Solution()
    output = solution.removeNthFromEnd2(head, n)

    assert is_same_list_node(output, expected_output)
    # output = solution.removeNthFromEnd2(head, n)
    #
    # assert is_same_list_node(output, expected_output)
