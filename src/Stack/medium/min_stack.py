"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

import pytest


# We start by initializing an empty list self.st to represent our stack. This stack will store both the value pushed
# and the minimum value at the time of pushing. By combining these two pieces of information in one stack,
# we avoid the need for a separate data structure to track the minimum values, leading to a more efficient
# and compact design.
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val

        self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", False),
])
def test_merge(s, t, expected_output):
    solution = MinStack()

    solution.push(-2)
    solution.push(0)
    solution.push(-3)
    assert solution.getMin() == -3
    solution.pop()
    assert solution.top() == 0
    assert solution.getMin() == -2
