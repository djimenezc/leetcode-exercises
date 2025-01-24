"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
 Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
 The same principle applies to the number nine, which is written as IX.
 There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

from collections import OrderedDict

import pytest


class Solution:
    values = OrderedDict([
        ('I', 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ])

    def romanToInt(self, s: str) -> int:
        res = 0
        # start from the right of the string to evaluate the chars
        i = len(s) - 1

        # stop after passing position 0
        while i > -1:
            if i != 0 and (s[i] == 'V' and s[i - 1] == 'I' or s[i] == 'X' and s[i - 1] == 'I' or
                           s[i] == 'L' and s[i - 1] == 'X' or s[i] == 'C' and s[i - 1] == 'X' or
                           s[i] == 'M' and s[i - 1] == 'C' or s[i] == 'D' and s[i - 1] == 'C'):
                res += self.values.get(s[i]) - self.values.get(s[i - 1])
                i = i - 2
            else:
                res += self.values.get(s[i])
                i = i - 1

        return res

    # Basically, you just need to convert either one or two characters into a number to get the answer.
    #
    # Complexity
    # Time complexity: O(n)
    # n is the length of the input string.
    #
    # Space complexity: O(1)
    # The dictionary roman always has a fixed size of seven key-value pairs,
    # regardless of the input size, so it uses constant space.
    def romanToInt2(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # loop through the string two characters at a time, shifting by one each time.
        # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
        # iterator is paired together, and then the second item in each passed iterator are paired together etc.
        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        return res + roman[s[-1]]


@pytest.mark.parametrize('s, k', [
    ("III", 3),
    ("IV", 4),
    ("VII", 7),
    ("IX", 9),
    ("XL", 40),
    ('XC', 90),
    ('CD', 400),
    ('CM', 900),
    ("XII", 12),
    ("XLIX", 49),
    ("LVIII", 58),
    ("CIV", 104),
    ("MCMXCIV", 1994),
])
def test_merge(s, k):
    solution = Solution()
    output = solution.romanToInt(s)

    assert output == k
    output = solution.romanToInt2(s)

    assert output == k
