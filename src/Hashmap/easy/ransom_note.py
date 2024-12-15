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
from collections import Counter

import pytest


class Solution:
    def canConstruct(self, ransomnote: str, magazine: str) -> bool:

        for x in magazine:
            if ransomnote.find(x) > -1:
                ransomnote = ransomnote.replace(x, '', 1)

        if ransomnote == '':
            return True
        else:
            return False

    def canConstruct2(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        # So, basically it will return the difference between the occurrences of each character.
        # Ex:- suppose,
        # st1 = Counter({'d': 1, 'e': 1, 'r': 1, 'o': 1})
        # st2 = Counter({'d': 2, 'i': 2, 'o': 2, 'g': 1, 'e': 1, 'r': 1})
        # so, st1 & st2 will return Counter({'d': 1, 'e': 1, 'r': 1, 'o': 1})
        # therefore, if st1 & st2 == st1, will imply that st1 can be formed from st1.
        if st1 & st2 == st1:
            return True
        return False


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

    output = solution.canConstruct2(ransom_note, magazine)
    assert output == expected_output
