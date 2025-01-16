"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""

import pytest


class Solution:
    # dp: A 2D list to store the results of sub-problems.
    # Time Complexity:
    #
    # The solution iterates over each possible (i,j) combination, leading to a time complexity of O(m×n).
    # Space Complexity:
    #
    # The space complexity is O(m×n) due to the 2D dp array.
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp1 = [[False] * (n + 1)] * (m + 1)
        dp[0][0] = True

        # Fill in the first column of dp array, considering only the characters from s2
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill in the first row of dp array, considering only the characters from s1.
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Loop through each possible (i, j) combination, starting from (1, 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        #  indicates whether s3 can be formed by interleaving s1 and s2
        return dp[m][n]

    # The optimization from 2D to 1D DP is based on the observation that the state of dp[i][j] in the 2D DP array
    # depends only on dp[i-1][j] and dp[i][j-1]. Therefore, while iterating through the strings, the current state
    # only depends on the states in the previous row of the 2D DP array, which means we can optimize our space
    # complexity by just keeping track of one row (1D DP).
    # Time Complexity:
    #
    # The solution iterates over each character of s1 and s2 once, leading to a complexity of O(m×n).
    # Space Complexity:
    #
    # The space complexity is optimized to O(min(m,n)) as we're only using a single 1D array instead of a 2D matrix.
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        # This is to ensure that s1 is not longer than s2, which helps in optimizing the space
        # complexity to O(min(m, n)).
        if m < n:
            return self.isInterleave2(s2, s1, s3)

        dp = [False] * (n + 1)
        dp[0] = True

        # For each character in s1, iterate through s2 and update the dp array based on the transition rule:
        # dp[j] = (dp[j] and s1[i] == s3[i+j]) or (dp[j-1] and s2[j] == s3[i+j]).
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # The transition rule checks if the current s3[i+j] can be matched by either s1[i] or s2[j],
        # relying solely on the previous values in the dp array.
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[n]

    # Recursion with Memoization
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        memo = {}

        # The function checks whether the substring s3[k:] can be formed by interleaving s1[i:] and s2[j:].
        def helper(i: int, j: int, k: int) -> bool:
            if k == l:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            ans = False
            if i < m and s1[i] == s3[k]:
                ans = ans or helper(i + 1, j, k + 1)

            if j < n and s2[j] == s3[k]:
                ans = ans or helper(i, j + 1, k + 1)

            # Store the result of each subproblem in the memo dictionary.
            memo[(i, j)] = ans
            return ans

        return helper(0, 0, 0)


@pytest.mark.parametrize('s1, s2, s3, expected_output', [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True)
])
def test_merge(s1, s2, s3, expected_output):
    solution = Solution()
    output = solution.isInterleave(s1, s2, s3)

    assert output == expected_output
    output = solution.isInterleave2(s1, s2, s3)

    assert output == expected_output
    output = solution.isInterleave3(s1, s2, s3)

    assert output == expected_output
