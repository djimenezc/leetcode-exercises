"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from typing import Optional

import pytest

from src.Linked_List.Utils import ListNode, build_list_node, is_same_list_node


class Solution:

    # intuition
    # Create a small list and a big list.
    # Time complexity: O(n)
    # The code iterates through the entire linked list once to partition the nodes into two separate lists
    # based on the value of x.
    #
    # Space complexity: O(1)
    # The code uses a constant amount of extra space for the two dummy nodes slist and blist, as well as
    # for the small and big pointers. The additional space used does not scale with the input size (linked list length)
    # but remains constant throughout the execution.
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist, blist = ListNode(), ListNode()
        small, big = slist, blist  # dummy lists

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next

        small.next = blist.next
        big.next = None  # prevent linked list circle

        return slist.next


@pytest.mark.parametrize('head, x, expected_output', [
    (build_list_node([1, 4, 3, 2, 5, 2]), 3, build_list_node([1, 2, 2, 4, 3, 5])),
    (build_list_node([2, 1]), 2, build_list_node([1, 2])),
])
def test_merge(head, x, expected_output):
    solution = Solution()
    output = solution.partition(head, x)

    assert is_same_list_node(output, expected_output)
