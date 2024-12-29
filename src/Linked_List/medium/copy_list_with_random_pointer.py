"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.

Strategies to Tackle the Problem
Hash Map Method:
This approach leverages a hash map to store the mapping between each node in the original list and its corresponding
node in the copied list.

Interweaving Nodes Method:
This approach cleverly interweaves the nodes of the copied list with the original list, using the structure to adjust
the random pointers correctly, and then separates them.
"""
from typing import Optional

import pytest

from src.Linked_List.Utils import Node, build_node, print_node


class Solution:
    # hashmap
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]

    # Interweaving Nodes
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head

        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head


@pytest.mark.parametrize('head, expected_output', [
    (build_node([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
     build_node([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])),
    (build_node([[1, 1], [2, 1]]), build_node([[1, 1], [2, 1]])),
    (build_node([[3, None], [3, 0], [3, None]]), build_node([[3, None], [3, 0], [3, None]])),
])
def test_merge(head, expected_output):
    solution = Solution()
    output = solution.copyRandomList(head)
    old_str = print_node(output)
    new_str = print_node(expected_output)

    assert new_str == old_str

    output = solution.copyRandomList2(head)
    old_str = print_node(output)
    new_str = print_node(expected_output)

    assert new_str == old_str
