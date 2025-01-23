"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
import math
from typing import List

import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1


@pytest.mark.parametrize('haystack, needle, expected_output', [
    ("sadbutsad", "sad", 0),
    ("aaasadbutsad", "sad", 3),
    ("leetcode", "leeto", -1),
])
def test_merge(haystack, needle, expected_output):
    solution = Solution()
    output = solution.strStr(haystack, needle, )

    assert output == expected_output
