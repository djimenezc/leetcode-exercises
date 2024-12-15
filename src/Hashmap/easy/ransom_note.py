"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
import math
import re

import pytest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for x in magazine:
            if ransomnote.find(x) > -1:
                ransomnote = ransomnote.replace(x, '', 1)

        if ransomnote == '':
            return true
        else:
            return false


@pytest.mark.parametrize('ransom_note, magazine, expected_output', [
    ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
])
def test_merge(ransom_note, magazine, expected_output):
    solution = Solution()
    output = solution.canConstruct(ransom_note, magazine)

    assert output == expected_output
