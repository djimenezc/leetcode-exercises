"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104


Follow up: Could you write a solution that works in logarithmic time complexity?

We have to find how many zeroes are there at the end of this number N. To deduce this, we have to know how trailing
zeros are formed in the first place. A trailing zero is formed when a multiple of 5 is multiplied with a multiple of 2.
Now, all we have to do is count the number of 5’s and 2’s in the multiplication.

Number of 5’s = 100/5 + 100/25 + 100/125 + … = 24 (Integer values only)


"""

import pytest


class Solution:
    def trailingZeroes(self, n: int) -> int:
        countOfZero = 0
        powerOfFive = 5

        while n // powerOfFive:
            countOfZero += n // powerOfFive
            powerOfFive *= 5

        # INSTEAD OF INCREASING THE POWER OF FIVE LIKE
        # 5 25 125 .....
        # YOU CAN SIPMLY DIVIDE THE n BY 5 IN EACH ITERATION
        # THUS AVOIDING THE INTEGER OVERFLOW

        # while n//powerOfFive:
        #    countOfZero+=n//powerOfFive
        #    n/=powerOfFive

        # YOU CAN USE THIS CODE SNIPPET INSTEAD OF THE ABOVE USED CODE

        return countOfZero


@pytest.mark.parametrize('n, expected_output', [
    (152, 37),
    (3, 0),
    (5, 1),
    (0, 0)
])
def test_merge(n, expected_output):
    solution = Solution()
    output = solution.trailingZeroes(n)

    assert output == expected_output
