"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

import pytest


class Solution:
    # Recursive Approach
    # we recursively compute the minimum distance by considering all three operations (insertion, deletion,
    # and replacement) for each character of the strings. It has exponential time complexity due
    # to overlapping subproblems.
    # Time complexity:O(2
    # n
    #  +2
    # m
    #  )
    # Space complexity:O(n+m)
    def solve(self, index1, index2, word1, word2):
        if index1 < 0:
            return index2 + 1
        if index2 < 0:
            return index1 + 1
        if word1[index1] == word2[index2]:
            return self.solve(index1 - 1, index2 - 1, word1, word2)
        insertion = 1 + self.solve(index1, index2 - 1, word1, word2)
        deletion = 1 + self.solve(index1 - 1, index2, word1, word2)
        replacement = 1 + self.solve(index1 - 1, index2 - 1, word1, word2)
        return min(insertion, deletion, replacement)

    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        return self.solve(n1 - 1, n2 - 1, word1, word2)

    #  Memoization Approach
    # This is a top-down dynamic programming approach that caches the results of subproblems to avoid redundant
    # computations. It reduces time complexity to O(n*m) by storing previously calculated results in a DP array.
    # Time complexity:O(n∗m)
    # Space complexity:O(n+m)[Recursive Stack Space]+O(n∗m)[Dp Array]
    def solve2(self, index1, index2, word1, word2, dp):
        if index1 < 0:
            return index2 + 1
        if index2 < 0:
            return index1 + 1
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if word1[index1] == word2[index2]:
            dp[index1][index2] = self.solve2(index1 - 1, index2 - 1, word1, word2, dp)
        else:
            insertion = 1 + self.solve2(index1, index2 - 1, word1, word2, dp)
            deletion = 1 + self.solve2(index1 - 1, index2, word1, word2, dp)
            replacement = 1 + self.solve2(index1 - 1, index2 - 1, word1, word2, dp)
            dp[index1][index2] = min(insertion, deletion, replacement)
        return dp[index1][index2]

    def minDistance2(self, word1, word2):
        n1, n2 = len(word1), len(word2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.solve2(n1 - 1, n2 - 1, word1, word2, dp)

    # The tabulation approach uses a bottom-up dynamic programming approach, filling a DP table. Starting from the base
    # cases, it computes the minimum distance by considering all possible operations for each pair of substrings.
    # Time complexity:O(n∗m)
    # Space complexity:O(n∗m)[Dp Array]
    def minDistance3(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insertion = 1 + dp[i][j - 1]
                    deletion = 1 + dp[i - 1][j]
                    replacement = 1 + dp[i - 1][j - 1]
                    dp[i][j] = min(insertion, deletion, replacement)

        return dp[n1][n2]

    # Space Optimization
    # This approach reduces space complexity by maintaining only two arrays (previous and current rows) instead of the
    # entire DP table. It optimizes memory usage while retaining the O(n*m) time complexity.
    # Time complexity:O(n∗m)
    # Space complexity:O(m+m)
    def minDistance4(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        prev = [j for j in range(n2 + 1)]
        curr = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            curr[0] = i
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insertion = 1 + curr[j - 1]
                    deletion = 1 + prev[j]
                    replacement = 1 + prev[j - 1]
                    curr[j] = min(insertion, deletion, replacement)
            prev = curr[:]

        return prev[n2]

    #
    # Time complexity : O(mn)
    # Space complexity : O(mn)
    def minDistance5(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # no operation is required because the characters at positions i-1 and j-1 are already the same.
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i][j] is the minimum of the following three values:
                    # dp[i-1][j-1] + 1: replace the character at position i-1 in word1 with the character at position
                    # j-1 in word2.
                    # dp[i-1][j] + 1: delete the character at position i-1 in word1.
                    # dp[i][j-1] + 1: insert the character at position j-1 in word2 into word1 at position i.
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        # which represents the minimum number of operations required to transform word1 into word2,
        # where m is the length of word1 and n is the length of word2.
        return dp[m][n]


@pytest.mark.parametrize('word1, word2, expected_output', [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
])
def test_merge(word1, word2, expected_output):
    solution = Solution()
    output = solution.minDistance(word1, word2)

    assert output == expected_output
    output = solution.minDistance2(word1, word2)

    assert output == expected_output
    output = solution.minDistance3(word1, word2)

    assert output == expected_output
    output = solution.minDistance4(word1, word2)

    assert output == expected_output
    output = solution.minDistance5(word1, word2)

    assert output == expected_output
