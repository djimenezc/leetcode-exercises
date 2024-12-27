"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.


Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        s = [x for x in s.split(' ') if x != '']
        s_len = len(s)
        i = 0
        while i < s_len - 1 - i:
            temp = s[s_len - 1 - i]
            s[s_len - 1 - i] = s[i]
            s[i] = temp
            i += 1

        return " ".join(s)


@pytest.mark.parametrize('s, expected_output', [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("a good  one two example", "example two one good a"),
])
def test_merge(s, expected_output):
    solution = Solution()
    output = solution.reverseWords(s)

    assert output == expected_output
