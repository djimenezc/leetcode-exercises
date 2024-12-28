"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

import pytest


class Solution:

    # Sliding Window & Set
    # Time complexity: O(n)
    # Space complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    # Solution 2 - Sliding Window and Hashing
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Every time we find a character, add 1 frequency to HashMap. Since this question requires us to find the
    # longest substring without repeating characters, so if we have more than 2 frequency of the current character,
    # we add -1 to HashMap until we have 1 frequency of the current character and move left pointer to the next at
    # the same time.
    #
    # After that, this is the same as solution 1. Just compare max length
    #
    # max_length = max(max_length, right - left + 1)
    def lengthOfLongestSubstring2(self, s: str) -> int:

        max_length = left = 0
        count = {}

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    # hashmap: the last position where each character was seen
    # Time complexity: O(n)
    # Space complexity: O(1)
    # We update left pointer with HashMap. In HashMap, we keep each character as a key and the last position
    # where each character was seen　as a value.
    def lengthOfLongestSubstring3(self, s: str) -> int:
        max_length = 0
        left = 0
        last_seen = {}

        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1

            max_length = max(max_length, right - left + 1)
            last_seen[c] = right

        return max_length


@pytest.mark.parametrize('s, expected_output', [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test_merge(s, expected_output):
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s)

    assert output == expected_output
    output = solution.lengthOfLongestSubstring2(s)

    assert output == expected_output
    output = solution.lengthOfLongestSubstring3(s)

    assert output == expected_output
