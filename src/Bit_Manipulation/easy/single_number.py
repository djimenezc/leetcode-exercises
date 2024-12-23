"""
Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?

"""

import pytest


class Solution:

    # faster
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        x_string = str(x)
        i = 0
        k = len(x_string) - 1

        while i < k:
            if x_string[i] != x_string[len(x_string) - 1 - i]:
                return False
            i += 1
            k -= 1

        return True

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x

    def isPalindrome3(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        # original = x

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10


@pytest.mark.parametrize('x, expected_output', [
    (121, True),
    (123321, True),
    (123421, False),
    (-121, False),
    (10, False),
])
def test_merge(x, expected_output):
    solution = Solution()
    output = solution.isPalindrome(x)

    assert output == expected_output
    output = solution.isPalindrome2(x)

    assert output == expected_output
    output = solution.isPalindrome3(x)

    assert output == expected_output
