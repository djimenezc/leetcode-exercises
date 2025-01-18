"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.


Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""
from collections import deque
from typing import Optional, List

import pytest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list: Optional[List[Optional[List[int]]]]) -> Node:
    if not adj_list:
        return None

        # Step 1: Create a list of nodes (1-based index)
    nodes = [Node(i) for i in range(1, len(adj_list) + 1)]

    # Step 2: Connect the nodes based on the adjacency list
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]  # Adjust for 0-based indexing

    # Return the first node (or the graph as a whole, depending on your needs)
    return nodes[0]


def are_graphs_equal(node1, node2):
    # Helper function to traverse and compare two graphs
    def dfs(node_a, node_b, visited_a, visited_b):
        # If both nodes are None, they are equal
        if not node_a and not node_b:
            return True
        # If one is None or their values differ, they are not equal
        if not node_a or not node_b or node_a.val != node_b.val:
            return False

        # Mark the nodes as visited
        visited_a.add(node_a)
        visited_b.add(node_b)

        # Check neighbors' lengths
        if len(node_a.neighbors) != len(node_b.neighbors):
            return False

        # Compare neighbors recursively
        for neighbor_a, neighbor_b in zip(sorted(node_a.neighbors, key=lambda x: x.val),
                                          sorted(node_b.neighbors, key=lambda x: x.val)):
            if neighbor_a not in visited_a and neighbor_b not in visited_b:
                if not dfs(neighbor_a, neighbor_b, visited_a, visited_b):
                    return False
            elif (neighbor_a in visited_a) != (neighbor_b in visited_b):
                return False  # One neighbor visited and the other is not

        return True

    # Edge case: if both graphs are empty
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False

    # Initialize visited sets
    visited1, visited2 = set(), set()

    return dfs(node1, node2, visited1, visited2)


class Solution:
    # To solve this problem we need two things:
    #
    # BFS to traverse the graph
    # A hash map to keep track of already visited and already cloned nodes
    # We push a node in the queue and make sure that the node is already cloned.
    # Then we process neighbors. If a neighbor is already cloned and visited,
    # we just append it to the current clone neighbors list, otherwise, we clone it first and append it to
    # the queue to make sure that we can visit it in the next tick.
    #
    # Time: O(V + E) - for BFS
    # Space: O(V) - for the hashmap
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}

        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                cur_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]


@pytest.mark.parametrize('node', [
    (build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])),
    (build_graph([[]])),
    (build_graph([]))
])
def test_merge(node):
    solution = Solution()
    output = solution.cloneGraph(node)

    assert are_graphs_equal(node, output)
