from skiplist import SkipList

from unittest import TestCase
import random


class TestSkipList(TestCase):
    def test_smoke(self):
        skip = SkipList()
        skip.add(3)
        skip.add(2)
        skip.add(1)
        # print(skip.viz())
        self.assertTrue(1 in skip)
        self.assertTrue(2 in skip)
        self.assertTrue(3 in skip)
        self.assertFalse(0 in skip)
        self.assertFalse(4 in skip)
        self.assertFalse(10 in skip)

    def test_add(self):
        items = list(range(100))
        random.shuffle(items)
        skip = SkipList()
        std = set()
        for i, x in enumerate(items):
            skip.add(x)
            std.add(x)
            self.assertEqual(x in skip, x in std)

            for j in range(i):
                y = items[j]
                self.assertEqual(y in skip, y in std)

    def test_remove(self):
        skip = SkipList([1, 2, 3])
        with self.assertRaises(KeyError):
            skip.remove(100)

        x = 1
        skip.remove(x)
        self.assertNotIn(x, skip)

        items = list(range(100))
        random.shuffle(items)
        skip = SkipList()
        std = set()

        for i, x in enumerate(items):
            skip.add(x)
            std.add(x)

        self.assertEqual(sorted(list(skip)), sorted(list(std)))

        for i, x in enumerate(items):
            skip.remove(x)
            std.remove(x)
            self.assertNotIn(x, skip)
            self.assertEqual(sorted(list(skip)), sorted(list(std)))
