"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

import pytest


class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(i):
            res, digit, sign = 0, 0, 1

            while i < len(s):
                if s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                elif s[i] in '+-':
                    res += digit * sign
                    digit = 0
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    subres, i = evaluate(i + 1)
                    res += sign * subres
                elif s[i] == ')':
                    res += digit * sign
                    return res, i
                i += 1

            return res + digit * sign

        return evaluate(0)

    def calculate2(self, s: str) -> int:
        """
        1. Take 3 containers:
        num -> to store current num value only
        sign -> to store sign value, initially +1
        res -> to store sum
        When ( comes these containers used for calculate sum of intergers within () brackets.
        --------------------
        2. When c is + or -
        Move num to res, because we need to empty num for next integer value.
        set num = 0
        sign = update with c
        --------------------
        3. When c is '('
        Here, we need num, res, sign to calculate sum of integers within ()
        So, move num and sign to stack => [num, sign]
        Now reset - res = 0, num = 0, sign = 1 (default)
        --------------------
        4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
        res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
        res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
        res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
        --------------------
        Simple Example: 2 - 3
        Initially res will have 2,i.e. res = 2
        then store '-' in sign. it will be used when 3 comes. ie. sign = -1
        Now 3 comes => res = res + num*sign
        Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
        """
        num = 0
        sign = 1
        res = 0
        stack = []
        for i in range(len(s)):  # iterate till last character
            c = s[i]
            if c.isdigit():  # process if there is digit
                num = num * 10 + int(c)  # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in '-+':  # check for - and +
                res += num * sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign


@pytest.mark.parametrize('s, expected_output', [
    ("100 + 1", 101),
    ("1 + 1", 2),
    (" 2-1 + 2 ", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23)
])
def test_merge(s, expected_output):
    solution = Solution()
    output = solution.calculate(s)

    assert output == expected_output
    output = solution.calculate2(s)

    assert output == expected_output
