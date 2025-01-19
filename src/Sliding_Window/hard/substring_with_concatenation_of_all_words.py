"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all
concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation
of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].



Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from collections import Counter, defaultdict
from typing import List

import pytest


class Solution:
    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        res = []
        # all words same length
        word_len = len(words[0])
        words_len = len(words)
        n = len(s)
        i = 0
        candidate_index = 0
        permutations_founds = [0] * words_len

        while i < n:
            candidate_word = s[i:i + word_len]
            word_index_found = words.index(candidate_word) if candidate_word in words else -1

            if word_index_found >= 0:
                if candidate_index == -1:
                    candidate_index = i
                permutations_founds[word_index_found] += 1
                i += word_len
                used_word = 0
                # check which words were used and that were use only once
                for x in permutations_founds:
                    if x not in [0, 1]:
                        permutations_founds = [0] * words_len
                        candidate_index = -1
                        i -= word_len
                        break
                    else:
                        used_word += 1 if x == 1 else 0
                        if used_word == words_len:
                            res.append(candidate_index)
                            first_word_permutation = s[candidate_index: candidate_index + word_len]
                            word_index_found = words.index(first_word_permutation)
                            permutations_founds[word_index_found] = 0
                            candidate_index = candidate_index + word_len

            else:
                i += 1

        return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        # all words same length
        word_len = len(words[0])
        word_count = Counter(words)
        words_len = len(words)
        n = len(s)
        i = 0
        candidate_index = 0
        words_found = {key: 0 for key in word_count}

        while i < n:
            candidate_word = s[i:i + word_len]

            if word_count[candidate_word]:
                if candidate_index == -1:
                    candidate_index = i
                words_found[candidate_word] += 1
                i += word_len
                used_word = 0
                # check which words were used and that were use only once
                for x in words_found:
                    if words_found[x] > word_count[x]:
                        words_found = [0] * words_len
                        candidate_index = -1
                        i -= word_len
                        break
                    else:
                        used_word += 1 if x == 1 else 0
                        if used_word == words_len:
                            res.append(candidate_index)
                            first_word_permutation = s[candidate_index: candidate_index + word_len]
                            word_index_found = words.index(first_word_permutation)
                            words_found[word_index_found] = 0
                            candidate_index = candidate_index + word_len
            else:
                i += 1

        return res

    # Slow
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        # word_count = defaultdict(int)
        # for word in words:
        #     word_count[word] += 1
        word_count = Counter(words)

        substr_len = len(words) * len(words[0])
        word_len = len(words[0])
        result = []

        for i in range(len(s) - substr_len + 1):
            seen = defaultdict(int)
            for j in range(i, i + substr_len, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else:
                result.append(i)

        return result

    # Time:   O(n*k), n = length of s, k = length of each word
    # Memory: O(m*k), m = length of words, k = length of each word
    def findSubstring3(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        word_count = Counter(words)
        indexes = []

        for i in range(length):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - length + 1, length):
                word = s[j:j + length]

                if word not in word_count:
                    start = j + length
                    window = defaultdict(int)
                    words_used = 0
                    continue

                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start:start + length]] -= 1
                    start += length
                    words_used -= 1

                if words_used == len(words):
                    indexes.append(start)

        return indexes


@pytest.mark.parametrize('s, str, expected_output', [
    ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
    ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
])
def test_merge(s, str, expected_output):
    solution = Solution()
    output = solution.findSubstring2(s, str)

    assert output == expected_output
    output = solution.findSubstring3(s, str)

    assert output == expected_output
