import pytest

from src import best_time_to_buy_and_sell_stock


@pytest.mark.parametrize('nums, k', [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
])
def test_merge(nums, k):
    solution = best_time_to_buy_and_sell_stock.Solution()
    output = solution.maxProfit(nums)

    assert k == output
