import pytest

from src import remove_element


@pytest.mark.parametrize('nums, val, expected, nums_expect', [
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3]),

])
def test_merge(nums, val, expected, nums_expect):
    solution = remove_element.Solution()
    k = solution.removeElement(nums, val)

    assert k == expected
    # nums[:k].sort()
    # assert nums[:k] == nums_expect
