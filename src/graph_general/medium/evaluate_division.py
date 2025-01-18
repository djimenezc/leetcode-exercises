"""
You are given an array of variable pairs equations and an array of real numbers values, where
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that
represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and
that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for
 them.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from typing import List

import pytest


class Solution:
    def dfs(self, node: str, dest: str, graph: dict, visit: set, ans: List[float], temp: float) -> None:
        if node in visit:
            return

        visit.add(node)
        if node == dest:
            ans[0] = temp
            return

        for ne, val in graph[node].items():
            self.dfs(ne, dest, graph, visit, ans, temp * val)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        graph = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        return graph

    # oriented graph where each node represents a variable (a,b,c,...) and
    # each edge (a,b, div) contains a number that says the value of the division from a to b
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        finalAns = []

        for query in queries:
            dividend, divisor = query

            if dividend not in graph or divisor not in graph:
                finalAns.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(dividend, divisor, graph, vis, ans, temp)
                finalAns.append(ans[0])

        return finalAns


@pytest.mark.parametrize('equations, values, queries,expected_output', [
    ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
     [0.50000, 2.00000, -1.00000, -1.00000]),
    ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
     [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]),
    ([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
     [3.75000, 0.40000, 5.00000, 0.20000]),
])
def test_merge(equations, values, queries, expected_output):
    solution = Solution()
    output = solution.calcEquation(equations, values, queries)

    assert output == expected_output
