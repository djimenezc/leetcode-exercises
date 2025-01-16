"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

import pytest


class Solution:

    # Time complexity: O(n
    # 2
    #  )
    # "n" is the length of the input string "s." This is because the code uses nested loops.
    # The outer loop runs for each character in the string, and the inner loop, expand_around_center,
    # can potentially run for the entire length of the string in the worst case, leading to a quadratic time complexity.
    #
    # Space complexity: O(1)
    # the code uses a constant amount of extra space for variables like "start," "end," "left," "right," and function
    # parameters. The space used does not depend on the size of the input string.
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # This function is responsible for expanding the palindrome around the center indices
        # and returns the length of the palindrome.
        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for i in range(len(s)):
            # expand around it by calling the expand_around_center function with two different center possibilities:
            # (i) the current character as the center (odd length palindrome), and
            # (ii) the current character and the next character as the center (even length palindrome).
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)

            # Check if the max_len is greater than the length of the current longest palindromic substring (end - start)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    # how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa".
    # If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two
    # left and right end letters are the same.
    # Time complexity : O(n^2). This gives us a runtime complexity of O(n^2).
    #
    # Space complexity : O(n^2). It uses O(n^2) space to store the table.
    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            # We will iterate over the string and mark the diagonal elements as true as every
            # single character is a palindrome.
            dp[i][i] = True
            # iterate over the string and for every character we will expand around its center.
            for j in range(i):
                # For odd length palindrome, we will consider the current character as the center and expand around it.
                # For even length palindrome, we will consider the current character and the next character
                # as the center and expand around it.
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j:i + 1]

        return max_str


@pytest.mark.parametrize('s, expected_output', [
    ("bab", "bab"),
    ("babad", ["bab", "aba"]),
    ("cbbd", "bb")
])
def test_merge(s, expected_output):
    solution = Solution()
    output = solution.longestPalindrome(s)

    assert output in expected_output
    output = solution.longestPalindrome2(s)

    assert output in expected_output
