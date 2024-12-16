"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false



Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
import math
import re
from collections import Counter

import pytest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chars_map = {}
        words_list = s.split(' ')

        if len(pattern) != len(words_list):
            return False

        for i in range(0, len(pattern)):
            if chars_map.get(pattern[i]) is None and not words_list[i] in chars_map.values():
                chars_map[pattern[i]] = words_list[i]
            if chars_map.get(pattern[i], None) != words_list[i]:
                return False

        return True


@pytest.mark.parametrize('pattern, s, expected_output', [
    ("aaa", "aa aa aa aa", False),
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
])
def test_merge(pattern, s, expected_output):
    solution = Solution()
    output = solution.wordPattern(pattern, s)

    assert output == expected_output

