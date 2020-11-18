#! usr/bin/env python3

from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity: int):
        """
        Initialize class variables

        Arguments:
            capacity {int} -- [capacity of cache]
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Retrieve item from provided key

        Arguments:
            key {int} -- [element]

        Returns:
            int -- [Return -1 if nonexistent]
        """
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: int, value: int) -> None:
        """
        Set the element if the key is not present in the cache.
        If the cache is at capacity remove the oldest item.

        Arguments:
            key {int} -- [description]
            element {int} -- [description]
        """
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def main():

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)  # returns 1
    our_cache.get(2)  # returns 2
    our_cache.get(9)  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # returns -1 because the cache reached it's capacity and 3 was the least
    # recently used entry
    our_cache.get(3)


if __name__ == "__main__":
    main()
