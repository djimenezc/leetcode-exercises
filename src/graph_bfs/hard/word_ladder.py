"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

"""
from collections import deque
from typing import List

import pytest


class Solution:
    # Intuition
    # The problem requires finding the shortest transformation sequence from a beginWord to an endWord such that:
    #
    # Each transformed word exists in the wordList.
    # Each transformation only changes one character.
    # This can be solved using Breadth-First Search (BFS) because BFS naturally explores all transformations
    # level by level, ensuring we find the shortest path first.
    #
    # Complexity
    # Time complexity:
    # O(N⋅L
    # 2
    #  ) Where N is the number of words in the word list, and L is the length of each word.
    #  For each word, we test all its transformations (L⋅26).
    #
    # Space complexity:
    # O(N+M) Where N is for the queue and M for the set storing the word list.
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert list to set for fast lookup
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])  # BFS queue storing (word, steps)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in range(26):  # Check all possible single character changes
                    transformed = word[:i] + chr(ord('a') + ch) + word[i + 1:]
                    if transformed in wordSet:
                        wordSet.remove(transformed)  # Avoid revisiting
                        queue.append((transformed, steps + 1))

        return 0  # If no valid transformation is found


@pytest.mark.parametrize('beginWord, endWord, wordList, expected_output', [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
])
def test_merge(beginWord, endWord, wordList, expected_output):
    solution = Solution()
    output = solution.ladderLength(beginWord, endWord, wordList)

    assert output == expected_output
