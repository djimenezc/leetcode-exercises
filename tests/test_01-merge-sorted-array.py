import pytest

from src import merge_sorted_array


@pytest.mark.parametrize('nums1,m,nums2,n, expected', [
    # each element of this list will provide values for the
    # topics "value_A" and "value_B" of the test and will
    # generate a stand-alone test case.
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([3, 3, 4, 5, 0, 0, 0], 4, [1, 1, 1], 3, [1, 1, 1, 3, 3, 4, 5]),
    ([1, 1, 6, 10, 0, 0, 0, 0, 0], 4, [2, 3, 7, 11, 12], 5, [1, 1, 2, 3, 6, 7, 10, 11, 12]),
    ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3])

])
def test_merge(nums1, m, nums2, n, expected):
    solution = merge_sorted_array.Solution()
    solution.merge(nums1, m, nums2, n)

    assert nums1 == expected
