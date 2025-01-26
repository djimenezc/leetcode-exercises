"""
The algorithm starts from a given source and explores all reachable vertices from the given source.
It is similar to Preorder Tree Traversal where we visit the root, then recur for its children.
In a graph, there might be loops. So we use an extra visited array to make sure that we do not process a vertex again.
"""

import pytest


class Solution:

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

    def dfs(self, adj, s):
        visited = [False] * len(adj)

        # list to keep all visited nodes
        node_list = []

        # Call the recursive DFS function
        self.dfs_rec(adj, visited, s, node_list)

        return node_list

    def add_edge(self, adj, s, t):
        # Add edge from vertex s to t
        adj[s].append(t)
        # Due to undirected Graph
        adj[t].append(s)


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        solution.add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    assert solution.dfs(adj, source) == [1, 2, 0, 3, 4]
