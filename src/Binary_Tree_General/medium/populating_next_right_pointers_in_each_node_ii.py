"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.



"""
from collections import deque

import pytest


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def buildTree(nodes: list) -> Node:
    n = len(nodes)

    if n == 0:
        return None

    parentStack = deque()
    root = Node(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = Node(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = Node(nodes[i])
                parentStack.append(curParent.right)

            curParent = parentStack.popleft()

    return root


def isSameTree(p: Node, q: Node) -> bool:
    if not p and not q:
        return True  # Both are None
    if not p or not q:
        return False  # One is None and the other is not
    if p.val != q.val:
        return False  # Values are different

    # Recursively check left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


class Solution:

    # Level Order Traversal Approach
    # As the problem states that the output should return a tree with all the nodes in the same level connected,
    # the problem can be solved using Level Order Traversal.
    # Each iteration of Queue traversal, the code would:
    #
    # Find the length of the current level of the tree.
    # Iterate through all the nodes in the same level using the level length.
    # Find the siblings in the next level and connect them using next pointers. Enqueue all the nodes in the next level.

    # Time = O(N) - iterate through all the nodes
    # Space=O(L) - As the code is using level order traversal, the maximum size of Queue is maximum number of nodes at any level.
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        q.append(root)
        dummy = Node(-999)  # to initialize with a not null prev
        while q:
            length = len(q)  # find level length

            prev = dummy
            for _ in range(length):  # iterate through all nodes in the same level
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                    prev.next = popped.left
                    prev = prev.next
                if popped.right:
                    q.append(popped.right)
                    prev.next = popped.right
                    prev = prev.next

        return root

    # O(1) Space Approach
    # In addition to this, there is a follow-up question asking to solve this problem using constant extra space.
    # There is an additional hint to maybe use recursion for this and the extra call stack is assumed to be O(1) space
    #
    # The code will track the head at each level and use that not null head to define the next iteration.
    # Following is my take on O(1) space solution:
    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return None

        curr = root
        dummy = Node(-999)
        head = root

        while head:
            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal
            # iterate through the linked-list of the current level and connect all the siblings in the next level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node

        return root


@pytest.mark.parametrize('root, expected_output', [
    # (buildTree([1, 2, 3, 4, 5, None, 7]), buildTree([1, '#', 2, 3, '#', 4, 5, 7, '#'])),
    (buildTree([]), buildTree([])),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.connect(root)

    assert isSameTree(output, expected_output)
