import pytest

from src import remove_duplicates_from_sorted_array


@pytest.mark.parametrize('nums, k, nums_expect', [
    ([], 0, []),
    ([1, 1, 2], 2, [1, 2, '_']),
    ([0, 0, 1, 1, 1], 2, [0, 1, '_', '_', '_']),
    ([0, 0, 1, 1, 1, 2], 3, [0, 1, 2, '_', '_', '_']),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']),

])
def test_merge(nums, k, nums_expect):
    solution = remove_duplicates_from_sorted_array.Solution()
    k = solution.removeDuplicates(nums)

    assert k == k
    for i in range(0, k):
        assert nums[i] == nums_expect[i];
