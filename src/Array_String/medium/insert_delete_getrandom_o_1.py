"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
from random import choice

import pytest


class RandomizedSet:
    def __init__(self):
        self.data_map = {}  # dictionary, aka map, aka hashtable, aka hashmap
        self.data = []  # list aka array

    def insert(self, val: int) -> bool:

        # the problem indicates we need to return False if the item
        # is already in the RandomizedSet---checking if it's in the
        # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val in self.data_map:
            return False

        # add the element to the dictionary. Setting the value as the
        # length of the list will accurately point to the index of the
        # new element. (len(some_list) is equal to the index of the last item +1)
        self.data_map[val] = len(self.data)

        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:

        # again, if the item is not in the data_map, return False.
        # we check the dictionary instead of the list due to lookup complexity
        if not val in self.data_map:
            return False

        # essentially, we're going to move the last element in the list
        # into the location of the element we want to remove.
        # this is a significantly more efficient operation than the obvious
        # solution of removing the item and shifting the values of every item
        # in the dicitionary to match their new position in the list
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        # change the last element in the list to now be the value of the element
        # we want to remove
        self.data[-1] = val

        # remove the last element in the list
        self.data.pop()

        # remove the element to be removed from the dictionary
        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        return choice(self.data)


@pytest.mark.parametrize('expected_output', [
    True,
])
def test_merge(expected_output):
    obj = RandomizedSet()

    assert obj.insert(1) == True
    assert obj.remove(2) == False
    assert obj.insert(2) == True
    random = obj.getRandom()
    assert random == 2 or random == 1
    assert obj.remove(1) == True
    assert obj.insert(2) == False
    random = obj.getRandom()
    assert random == 2 or random == 1
