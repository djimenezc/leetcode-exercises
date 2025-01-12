"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List

import pytest


class Solution:
    # Using backtracking to create all possible combinations
    # Complexity
    # Time complexity: O(3^n) or O(4^n)
    # n is length of input string. Each digit has 3 or 4 letters. For example, if you get "23"(n) as input string,
    # we will create 9 combinations which is O(3^2) = 9
    #
    # Space complexity: O(n)
    # n is length of input string. This is for recursive call stack.
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return

            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")

        return res


@pytest.mark.parametrize('digits, expected_output', [
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("", []),
    ("2", ["a", "b", "c"]),
])
def test_merge(digits, expected_output):
    solution = Solution()
    output = solution.letterCombinations(digits)

    assert output == expected_output
