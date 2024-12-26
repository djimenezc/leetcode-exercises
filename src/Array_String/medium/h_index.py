"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their
ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the
given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5
citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations
each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""
from typing import List

import pytest


class Solution:

    # First of all, we need to sort a citations array in ascending order.
    # Next, we iterate through the citations array and track the case where citations[i] is greater than n - i which
    # means that we have at least n - i articles with n - i citations which is our h-index value.
    # Finally, we just return the answer n - i in that case.
    # Time complexity: O(n∗log(n))
    # Space complexity: O(log(n))
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0

    # Sorting: Sorts the citations list in ascending order.
    # Iterative Check: Iterates through the sorted list.
    # For each citation v at index i:
    # If n - i (number of articles with at least n - i citations) is less than or equal to v itself
    # (the current citation count), it means the h-index is n - i.
    # Returns n - i as the h-index.
    # Default Return: If no valid h-index is found, returns 0.
    def hIndex2(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0

    # Frequency Array: Creates a temporary array temp of size n + 1 to store citation frequencies.
    # Counting Citations: Iterates through the citations list:
    # If a citation v is greater than n, adds it to the highest frequency bucket (temp[n]).
    # Otherwise, increments the count in the corresponding bucket (temp[v]).
    # Calculating h-index: Iterates backward through the temp array:
    # Accumulates the total number of citations up to each index i.
    # If the total count (total) is greater than or equal to i itself, it means i is the h-index.
    # Returns i as the h-index.
    def hIndex3(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]

        for i, v in enumerate(citations):
            if v > n:
                temp[n] += 1
            else:
                temp[v] += 1

        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i


@pytest.mark.parametrize('citations, expected_output', [
    ([3, 0, 6, 1, 5], 3),
    ([1, 3, 1], 1),
])
def test_merge(citations, expected_output):
    solution = Solution()
    output = solution.hIndex(citations)

    assert output == expected_output
    output = solution.hIndex2(citations)

    assert output == expected_output
    output = solution.hIndex3(citations)

    assert output == expected_output
