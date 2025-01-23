"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
import math
from typing import List

import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ''

        if len(strs) == 1:
            longest_common_prefix = strs[0]
        else:
            for i in range(1, len(strs)):
                temp_prefix = ''
                for k in range(0, len(strs[0])):
                    if k < len(strs[i]) and strs[i][k] == strs[0][k]:
                        temp_prefix = temp_prefix + strs[0][k]
                    else:
                        # Get the common prefix between longest_common_prefix and temp_prefix
                        if len(longest_common_prefix) > len(temp_prefix):
                            longest_common_prefix = temp_prefix
                        break
                if i == 1 and longest_common_prefix == '':
                    longest_common_prefix = temp_prefix

        return longest_common_prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""

                pref = pref[0:pref_len]

        return pref

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        longest_common_prefix = strs[0]

        for x in strs[1:]:
            temp_common_prefix = ''
            for i in range(len(min(longest_common_prefix, x))):
                if longest_common_prefix[i] == x[i]:
                    temp_common_prefix += x[i]
                else:
                    break

            longest_common_prefix = temp_common_prefix

        return longest_common_prefix


@pytest.mark.parametrize('strs, expected_output', [
    (["aba", "c", "b", "a", "ab"], ''),
    (["flower", "flower", "flower", "flower"], "flower"),
    (["a"], "a"),
    (["c", "c"], 'c'),
    (["c", "acc", "ccc"], ''),
    (["flower", "flow", "flight"], "fl"),
    (["falower", "flow", "flight"], "f"),
    (["dog", "racecar", "car"], ""),
])
def test_merge(strs, expected_output):
    solution = Solution()
    output = solution.longestCommonPrefix(strs)

    assert output == expected_output
    output = solution.longestCommonPrefix2(strs)

    assert output == expected_output
    output = solution.longestCommonPrefix3(strs)

    assert output == expected_output
