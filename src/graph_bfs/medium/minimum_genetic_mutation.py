"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2


Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
from collections import deque
from typing import List

import pytest


class Solution:

    # authorslog.com/blog/Mi9WhN6rID
    # Intuition
    # The problem can be approached using Breadth-First Search (BFS) because it involves finding the shortest path
    # (minimum mutations) in an unweighted graph where each gene is a node and edges exist between nodes that can be
    # reached by a single mutation.
    #
    # Approach
    # Convert the bank list into a set for O(1) lookup times.
    # Use a queue to implement BFS, starting with the startGene.
    # Track the number of mutations required.
    # For each gene in the queue, generate all possible single mutations.
    # If a mutated gene is in the bank, add it to the queue and remove it from the bank.
    # If the endGene is found, return the number of mutations.
    # If the queue is exhausted without finding the endGene, return -1.
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        queue = deque([startGene])
        mutations = 0

        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mutations

                for i in range(len(gene)):
                    for c in "ACGT":
                        mutated = gene[:i] + c + gene[i + 1:]
                        if mutated in bankSet:
                            queue.append(mutated)
                            bankSet.remove(mutated)

            mutations += 1

        return -1

    # Each mutation at every step from start gene to end gene must be in gene bank.
    # Mutation is only defined when there is just one alteration in genetic code.
    # If there is three change between start gene and end gene, there must be three valid mutation at different
    # time that led to that genetic condition.
    def minMutation2(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        number_mutations = 0

        for i in range(len(endGene)):
            if endGene[i] != startGene[i]:
                number_mutations += 1

        return number_mutations


@pytest.mark.parametrize('startGene, endGene,bank,  expected_output', [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2),
    ("AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"], -1)
])
def test_merge(startGene, endGene, bank, expected_output):
    solution = Solution()
    output = solution.minMutation(startGene, endGene, bank)

    assert output == expected_output
