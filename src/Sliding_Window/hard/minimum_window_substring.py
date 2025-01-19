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
        # If the length of s is smaller than the length of t,
        # it's impossible for s to contain t. Therefore, return an empty string.
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
        # s using end_index as the index and ch as the character.
        for end_index, ch in enumerate(s):
            # If ch is a required character (its count in char_count is positive),
            # decrement target_chars_remaining because one more required character is included.
            if char_count[ch] > 0:
                target_chars_remaining -= 1
            # Decrease the count of ch in char_count because it's now part of the window
            char_count[ch] -= 1

            # Contract Window
            # the current window contains all required characters.
            if target_chars_remaining == 0:
                # the current window contains all required characters.
                while True:
                    char_at_start = s[start_index]
                    # If its count in char_count is 0, exit the loop because it means this character
                    # is needed for a valid window.
                    if char_count[char_at_start] == 0:
                        break
                    #  increment its count and move start_index to the right to shrink the window.
                    char_count[char_at_start] += 1
                    start_index += 1

                #  Update Minimum Window
                # After contracting the window, check if the current window is smaller than
                # the previously found minimum window.
                if end_index - start_index < min_window[1] - min_window[0]:
                    # update min_window to the new start and end indices.
                    min_window = (start_index, end_index)

                # adjust the character count for the character being removed from the window (s[start_index]).
                char_count[s[start_index]] += 1
                # Increment target_chars_remaining since a required character is no longer in the window.
                target_chars_remaining += 1
                # Move start_index to the right to continue searching for smaller windows.
                start_index += 1

        # After iterating through s, check if a valid window was found.
        # If min_window[1] is still float("inf"), no valid window was found, so return an empty string.
        # Otherwise, return the smallest window substring from s using the indices stored in min_window.
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
