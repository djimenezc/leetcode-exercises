"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in
a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix,
 and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

import pytest


class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Fixed size array for 'a' to 'z'
        self.isEnd = False


# - Compact Node Representation:
# Instead of using a full character map for children (like unordered_map or HashMap), use a fixed array of size 26 to
# represent each possible child node. This drastically reduces memory overhead compared to hash-based approaches
# while still maintaining constant-time access.
# - Avoid Redundant Data:
# Instead of storing entire words or additional metadata, only store what is essential for the Trie operations:
# a boolean isEnd to signify the end of a word and the necessary child pointers.
# -Iterative Search and Insertion:
# Keep operations iterative instead of recursive to reduce stack memory usage during function calls.
# Time Complexity:
# Insert: O(m) — m is the length of the word.
# Search:O(m) — m is the length of the word.
# Prefix Search (startsWith): O(m) — m is the length of the prefix.
# Space Complexity:
# O(n.m) , where n is the number of words and m is the average length of the words.
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            # Return the integer that represents the character "a":
            index = ord(char) - ord('a')

            if not node.children[index]:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not node.children[index]:
                return False

            node = node.children[index]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        # Same as search, except there is no isEnd condition at final return
        node = self.root

        for c in prefix:
            index = ord(c) - ord('a')

            if not node.children[index]:
                return False

            node = node.children[index]

        return True


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple")  # return True
    assert not trie.search("app")  # return False
    assert trie.startsWith("app")  # return True
    trie.insert("app")
    assert trie.search("app")  # return True
