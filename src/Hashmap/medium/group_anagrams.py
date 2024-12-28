"""
Given an array of strings strs, group the
anagrams
 together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import Counter, defaultdict
from typing import List

import pytest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[""]]

        map_of_anagrams = {}
        for s in strs:
            counter = Counter(s)
            chars_in_string = ', '.join(f'{key}={value}' for key, value in sorted(counter.items()))
            if chars_in_string in map_of_anagrams:
                map_of_anagrams[chars_in_string].append(s)
            else:
                map_of_anagrams[chars_in_string] = [s]

        return list(map_of_anagrams.values())

    # Time complexity: O(m∗nlogn)
    # Space complexity: O(mn)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())


@pytest.mark.parametrize('strs, expected_output', [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    ([], [[""]]),
    (['a'], [["a"]]),
])
def test_merge(strs, expected_output):
    solution = Solution()
    output = solution.groupAnagrams(strs)

    assert output == expected_output
    output = solution.groupAnagrams2(strs)

    assert output == expected_output
    output = solution.groupAnagrams3(strs)

    assert output == expected_output
