"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []



Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Intuition
When performing a right-side view of a binary tree, the goal is to capture the rightmost node visible at each level.
This can be achieved by traversing the tree level by level, prioritizing the right child of each node. By processing
the right child first, we ensure that the first node encountered at each level is the rightmost node.

Approach
Breadth-First Search (BFS): Use a queue to perform a level-order traversal.
Track Rightmost Nodes:
At each level, add the first node processed (rightmost node at that level) to the result list.
Prioritize Right Nodes:
Add the right child of each node to the queue first, followed by the left child. This ensures that nodes on the right
are processed before nodes on the left.
Complexity
Time complexity: O(n), where n is the number of nodes in the tree. Each node is visited once during the BFS traversal.
Space complexity: O(w), where w is the maximum width of the tree (maximum number of nodes at any level). This is due
to the queue used for BFS.

"""
from collections import deque
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree, is_same_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])  # Initialize a deque (double-ended queue) for BFS

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()  # Remove from the front of the queue

                # Add the first node of this level (rightmost node in our traversal)
                if i == 0:
                    res.append(node.val)

                # Add the right child first, then the left child, to ensure rightmost is processed first
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([1, 2, 3, None, 5, None, 4]), [1, 3, 4]),
    (build_tree([1, 2, 3, 4, None, None, None, 5]), [1, 3, 4, 5]),
    (build_tree([1, None, 3]), [1, 3]),
    (build_tree([]), []),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.rightSideView(root)

    assert output == expected_output
