"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace"
is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
to see if t has its subsequence. In this scenario, how would you change your code?
"""
import math
import re

import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for x in s:
            if t.find(x) >= 0:
                t = t[t.find(x)+1:]
            else:
                return False

        return True


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", False),
    ("aaaa", "bbaaaa", True),
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("ab", "baab", True)
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.isSubsequence(s, t)

    assert output == expected_output
