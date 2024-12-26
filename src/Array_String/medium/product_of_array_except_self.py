"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for
space complexity analysis.)
"""
from functools import reduce
from typing import List

import pytest


class Solution:
    # Time Limit Exceeded
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums_len = len(nums)
        output = [0] * len(nums)

        for i in range(len(nums)):
            output[i] = reduce(lambda x, y: x * y, nums[0:i] + nums[i + 1:nums_len])

        return output

    # Initialize:
    # result array with size ( n ), all elements set to 1.
    # A variable suffix initialized to 1.
    # First pass (Left-to-Right):
    # Compute prefix products and store them in result.
    # Second pass (Right-to-Left):
    # Update the result array by multiplying the current value with suffix.
    # Update suffix as ( \text{suffix} \times \text{nums}[i] ).
    # Return the updated result array.
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # First pass: Calculate prefix products
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Second pass: Calculate suffix products on the fly
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer


@pytest.mark.parametrize('nums, expected_output', [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
])
def test_merge(nums, expected_output):
    solution = Solution()
    output = solution.productExceptSelf(nums)

    assert output == expected_output
    output = solution.productExceptSelf2(nums)

    assert output == expected_output
    output = solution.productExceptSelf3(nums)

    assert output == expected_output
