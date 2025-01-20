from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def build_node(nums: List) -> Node:
    if not nums:
        return None

        # Step 1: Create all nodes and store them in a list for reference
    nodes = [Node(val) for val, _ in nums]

    # Step 2: Link the `next` pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Step 3: Link the `random` pointers
    for i, (_, random_index) in enumerate(nums):
        if random_index is not None:  # If a random pointer exists
            nodes[i].random = nodes[random_index]

    return nodes[0]


def print_node(head: Node):
    current = head
    str = ''
    while current:
        random_val = current.random.val if current.random else None
        str += f"Node(val={current.val}, random={random_val})"
        print(f"Node(val={current.val}, random={random_val})")
        current = current.next
    return str


def print_list_node(head: ListNode):
    current = head
    str = ''
    while current:
        str += f"Node(val={current.val})"
        print(str)
        current = current.next
    return str


def build_list_node(nums: List) -> ListNode:
    head = ListNode(nums[0])
    current_node = head
    for i in range(1, len(nums)):
        current_node.next = ListNode(nums[i])
        current_node = current_node.next

    return head


def is_same_list_node(p: ListNode, q: ListNode) -> bool:
    if not p and not q:
        return True  # Both are None
    if not p or not q:
        return False  # One is None and the other is not
    if p.val != q.val:
        return False  # Values are different

    # Recursively check left and right subtrees
    return is_same_list_node(p.next, q.next)
