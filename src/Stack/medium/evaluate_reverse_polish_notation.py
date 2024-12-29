"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
import math
from functools import reduce
from typing import List

import pytest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operators = ['+', '-', '*', '/']
        stack = []
        operations = {
            '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y),
            '*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(x) / int(y) if int(y) != 0 else float('inf'),  # Handle division by zero
        }

        for token in tokens:
            if token not in valid_operators:
                stack.append(int(token))
            else:
                calculation = int(reduce(operations[token], stack[-2:]))
                stack = stack[:-2]
                stack.append(calculation)

        return stack.pop()

    def evalRPN2(self, tokens: List[str]) -> int:
        st = []

        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))
            else:
                st.append(int(c))

        return st[0]


@pytest.mark.parametrize('tokens, expected_output', [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
])
def test_merge(tokens, expected_output):
    solution = Solution()
    output = solution.evalRPN(tokens)

    assert output == expected_output
    output = solution.evalRPN2(tokens)

    assert output == expected_output
