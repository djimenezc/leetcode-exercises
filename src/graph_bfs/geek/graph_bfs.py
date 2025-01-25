"""

"""

from collections import deque
from typing import List

import pytest


class Solution:
    # BFS from given source s
    def bfs(self, adj, s) -> List[int]:

        # Create a queue for BFS
        q = deque()
        res = []
        # Initially mark all the vertices as not visited
        # When we push a vertex into the q, we mark it as
        # visited
        visited = [False] * len(adj)

        # Mark the source node as visited and enqueue it
        visited[s] = True
        q.append(s)

        # Iterate over the queue
        while q:

            # Dequeue a vertex from queue and print it
            curr = q.popleft()
            print(curr, end=" ")
            res.append(curr)

            # Get all adjacent vertices of the dequeued
            # vertex. If an adjacent has not been visited,
            # mark it visited and enqueue it
            for x in adj[curr]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)

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
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    solution.add_edge(adj, 0, 1)
    solution.add_edge(adj, 0, 2)
    solution.add_edge(adj, 1, 3)
    solution.add_edge(adj, 1, 4)
    solution.add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    assert solution.bfs(adj, 0) == [0, 1, 2, 3, 4]
