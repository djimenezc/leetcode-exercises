"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import heapq
import random
from typing import List

import pytest


class Solution:

    # sorting
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        return nums[k - 1]

    # Min-Heap
    # Rather than sorting the entire array, this method utilizes a min-heap to maintain the k-th largest elements.
    # The heap allows us to efficiently compare each new element with the smallest of the k-th largest elements
    # seen so far. By the end of the iteration, the top of the heap will contain our desired k-th largest element.
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

    # QuickSelect Algorithm
    # Inspired by the QuickSort algorithm, QuickSelect is a divide-and-conquer technique. It partitions the array
    # around a pivot and recursively searches for the k-th largest element in the appropriate partition.
    # When the pivot is chosen randomly, the algorithm tends to have a linear average-case time complexity,
    # making it faster than the sorting approach for large datasets.
    def findKthLargest3(self, nums, k):
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            new_pivot_index = self.partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1
        nums[right], nums[stored_index] = nums[stored_index], nums[right]
        return stored_index


@pytest.mark.parametrize('nums, k, expected_output', [
    ([3, 2], 2, 2),
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
])
def test_merge(nums, k, expected_output):
    solution = Solution()
    output = solution.findKthLargest(nums, k)

    assert output == expected_output
    output = solution.findKthLargest2(nums, k)

    assert output == expected_output
    output = solution.findKthLargest3(nums, k)

    assert output == expected_output
