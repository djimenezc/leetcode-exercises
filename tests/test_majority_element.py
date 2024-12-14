import pytest

from src import majority_element


@pytest.mark.parametrize('nums, k', [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2)
])
def test_merge(nums, k, ):
    solution = majority_element.Solution()
    output = solution.majorityElement(nums)

    assert k == output
