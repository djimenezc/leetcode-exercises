"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
import math
import re
from collections import Counter
from typing import List, Optional

import pytest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildList(nums: List):
    head = ListNode(nums[0])
    current_node = head
    for i in range(1, len(nums)):
        current_node.next = ListNode(nums[i])
        current_node = current_node.next

    return head


def print_node_list(node_list: ListNode):
    values = []
    while node_list:
        values.append(node_list.val)
        node_list = node_list.next

    print('f', str(values))

    return str(values)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        tail = None

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        while list1 is not None and list2 is not None:
            if list1.val == list2.val:
                if tail is None:
                    tail = ListNode(list1.val)
                else:
                    tail.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val > list2.val:
                if tail is None:
                    tail = ListNode(list2.val)
                else:
                    tail.next = ListNode(list2.val)
                list2 = list2.next
            else:
                if tail is None:
                    tail = ListNode(list1.val)
                else:
                    tail.next = ListNode(list1.val)
                list1 = list1.next
            if head is None:
                head = tail
            else:
                tail = tail.next
            print_node_list(head)

        tail.next = list1 if list2 is None else list2
        print_node_list(head)

        return head

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        pointer1 = list1
        pointer1_prev = None
        pointer2 = list2

        def insert_node_after(node, val):
            temp_node = node.next
            node.next = ListNode(val)
            node.next.next = temp_node

            return node

        while pointer2:
            if pointer1.val == pointer2.val:
                insert_node_after(pointer1, pointer2.val)
                pointer2 = pointer2.next
                pointer1_prev = pointer1
                pointer1 = pointer1.next
            elif pointer1.val < pointer2.val:
                if pointer1.next and pointer1.next.val < pointer2.val:
                    pointer1_prev = pointer1
                    pointer1 = pointer1.next
                else:
                    insert_node_after(pointer1, pointer2.val)
                    pointer2 = pointer2.next
                    pointer1_prev = pointer1
                    pointer1 = pointer1.next
            else:
                if pointer1_prev is None:
                    head = ListNode(pointer2.val)
                    head.next = pointer1
                    pointer1_prev = head
                    pointer2 = pointer2.next
                    list1 = head
                else:
                    if pointer1_prev.val <= pointer2.val:
                        insert_node_after(pointer1_prev, pointer2.val)
                        pointer1 = pointer1_prev.next
                    else:
                        insert_node_after(pointer1, pointer2.val)

                    pointer2 = pointer2.next
            print_node_list(list1)

        return list1

    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2
        print_node_list(dummy.next)

        return dummy.next  # Return the head of the merged list


@pytest.mark.parametrize('list1, list2, expected_output', [
    (buildList([5]), buildList([1, 2, 4]), buildList([1, 2, 4, 5])),
    (buildList([1]), buildList([2]), buildList([1, 2])),
    (buildList([2]), buildList([1]), buildList([1, 2])),
    (buildList([3]), buildList([1, 2]), buildList([1, 2, 3])),
    (buildList([3]), buildList([1, 2, 2]), buildList([1, 2, 2, 3])),
    (buildList([1, 2]), buildList([1, 3]), buildList([1, 1, 2, 3])),
    (buildList([1, 2, 4]), buildList([1, 3, 4]), buildList([1, 1, 2, 3, 4, 4])),
    (None, None, []),
    (None, ListNode(0), ListNode(0)),
])
def test_merge(list1, list2, expected_output):
    solution = Solution()
    output = solution.mergeTwoLists(list1, list2)

    assert print_node_list(output) == print_node_list(expected_output)
    output = solution.mergeTwoLists2(list1, list2)

    assert print_node_list(output) == print_node_list(expected_output)
    output = solution.mergeTwoLists3(list1, list2)

    assert print_node_list(output) == print_node_list(expected_output)
