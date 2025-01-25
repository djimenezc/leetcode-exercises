"""
Let us now talk about the algorithm that prints all vertices without any source and the graph maybe disconnected.

The idea is simple, instead of calling BFS for a single vertex, we call the above implemented BFS for
 all non-visited vertices one by one.
"""

from collections import deque
from typing import List

import pytest


class Solution:
    # BFS from given source s
    def bfs(self, adj, s, visited: List[bool]) -> List[int]:

        q = deque()  # Create a queue for BFS
        res = []
        # Mark the source node as visited and enqueue it
        visited[s] = True
        q.append(s)

        # Iterate over the queue
        while q:
            curr = q.popleft()  # Dequeue a vertex
            print(curr, end=" ")
            res.append(curr)

            # Get all adjacent vertices of curr
            for x in adj[curr]:
                if not visited[x]:
                    visited[x] = True  # Mark as visited
                    q.append(x)  # Enqueue it

        return res

    def bfs_disconnected(self, adj):
        visited = [False] * len(adj)  # Not visited
        res = []

        for i in range(len(adj)):
            if not visited[i]:
                res = res + self.bfs(adj, i, visited)

        return res

    # Function to add an edge to the graph
    def add_edge(self, adj, u, v: int):
        adj[u].append(v)
        adj[v].append(u)


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    # Number of vertices in the graph
    V = 6

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    solution.add_edge(adj, 0, 1)
    solution.add_edge(adj, 0, 2)
    solution.add_edge(adj, 3, 4)
    solution.add_edge(adj, 4, 5)

    # Perform BFS traversal for the entire graph
    print("BFS starting from 0: ")
    assert solution.bfs_disconnected(adj) == [0, 1, 2, 3, 4, 5]
