from typing import List, Optional


class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self._mapping = dict()
        self._order = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        value = self._mapping.get(key, -1)
        if value != -1:
            del self._order[key]
            self._order[key] = None
        return value

    def put(self, key: int, value: int) -> None:
        if key in self._mapping:
            del self._order[key]
            self._order[key] = None
            self._mapping[key] = value
            return

        # new key
        if len(self._mapping)+1 > self._capacity:
            popped_key, _value = self._order.popitem(last=False)
            del self._mapping[popped_key]

        self._order[key] = None
        self._mapping[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    # m, n = input_
    result = None #Solution().(m, n)
    assert_eq(result, output)


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert_eq(cache.get(1), 1)
    cache.put(3, 3)
    assert_eq(cache.get(2), -1)
    cache.put(4, 4)
    assert_eq(cache.get(1), -1)
    assert_eq(cache.get(3), 3)
    assert_eq(cache.get(4), 4)
