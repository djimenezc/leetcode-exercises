from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildList(nums: List):
    head = ListNode(nums[0])
    current_node = head
    for i in range(1, len(nums)):
        current_node.next = ListNode(nums[i])
        current_node = current_node.next

    return head


def isSameListNode(p: ListNode, q: ListNode) -> bool:
    if not p and not q:
        return True  # Both are None
    if not p or not q:
        return False  # One is None and the other is not
    if p.val != q.val:
        return False  # Values are different

    # Recursively check left and right subtrees
    return isSameListNode(p.next, q.next)
