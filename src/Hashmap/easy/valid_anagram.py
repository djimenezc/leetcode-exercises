"""
Given two strings s and t, return true if t is an
anagram
 of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter

import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for x in s:
            if x in t:
                t = t.replace(x, '',1)

        return t == ''

    def isAnagram2(self, s: str, t: str) -> bool:
        st1, st2 = Counter(s), Counter(t)

        if st1 == st2:
            return True
        else:
            return False


@pytest.mark.parametrize('s, t, expected_output', [
    ("ab", "a", False),
    ("anagram", "nagaram", True),
    ("rat", "cat", False),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.isAnagram(s, t)

    assert output == expected_output

    output = solution.isAnagram2(s, t)
    assert output == expected_output




