"""

"""

import pytest


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    def search_recursive(self, root, key):

        # Base Cases: root is null or key
        # is present at root
        if root is None or root.key == key:
            return root

        # Key is greater than root's key
        if root.key < key:
            return self.search_recursive(root.right, key)

        # Key is smaller than root's key
        return self.search_recursive(root.left, key)

    # Function to search in a bst.
    def search_iterative(self, root, x):

        curr = root

        while curr is not None:

            # If curr node is x
            if curr.key == x:
                return True

            # Search in right subtree
            elif curr.key < x:
                curr = curr.right

            # Search in left subtree
            else:
                curr = curr.left

        # If x is not found.
        return False


solution = Solution()


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
class TestCase:
    def test_recursive(self, s, t, expected_output):
        # Creating a hard coded tree for keeping
        # the length of the code small. We need
        # to make sure that BST properties are
        # maintained if we try some other cases.
        root = Node(50)
        root.left = Node(30)
        root.right = Node(70)
        root.left.left = Node(20)
        root.left.right = Node(40)
        root.right.left = Node(60)
        root.right.right = Node(80)

        assert not solution.search_recursive(root, 19)
        assert solution.search_recursive(root, 80)

    def test_iterative(self, s, t, expected_output):
        # Create a hard coded BST.
        #        20
        #       /  \
        #      8   22
        #     / \
        #   4   12
        #       /  \
        #     10   14
        root = Node(20)
        root.left = Node(8)
        root.left.left = Node(4)
        root.left.right = Node(12)
        root.left.right.left = Node(10)
        root.left.right.right = Node(14)
        root.right = Node(22)

        x = 12

        assert solution.search_iterative(root, x)
