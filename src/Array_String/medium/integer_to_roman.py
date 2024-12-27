"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a
decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
 append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms
are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot
append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.



Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV


Constraints:

1 <= num <= 3999
"""
import math
from collections import OrderedDict

import pytest


class Solution:
    chars_with_value = OrderedDict([
        ('I', 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ])

    # pass with poor score
    def intToRoman(self, num: int) -> str:
        n = len(self.chars_with_value) - 1
        rest = num
        roman_str = ''

        while n > -1:
            digit = math.floor(rest / list(self.chars_with_value.values())[n])

            if n == 5 and math.floor(rest / 100) == 9:
                roman_str += 'CM'
                rest -= 900
            elif n == 5 and math.floor(rest / 100) == 4:
                roman_str += 'CD'
                rest -= 400
            elif n == 3 and math.floor(rest / 10) == 9:
                roman_str += 'XC'
                rest -= 90
            elif n == 3 and math.floor(rest / 10) == 4:
                roman_str += 'XL'
                rest -= 40
            elif n == 1 and rest == 9:
                roman_str += 'IX'
                rest -= 9
            elif n == 1 and rest == 4:
                roman_str += 'IV'
                rest -= 4
            elif digit > 0:
                roman_str += list(self.chars_with_value.keys())[n] * digit
                rest = rest % (list(self.chars_with_value.values())[n] * digit)

            if rest == 0:
                break
            n -= 1

        return roman_str

    # The Roman numeral system is based on subtractive notation and powers of 10. Therefore:
    #
    # Start with the largest Roman numeral that can fit into the number.
    # Use the subtractive notation for numbers like 4 (IV) or 9 (IX),
    # where one symbol is subtracted from another of greater value.
    # Repeat the process until the number becomes 0.
    def intToRoman2(self, num: int) -> str:
        roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = []
        for value, symbol in roman:
            while num >= value:
                result.append(symbol)
                num -= value
        return "".join(result)


@pytest.mark.parametrize('num, expected_output', [
    (94, 'XCIV'),
    (49, 'XLIX'),
    (999, 'CMXCIX'),
    (3999, 'MMMCMXCIX'),
    (1999, 'MCMXCIX'),
    (3900, 'MMMCM'),
    (1900, 'MCM'),
    (900, 'CM'),
    (400, 'CD'),
    (90, 'XC'),
    (40, 'XL'),
    (9, 'IX'),
    (4, 'IV'),
    (1100, 'MC'),
    (150, 'CL'),
    (10, 'X'),
    (3749, 'MMMDCCXLIX'),
    (58, 'LVIII'),
    (1994, 'MCMXCIV'),
])
def test_merge(num, expected_output):
    solution = Solution()
    output = solution.intToRoman(num)

    assert output == expected_output
    output = solution.intToRoman2(num)

    assert output == expected_output
