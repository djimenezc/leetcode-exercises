"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

import pytest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars_map = {}

        for i in range(0, len(s)):
            if chars_map.get(s[i]) is None and not t[i] in chars_map.values():
                chars_map[s[i]] = t[i]
            if chars_map.get(s[i], None) != t[i]:
                return False

        return True


@pytest.mark.parametrize('s, t, expected_output', [
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("badc", "baba", False),
    ("aaaac", "aaaab", True),
    ("aaaac", "aaazb", False),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.isIsomorphic(s, t)

    assert output == expected_output

