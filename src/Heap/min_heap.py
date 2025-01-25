# Import the heap functions from python library
from heapq import heappush, heappop

import pytest


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i) -> int:
        return int((i - 1) / 2)

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

        # Decrease value of key at index 'i' to new_val

    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i: int, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)], self.heap[i])

    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


@pytest.mark.parametrize('nums, target, expected_output', [
    ([1, 3, 5, 6], 5, 2),
])
def test_merge(nums, target, expected_output):

    # Driver pgoratm to test above function
    heap_obj = MinHeap()
    heap_obj.insertKey(3)
    heap_obj.insertKey(2)
    heap_obj.deleteKey(1)
    heap_obj.insertKey(15)
    heap_obj.insertKey(5)
    heap_obj.insertKey(4)
    heap_obj.insertKey(45)

    min_val = heap_obj.extractMin()
    assert min_val == 2
    print(min_val)

    min_val = heap_obj.getMin()
    assert min_val == 4
    print(min_val)

    heap_obj.decreaseKey(2, 1)

    min_val = heap_obj.getMin()
    assert min_val == 1
    print(min_val)
