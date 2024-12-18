"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
import math
import re
from collections import Counter
from typing import List

import pytest


class Solution:
    def isValid(self, s: str) -> bool:

        lifo = []
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']

        for x in s:
            if len(lifo) != 0 and x in close_brackets and lifo[len(lifo) - 1] == open_brackets[close_brackets.index(x)]:
                lifo.pop()
            else:
                lifo.append(x)

        return len(lifo) == 0

    def isValid2(self, s):
        stack = []  # create an empty stack to store opening brackets
        for c in s:  # loop through each character in the string
            if c in '([{':  # if the character is an opening bracket
                stack.append(c)  # push it onto the stack
            else:  # if the character is a closing bracket
                if not stack or \
                        (c == ')' and stack[-1] != '(') or \
                        (c == '}' and stack[-1] != '{') or \
                        (c == ']' and stack[-1] != '['):
                    return False  # the string is not valid, so return false
                stack.pop()  # otherwise, pop the opening bracket from the stack
        return not stack
        # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
        # so the string is valid, otherwise, there are unmatched opening brackets, so return false

    def isValid3(self, s):

        while True:
            if s.find("()") != -1:
                s = s.replace("()", "")
            elif s.find("[]") != -1:
                s = s.replace("[]", "")
            elif s.find("{}") != -1:
                s = s.replace("{}", "")
            else:
                return len(s) == 0

    def isValid4(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


@pytest.mark.parametrize('s, expected_output', [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
])
def test_merge(s, expected_output):
    solution = Solution()
    output = solution.isValid(s)

    assert output == expected_output
    output = solution.isValid2(s)

    assert output == expected_output
    output = solution.isValid3(s)

    assert output == expected_output
    output = solution.isValid4(s)

    assert output == expected_output
