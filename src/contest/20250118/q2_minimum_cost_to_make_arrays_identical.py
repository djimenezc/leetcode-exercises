"""
You are given two integer arrays arr and brr of length n, and an integer k. You can perform the following operations on arr any number of times:

Split arr into any number of contiguous subarrays and rearrange these subarrays in any order. This operation has a fixed cost of k.
Choose any element in arr and add or subtract a positive integer x to it. The cost of this operation is x.

Return the minimum total cost to make arr equal to brr.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: arr = [-7,9,5], brr = [7,-2,-5], k = 2

Output: 13

Explanation:

Split arr into two contiguous subarrays: [-7] and [9, 5] and rearrange them as [9, 5, -7], with a cost of 2.
Subtract 2 from element arr[0]. The array becomes [7, 5, -7]. The cost of this operation is 2.
Subtract 7 from element arr[1]. The array becomes [7, -2, -7]. The cost of this operation is 7.
Add 2 to element arr[2]. The array becomes [7, -2, -5]. The cost of this operation is 2.
The total cost to make the arrays equal is 2 + 2 + 7 + 2 = 13.

Example 2:

Input: arr = [2,1], brr = [2,1], k = 0

Output: 0

Explanation:

Since the arrays are already equal, no operations are needed, and the total cost is 0.

 

Constraints:

1 <= arr.length == brr.length <= 105
0 <= k <= 2 * 1010
-105 <= arr[i] <= 105
-105 <= brr[i] <= 105©leetcode
"""
import math
from typing import List

import pytest


# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/description/
class Solution:
    def minCost1(self, arr: List[int], brr: List[int], k: int) -> int:
        res = 0
        n = len(arr)

        if n > 1:
            # rearrange k positions
            for i in range(k):
                element = arr.pop()
                arr.insert(0, element)

            # add the cost of moving k position in arr
            res += k

        # calculate differences per position and count the cost in res
        for i in range(n):
            res += abs(arr[i] - brr[i])

        return res

    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)

        min_cost = math.inf

        def calculate_min_cost(i):
            res = 0
            # calculate differences per position and count the cost in res
            for j in range(n):
                # res += min(abs(arr[i] - brr[i]), abs(arr[i] + brr[i]))
                res += abs(arr[j] - brr[j])
            # include the cost of traverse i position in arr
            return min(min_cost, res + i)

        if k == 0:
            return calculate_min_cost(0)
        else:
            if k > n:
                k = n % k

        # rearrange k positions
        for i in range(k + 1):
            min_cost = calculate_min_cost(i)
            element = arr.pop()
            arr.insert(0, element)

        return min_cost


@pytest.mark.parametrize('arr, brr, k, expected_output', [
    # ([3, 10], [4, 3], 15, 8),
    ([8, -1], [4, -6], 7, 9),
    ([-9], [9], 29, 18),
    ([1], [-1], 0, 2),
    ([-7, 9, 5], [7, -2, -5], 2, 13),
    ([2, 1], [2, 1], 0, 0)
])
def test_merge(arr, brr, k, expected_output):
    solution = Solution()
    output = solution.minCost(arr, brr, k)

    assert output == expected_output
