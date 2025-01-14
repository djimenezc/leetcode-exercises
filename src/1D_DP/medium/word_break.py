"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from typing import List

import pytest


class Solution:
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            s = s.replace(word, "")

        return s == ""

    # Complexity
    # Time complexity: O(n∗m∗k)
    # n is length of input string.
    # m is number of words in wordDict
    # k is average size of substrings.
    #
    # Space complexity: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                # Check if start is non-negative, meaning the word w can fit within the substring s[0:i].
                # Check if the value dp[start] is True, meaning the substring s[0:start] can be segmented.
                # Check if the substring s[start:i] matches the word w.
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[-1]


@pytest.mark.parametrize("s, word_dict, expected_output", [
    ("cars", ["car", "ca", "rs"], True),
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)
])
def test_merge(s, word_dict, expected_output):
    solution = Solution()
    output = solution.wordBreak(s, word_dict)

    assert output == expected_output
