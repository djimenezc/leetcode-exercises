"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict
from typing import List

import pytest


class Solution:
    # In summary, the algorithm performs a depth-first search to check if it is possible to finish all the courses
    # given their prerequisites. It uses a dictionary to store the prerequisites for each course and a set to keep
    # track of the visited courses during the traversal. If there is a cycle in the course dependencies or
    # if any course cannot be finished, it returns False; otherwise, it returns True.
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        # store the prerequisites for each course
        for course, p in prerequisites:
            pre[course].append(p)

        # keep track of the courses that have been visited during the depth-first search (DFS) traversal.
        taken = set()

        # perform the DFS traversal to check if the course can be finished.
        def dfs(course):
            # If the list of prerequisites for the current course is empty
            # (i.e., there are no remaining prerequisites), return True since the course can be finished.
            if not pre[course]:
                return True

            # If the course is already present in the taken set,
            # return False since there is a cycle in the course dependencies.
            if course in taken:
                return False

            # Add the course to the taken set to mark it as visited.
            taken.add(course)

            # Iterate over each prerequisite p for the current course in the pre dictionary:
            for p in pre[course]:
                if not dfs(p):
                    return False

            # Set the list of prerequisites for the current course in the pre dictionary to an empty list,
            # indicating that all the prerequisites have been satisfied.
            pre[course] = []

            # True at the end of the dfs function since all the prerequisites for the course have been satisfied.
            return True

        for course in range(num_courses):
            if not dfs(course):
                # the course cannot be finished,
                return False

        # all the courses can be finished,
        return True


@pytest.mark.parametrize('num_courses, prerequisites, expected_output', [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False)
])
def test_merge(num_courses, prerequisites, expected_output):
    solution = Solution()
    output = solution.canFinish(num_courses, prerequisites)

    assert output == expected_output
