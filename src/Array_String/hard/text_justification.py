"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra
spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be
left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is",
"everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List

import pytest


class Solution:
    def fullJustify1(self, words: List[str], maxWidth: int) -> List[str]:

        res = [""]
        line_pos = 0
        n = len(words)

        for i in range(n):
            if len(words[i]) + len(res[line_pos]) < maxWidth:
                res[line_pos] += words[i]
                # last line case is handled outside the loop
                # is last word in line_pos line
                if i != n - 1 and len(res[line_pos]) + len(words[i + 1]) > maxWidth:
                    res[line_pos] += ''.join([" "] * (maxWidth - len(res[line_pos])))
                else:
                    res[line_pos] += ' '
            else:
                res.append(words[i])
                line_pos += 1

        # fill last line with spaces up to maxWidth
        res[line_pos] += ''.join([" "] * (maxWidth - len(res[line_pos])))

        return res

    # To solve the "Text Justification" problem using this approach, we pack words into each line using a greedy
    # strategy. We then distribute spaces among the words on each line, using modulo arithmetic to decide where
    # to place the extra spaces.
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % (len(line) - 1 or 1)] += ' '
                res, line, width = res + [''.join(line)], [], 0
            line += [w]
            width += len(w)

        return res + [' '.join(line).ljust(maxWidth)]

    # Code Gap-based
    # Time Complexity: Both approaches process each word once and have a time complexity of O(n),
    # where n is the number of words.
    # the way we pack words into each line remains similar to the first approach. However, when it comes to
    # distributing spaces, the logic is a tad different. Instead of using modulo arithmetic directly, we compute
    # the number of gaps between words and then decide how many spaces to put in each gap. This makes the logic
    # more intuitive.
    # Space Complexity: The space complexity for both methods is O(n×m), where n is the number of words
    # and m is the average length of the words.
    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur_words, cur_len = [], [], 0

        for word in words:
            if cur_len + len(word) + len(cur_words) > maxWidth:
                total_spaces = maxWidth - cur_len
                gaps = len(cur_words) - 1
                if gaps == 0:
                    res.append(cur_words[0] + ' ' * total_spaces)
                else:
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    line = ''
                    for i, w in enumerate(cur_words):
                        line += w
                        if i < gaps:
                            line += ' ' * space_per_gap
                            if i < extra_spaces:
                                line += ' '
                    res.append(line)
                cur_words, cur_len = [], 0
            cur_words.append(word)
            cur_len += len(word)

        last_line = ' '.join(cur_words)
        remaining_spaces = maxWidth - len(last_line)
        res.append(last_line + ' ' * remaining_spaces)

        return res


@pytest.mark.parametrize('words, maxWidth, expected_output', [
    (["This", "is", "an", "example"], 16, [
        "This    is    an",
        "example         ",
    ]),
    # (["This", "is", "an", "example", "of", "text", "justification."], 16, [
    #     "This    is    an",
    #     "example  of text",
    #     "justification.  "
    # ]),
    # (["What", "must", "be", "acknowledgment", "shall", "be"], 16, [
    #     "What   must   be",
    #     "acknowledgment  ",
    #     "shall be        "
    # ]),
    # (["Science", "is", "what", "we", "understand",
    #   "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20,
    #  [
    #      "Science  is  what we",
    #      "understand      well",
    #      "enough to explain to",
    #      "a  computer.  Art is",
    #      "everything  else  we",
    #      "do                  "
    #  ]
    #  ),
])
def test_merge(words, maxWidth, expected_output):
    solution = Solution()
    output = solution.fullJustify(words, maxWidth)

    assert output == expected_output
    output = solution.fullJustify2(words, maxWidth)

    assert output == expected_output
