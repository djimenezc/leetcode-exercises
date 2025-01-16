# leetcode-exercises

Repository with multiple solutions in Python to resolve 
Leetcode exercises.

https://leetcode.com/studyplan/top-interview-150/

--log-cli-level=10

## coderpad.io

```python
import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        return True


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.isSubsequence(s, t)

    assert output == expected_output
    
pytest.main(["-s", "-v"])
```

## solution template

- Intuition
- Approach
- Complexity

## Techniques

- Hashmap
- Stack
- Heap [average_of_levels_in_binary_tree.py](src%2Fbinary_tree_bfs%2Feasy%2Faverage_of_levels_in_binary_tree.py)
- Divide and conquer
- Two Pointers
- Binary search
- Greedy Algorithm
  -  builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate 
     benefit. Greedy algorithms are used for optimization problems.
- Dynamic programing
- Backtracking
- Binary tree: https://www.javatpoint.com/bfs-vs-dfs
	- DFS: Depth First Search, the stack data structure is used, which works on the LIFO (Last In First Out) principle
	- BFS: Breadth First Search, level order traversal.[rotate_list.py](src%2FLinked_List%2Fmedium%2Frotate_list.py)
      - use deque
- Heap
  - use heapq.heapify(heap)

## Data structures
- Hash Tables
- Linked Lists
- Stacks
- Queues
- Trees
- Trie
- Graphs
- Vectors
- Heaps

## Links:
- https://www.crackingthecodinginterview.com/uploads/6/5/2/8/6528028/cracking_the_coding_skills_-_v6.pdf
- https://www.geeksforgeeks.org/dynamic-programming/
- https://www.geeksforgeeks.org/introduction-to-greedy-algorithm-data-structures-and-algorithm-tutorials/
- https://www.geeksforgeeks.org/introduction-to-backtracking-2/

## Videos
- [Algorithms](https://www.youtube.com/watch?v=KEEKn7Me-ms&list=PLI1t_8YX-ApvMthLj56t1Rf-Buio5Y8KL)
- [Data Structures](https://www.youtube.com/watch?v=IhJGJG-9Dx8&list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX)
- [Big O](https://youtu.be/v4cd1O4zkGw)
- [You only need 150 LeetCode questions](https://www.youtube.com/watch?v=J_a4DEw-kCQ)