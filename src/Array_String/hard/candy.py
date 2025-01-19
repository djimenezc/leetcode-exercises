"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""
from typing import List

import pytest


class Solution:
    # Intuition
    # Keep two peak values and subtract the lower peak from total.
    #
    # Time complexity: O(n)
    # 'n' is the number of elements in the 'ratings' list. This is because we are using a single loop to iterate
    # through the ratings, and within the loop, we perform constant time operations.
    #
    # Space complexity: O(1), which means it uses a constant amount of additional memory regardless of the size of
    # the 'ratings' list. The only variables that consume memory are 'n', 'total_candies', 'i', 'current_peak',
    # and 'current_valley', and these variables do not depend on the input size 'n'.
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # at least all children has one candy.
        total_candies = n
        i = 1

        while i < n:
            # we don't have to give a candy to the current i child because current i child has the same
            # rating with previous child. Just increment i and continue.
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            current_peak = 0
            # current i child has higher rating than i - 1 previous child. In this case, we need to give
            # candies to the current i child.
            while i < n and ratings[i] > ratings[i - 1]:
                current_peak += 1
                total_candies += current_peak
                i += 1

            if i == n:
                return total_candies

            current_valley = 0
            # current i child has lower rating than i - 1 previous child.
            while i < n and ratings[i] < ratings[i - 1]:
                current_valley += 1
                total_candies += current_valley
                i += 1

            # subtract minium of current_peak or current_valley from total_candies.
            # we add peaks twice as a peak and as a valley and we need only once
            total_candies -= min(current_peak, current_valley)

        return total_candies

    # Greedy approach
    # the goal is to meet the conditions using the least amount of candy.
    # Greedy Algorithm makes choices that seem optimal at the moment. For this problem, we use a two-pass greedy
    # approach to make sure each child gets the minimum number of candies that still satisfy the conditions.
    # Time and Space Complexity
    # Time Complexity: O(n), for the single pass through the ratings array.
    # Space Complexity: O(1), as we only use a few extra variables.
    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        # every child will receive at least one candy,
        candies = [1] * n

        # Forward Pass: Left to Right
        # For each child (except the first), we compare their rating with the one to the left
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Backward Pass: Right to Left
        # compare each child's rating with the child to their right.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


@pytest.mark.parametrize('ratings, expected_output', [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4)
])
def test_merge(ratings, expected_output):
    solution = Solution()
    output = solution.candy(ratings)

    assert output == expected_output
    output = solution.candy2(ratings)

    assert output == expected_output
