"""
prints all vertices without any source and the graph maybe disconnected.

The idea is simple, instead of calling DFS for a single vertex, we call the above implemented DFS for all all
 non-visited vertices one by one.
"""

import pytest


class Solution:

    def __init__(self, vertices):
        # Adjacency list representation of the graph
        self.adj = [[] for _ in range(vertices)]

    def dfs_rec(self, adj, visited, s, node_list):
        # Mark the current vertex as visited
        visited[s] = True

        # Print the current vertex
        print(s, end=" ")
        node_list.append(s)

        # Recursively visit all adjacent vertices
        # that are not visited yet
        for i in adj[s]:
            if not visited[i]:
                self.dfs_rec(adj, visited, i, node_list)

    def dfs(self):
        visited = [False] * len(self.adj)

        # list to keep all visited nodes
        node_list = []

        # Loop through all vertices to handle disconnected
        # graph
        for i in range(len(self.adj)):
            if not visited[i]:
                # Perform DFS from unvisited vertex
                self.dfs_rec(self.adj, visited, i, node_list)

        return node_list

    def add_edge(self, s, t):
        # Add edge from vertex s to t
        self.adj[s].append(t)
        # Due to undirected Graph
        self.adj[t].append(s)


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    # Number of vertices in the graph
    V = 6

    solution = Solution(V)

    # Define the edges of the graph
    edges = [(1, 2), (2, 0), (0, 3), (4, 5)]

    # Populate the adjacency list with edges
    for e in edges:
        solution.add_edge( e[0], e[1])

    assert solution.dfs() == [0, 2, 1, 3, 4, 5]
