"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length

"""
import heapq
import random
from typing import List

import pytest


class Solution:

    # Intuition
    # The code aims to find the k smallest pairs from two sorted arrays, nums1 and nums2, based on their pair sums.
    # The approach used in the code is optimized to avoid inserting all pairs into the priority queue,
    # which would result in a time complexity of O(N
    # 2
    #  logN
    # 2
    #  ) and lead to a Time Limit Exceeded (TLE) error.
    #
    # To overcome this, the code follows a specific method to find the k smallest pairs efficiently.
    # It starts by inserting the pair sums of each element from nums1 and the first element of nums2 into
    # a priority queue. Since both arrays are sorted, the pair sums will be in increasing order.
    #
    # By utilizing a priority queue, the smallest sum pair is always accessible at the top. The code then pops
    # the smallest pair from the priority queue and adds it to the result vector. Next, it inserts the next pair,
    # which consists of the same element from nums1 but the next element from nums2.
    #
    # The code repeats this process, gradually inserting pairs with increasing elements from nums2, until it has
    # added k pairs to the result vector or the priority queue becomes empty (i.e., all pairs have been explored).
    # This ensures that only the k smallest pairs are considered.
    #
    # Finally, the code returns the resulting vector containing the k smallest pairs.
    #
    # Overall, the approach intelligently uses the priority queue to avoid unnecessary computations, allowing for an optimized solution with a time complexity of O(KlogN), where N represents the size of nums1 and K is the given parameter for the number of smallest pairs to find.
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        resV = []  # Result list to store the pairs
        pq = []  # Priority queue to store pairs with smallest sums, sorted by the sum

        # Push the initial pairs into the priority queue
        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])  # The sum and the index of the second element in nums2

        # Pop the k smallest pairs from the priority queue
        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]  # Get the smallest sum and the index of the second element in nums2

            resV.append([s - nums2[pos], nums2[pos]])  # Add the pair to the result list

            # If there are more elements in nums2, push the next pair into the priority queue
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  # Decrement k

        return resV  # Return the k smallest pairs


@pytest.mark.parametrize('nums1, nums2, k, expected_output', [
    ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
    ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]])
])
def test_merge(nums1, nums2, k, expected_output):
    solution = Solution()
    output = solution.kSmallestPairs(nums1, nums2, k)

    assert output == expected_output
