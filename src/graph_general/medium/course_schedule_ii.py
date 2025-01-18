"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return
any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    # it's using BFS, rather than the prototypical DFS Topo approach.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a prerequisite dict. containing courses (nodes) that need to be taken (visited)
        # before we can visit the key.
        preq = {i: set() for i in range(numCourses)}
        # Create a graph for adjacency and traversing.
        graph = defaultdict(set)
        for i, j in prerequisites:
            # Preqs store requirements as their given.
            preq[i].add(j)
            # Graph stores nodes and neighbors.
            graph[j].add(i)

        q = deque([])
        # We need to find a starting location, aka courses that have no prereqs.
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
            # Keep track of which courses have been taken.
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            # If we have visited the numCourses we're done.
            if len(taken) == numCourses:
                return taken
            # For neighboring courses.
            for cor in graph[course]:
                # If the course we've just taken was a prereq for the next course, remove it from its prereqs.
                preq[cor].remove(course)
                # If we've taken all the preqs for the new course, we'll visit it.
                if not preq[cor]:
                    q.append(cor)
            # If we didn't hit numCourses in our search we know we can't take all the courses.
        return []

    def findOrder2(self, numCourses, prerequisites):
        topo = []
        # pre-requisite adjacency map. Key's = course, and Values = pre-requisite course.
        preq = {i: set() for i in range(numCourses)}
        # graph adjacency map. Key's = Pre-Requisite course. Values = the courses that depend on the Key.
        graph = defaultdict(set)

        for i, j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)
        # Locate a starting node - a course without dependencies.
        q = deque([k for k, v in preq.items() if not v])

        while q:
            course = q.popleft()
            # Pop off the Queue, add the Course pop'd to the topo result.
            topo.append(course)
            # If the topo length == number of courses, we know we're finished.
            if len(topo) == numCourses:
                return topo
            # Iterate over the neighbors for the given course, finding all neighbors that are blocked
            # by the current node.
            # Remove the current node from all those neighbor's pre-requisite lists.
            for cor in graph[course]:
                # Looking within the pre-requisite adjacency map,
                # if a neighbor has no more pre-requisites, then we know it's safe to take that course,
                # so add it to the Queue.
                preq[cor].remove(course)
                if not preq[cor]:
                    q.append(cor)

        # it's impossible to take the course
        return []


@pytest.mark.parametrize('numCourses, prerequisites,expected_output', [
    (2, [[1, 0]], [0, 1]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
    (1, [], [0])
])
def test_merge(numCourses, prerequisites, expected_output):
    solution = Solution()
    output = solution.findOrder(numCourses, prerequisites)
    expected_output.sort()

    assert output == expected_output

    output = solution.findOrder2(numCourses, prerequisites)

    assert output == expected_output

