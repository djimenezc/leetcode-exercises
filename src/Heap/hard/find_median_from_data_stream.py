"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer
will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
from heapq import heappush, heappushpop, heappop

import pytest


# I keep two heaps (or priority queues):
#
# Max-heap small has the smaller half of the numbers.
# Min-heap large has the larger half of the numbers.
# This gives me direct access to the one or two middle values (they're the tops of the heaps),
# so getting the median takes O(1) time. And adding a number takes O(log n) time.
# simply negate the numbers in the heap in which I want the reverse of the default order
# Using larger integer types also prevents an overflow error when taking the mean of the two middle numbers.
# I think almost all solutions posted previously have that bug.
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        # Odd
        if len(self.large) > len(self.small):
            return float(self.large[0])
        # Even
        return (self.large[0] - self.small[0]) / 2.0



@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):

    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)

    assert obj.findMedian() == 1.5
    obj.addNum(2)
    assert obj.findMedian() == 2.0
