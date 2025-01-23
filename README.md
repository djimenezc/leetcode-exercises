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
    
# pytest.main(["-s", "-v"])
pytest.main()
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

## Complexity
### O(1)
Constant time complexity. Could be

Hashmap lookup
Array access and update
Pushing and popping elements from a stack
Finding and applying math formula
Typically for n > 10⁹

### O(log(N))
log(N) grows VERY slowly.

In coding interviews, log(N) typically means

Binary search or variant
Balanced binary search tree lookup
Processing the digits of a number
Typically for n > 10⁸

### O(N)
Linear time typically means looping through a linear data structure a constant number of times. Most commonly, this means

- Going through array/linked list
- Two pointers
- Some types of greedy
- Tree/graph traversal
- Stack/Queue
- Typically for n ≤ 10⁶

### O(K log(N))
- Heap push/pop K times. When you encounter problems that seek the "top K elements", 
you can often solve them by pushing and popping to a heap K times, resulting in an O(K log(N)) runtime. e.g., 
K closest points, merge K sorted lists.
- Binary search K times.
- Typically for n ≤ 10⁶

###  O(N log(N))

- Sorting. The default sorting algorithm's expected runtime in all mainstream languages is N log(N). 
For example, java uses a variant of merge sort for object sorting and a variant of Quick Sort for primitive type sorting.
- Divide and conquer with a linear time merge operation. Divide is normally log(N), and if merge is O(N) then 
the overall runtime is O(N log(N)). An example problem is smaller numbers to the right.
- Typically for n ≤ 10⁶

### O(N^2)
Also called quadratic time.

- Nested loops, e.g., visiting each matrix entry
- Many brute force solutions
- Typically for n ≤ 3000

### O(2^N)
Grows very rapidly. Often requires memoization to avoid repeated computations and reduce complexity.

- Combinatorial problems, backtracking, e.g. subsets
- Often involves recursion and is harder to analyze time complexity at first sight
- Further detailed code examples can be found in the backtracking section
- Typically for n ≤ 20

A recursive Fibonacci algorithm is O(2^N) because for any Fib(i) where i > 1, we call Fib(i - 1) and Fib(i - 2).

### O(N!)
Grows insanely rapidly. Only solvable by computers for small N. Often requires memoization to avoid repeated 
computations and reduce complexity.

- Combinatorial problems, backtracking, e.g. permutations
- Often involves recursion and is harder to analyze time complexity at first sight
- Detailed code examples can be found in the backtracking section
- Typically for n ≤ 12

## Big O Notation Practice
Answers for these questions will be at the end of this article.

What is the asymptotic time bound of functions with these time complexities?
- 3N + 2N + N => O(N)
- 2N^3 + 5N^2 => O(N^3)
- N + log(N)  => O(N)
- N^2log(N)   => O(N^2 Log(N))
- 2^N + N^2   => O(2^N)
- 10          => O(1)
- O(2^log(N)) => O(N)

## Keyword to Algorithm

"Top k"
- Heap: K closest points

"How many ways.."
- DFS: Decode ways
- DP: Robot paths

"Substring"
- Sliding window: Longest substring without repeating characters
- "Palindrome"
- two pointers: Valid Palindrome
- DFS: Palindrome Partitioning
- DP: Palindrome Partitioning II

"Tree"
- shortest, level-order
- BFS: Binary Tree Level-Order Traversal
- else: DFS: Max Depth

"Parentheses"
- Stack: Valid Parentheses

"Subarray"
- Sliding window: Maximum subarray sum
- Prefix sum: Subarray sum
- Hashmap: Continuous subarray sum
- Max subarray
- Greedy: Kadane's Algorithm

"X Sum"
- Two pointer: Two sum

"Max/longest sequence"
- Dynamic programming, DFS: Longest increasing subsequence
- mono deque: Sliding window maximum

"Minimum/Shortest"
- Dynamic programming, DFS: Minimal path sum
- BFS: Shortest path

"Partition/split ... array/string"
- DFS: Decode ways

"Subsequence"
- Dynamic programming, DFS: Longest increasing subsequence
- Sliding window: Longest increasing subsequence

"Matrix"
- BFS, DFS: Flood fill, Islands
- Dynamic programming: Maximal square

"Jump"
- Greedy/DP: Jump game

"Game"
- Dynamic programming: Divisor game, Stone game

"Connected component", "Cut/remove" "Regions/groups/connections"
- Union Find: Number of connected components, Redundant connections

Transitive relationship
If the items are related to one another and the relationship is transitive, 
then chances are we can build a graph and use BFS or Union Find.

- string converting to another, BFS: Word Ladder
- string converting to another, BFS, Union Find: Sentence Similarity
- numbers having divisional relationship, BFS, Union Find: Evaluate Division

"Interval"
- Greedy: sort by start/end time and then go through sorted intervals Interval Pattern

## Links:
- https://www.crackingthecodinginterview.com/uploads/6/5/2/8/6528028/cracking_the_coding_skills_-_v6.pdf
- https://www.geeksforgeeks.org/dynamic-programming/
- https://www.geeksforgeeks.org/introduction-to-greedy-algorithm-data-structures-and-algorithm-tutorials/
- https://www.geeksforgeeks.org/introduction-to-backtracking-2/
- https://algo.monster/problems/runtime_summary
- https://algo.monster/problems/keyword_to_algo
- https://www.w3schools.com/python/default.asp
- https://realpython.com/sorting-algorithms-python/
- https://docs.python.org/3/reference/index.html

## Videos
- [Algorithms](https://www.youtube.com/watch?v=KEEKn7Me-ms&list=PLI1t_8YX-ApvMthLj56t1Rf-Buio5Y8KL)
- [Data Structures](https://www.youtube.com/watch?v=IhJGJG-9Dx8&list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX)
- [Big O](https://youtu.be/v4cd1O4zkGw)
- [You only need 150 LeetCode questions](https://www.youtube.com/watch?v=J_a4DEw-kCQ)

