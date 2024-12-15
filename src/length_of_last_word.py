"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
import math
from typing import List

import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        length_last_word = len(words[len(words) - 1])

        return length_last_word


@pytest.mark.parametrize('s, expected_output', [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
])
def test_merge(s, expected_output):
    solution = Solution()
    output = solution.lengthOfLastWord(s)

    assert output == expected_output
