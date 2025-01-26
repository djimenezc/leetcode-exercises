"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?

https://www.youtube.com/watch?v=ew-E3mHOBT0&t=111s

1. Strategies to Tackle the Problem
Hash Table Method:
This approach involves storing visited nodes in a hash table. During traversal, if a node is encountered that already
 exists in the hash table, a cycle is confirmed.

2. Two-Pointers Method (Floyd's Cycle-Finding Algorithm):
Also known as the "hare and tortoise" algorithm, this method employs two pointers that move at different speeds.
If there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the cycle's existence.
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


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2.next

head3 = ListNode(1)


@pytest.mark.parametrize('head, expected_output', [
    (head1, True),
    (head2, True),
    (head3, False),
])
def test_merge(head, expected_output):
    solution = Solution()
    output = solution.hasCycle(head)

    assert output == expected_output
