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
    # Greedy approach
    # the goal is to meet the conditions using the least amount of candy.
    # Greedy Algorithm makes choices that seem optimal at the moment. For this problem, we use a two-pass greedy
    # approach to make sure each child gets the minimum number of candies that still satisfy the conditions.
    # Time and Space Complexity
    # Time Complexity: O(n), for the single pass through the ratings array.
    # Space Complexity: O(1), as we only use a few extra variables.
    def candy(self, ratings: List[int]) -> int:
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
