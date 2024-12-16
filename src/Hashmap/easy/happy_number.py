"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""
from collections import Counter
from functools import reduce

import pytest


class Solution:
    def isHappy(self, n: int) -> bool:

        visited = {}

        while True:
            digits_list = [int(d) for d in str(n)]

            n = 0
            for x in digits_list:
                n = n + x ** 2

            if n == 1:
                return True
            elif not visited.get(n, False):
                visited[n] = True
            else:
                return False

    def isHappy2(self, n: int) -> bool:
        current_number = n
        number = 0
        numbers = {}

        while True:
            for i in str(current_number):
                number += int(i) ** 2
            if number == 1:
                return True
            if number in numbers:
                return False
            numbers[number] = 0
            current_number = number
            number = 0

    def isHappy3(self, n: int) -> bool:

        visited = {}

        while True:
            number = 0
            for i in str(n):
                number += int(i) ** 2
            n = number

            if n == 1:
                return True
            elif not visited.get(n, False):
                visited[n] = True
            else:
                return False


@pytest.mark.parametrize('n, expected_output', [
    (19, True),
    (2, False),
    (7, True),
    (78, False)
])
def test_merge(n, expected_output):
    solution = Solution()
    output = solution.isHappy(n)

    assert output == expected_output

    output = solution.isHappy2(n)

    assert output == expected_output

    output = solution.isHappy3(n)

    assert output == expected_output
