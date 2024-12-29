"""

"""

import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        return True


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    solution = Solution()
    output = solution.isSubsequence(s, t)

    assert output == expected_output
