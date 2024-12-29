"""

"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, buildList, isSameListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        result = None
        head = None

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_vals = val1 + val2 + carry
            if int(sum_vals / 10) == 1:
                carry = 1
                sum_vals = sum_vals % 10
            else:
                carry = 0

            if head:
                result.next = ListNode(sum_vals)
                result = result.next
            else:
                result = ListNode(sum_vals)
                head = result
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            result.next = ListNode(1)

        return head

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next


@pytest.mark.parametrize('l1, l2, expected_output', [
    (buildList([2, 4, 3]), buildList([5, 6, 4]), buildList([7, 0, 8])),
    (buildList([0]), buildList([0]), buildList([0])),
    (buildList([9, 9, 9, 9, 9, 9, 9]), buildList([9, 9, 9, 9]), buildList([8, 9, 9, 9, 0, 0, 0, 1])),
])
def test_merge(l1, l2, expected_output):
    solution = Solution()
    output = solution.addTwoNumbers(l1, l2)

    assert isSameListNode(output, expected_output)
    output = solution.addTwoNumbers2(l1, l2)

    assert isSameListNode(output, expected_output)
