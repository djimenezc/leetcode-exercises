"""

"""
from collections import defaultdict

import pytest


class Solution:
    # Use a sliding window to find the smallest range that contains all characters in string t.
    # Approach:
    #
    # Using HashMap: A HashMap is used to keep track of the frequency of each character,
    # allowing efficient management of character counts.
    # Target Character Management: Track the frequency of characters in T and calculate the minimum window size when
    # all target characters are included in the window.
    # Window Minimization: Expand the window to include more characters and contract it to find the smallest
    # valid window.
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case Handling
        if len(s) < len(t):
            return ""

        # store the frequency of each character in t
        char_count = defaultdict(int)
        for ch in t:
            char_count[ch] += 1

        # tracks how many characters from t are still needed in the current window.
        # Initially, it's set to the length of t
        target_chars_remaining = len(t)
        # holds the start and end indices of the smallest window found.
        # Initialize with (0, float("inf")), indicating no valid window found yet.
        min_window = (0, float("inf"))
        # the beginning of the current window in s.
        start_index = 0

        #  Expand Window
        for end_index, ch in enumerate(s):
            if char_count[ch] > 0:
                target_chars_remaining -= 1
            char_count[ch] -= 1

            if target_chars_remaining == 0:
                while True:
                    char_at_start = s[start_index]
                    if char_count[char_at_start] == 0:
                        break
                    char_count[char_at_start] += 1
                    start_index += 1

                if end_index - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)

                char_count[s[start_index]] += 1
                target_chars_remaining += 1
                start_index += 1

        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1] + 1]


@pytest.mark.parametrize('s, t, expected_output', [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", "")
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.minWindow(s, t)

    assert output == expected_output
