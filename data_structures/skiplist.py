from random import randint

# https://w3.cs.jmu.edu/spragunr/CS240_F14/activities/skip_list/skip_list.shtml
# https://w3.cs.jmu.edu/lam2mo/cs240_2015_08/files/07-skip_lists.pdf
# https://w3.cs.jmu.edu/lam2mo/cs240_2015_08/pa03-skip_set.html


import random


def _generate_level():
    n = 0
    while randint(0, 1):
        n += 1
    return n


class SkipList:
    """ SortedSet ADT implemented using a skip list.
        Maintains elements in standard sorted order.
        Single-level nodes with next and below pointers.
        Uses sentinel values at the beginning of the skip list.
        Uses "coin tosses" to determine insertion heights.
    """

    class _Node:
        """ Represents a single-level node in a skip list,
            with two-way neighbor references
        """

        __slots__ = 'value', 'next', 'below'    # performance optimization

        def __init__(self, value):
            """ Create new node """
            self.value = value
            self.next = None
            self.below = None

        def __str__(self):
            return str(self.value)


    def __init__(self, iterable=[]):
        """ Create a new (empty) skip list """
        self._height = 0
        self._head = SkipList._Node(None)
        self._len = 0
        for elem in iterable:
            self.add(elem)

    def viz(self):
        """ Returns a formatted textual representation of the list """
        width = 5           # column width
        reps = []           # string representations of rows
        curs = []           # list of pointers for simultaneous traversal

        # start by adding all sentinels to "curs"
        cur = self._head
        while cur is not None:
            curs.append(cur)
            reps.append("")
            cur = cur.below

        # follow one "next" reference at a time on the lowest layer
        lowest = curs[-1]
        while lowest is not None:
            for i in range(len(curs)):
                # advance each reference if we've reached a node that matches
                # the node on the bottom of the list
                if curs[i] is not None and curs[i].value == lowest.value:
                    reps[i] += str(curs[i]).center(width)
                    curs[i] = curs[i].next
                else:
                    reps[i] += "".center(width)
            lowest = lowest.next
        return "\n".join(reps) + "\n------------------"

    def add(self, value):
        """ Insert a value into the skip list; doesn't allow duplicates """
        if value in self:
            return

        insertion_height = _generate_level()
        while self._height < insertion_height + 1:
            new_head = SkipList._Node(None)
            new_head.below = self._head
            new_head.next = None
            self._head = new_head
            self._height += 1

        level = self._height - 1
        current = self._head
        recently_added = None

        while current:
            while current.next and value > current.next.value:
                current = current.next
            if level < insertion_height:
                new_node = SkipList._Node(value)
                new_node.next = current.next
                current.next = new_node

                if recently_added:
                    recently_added.below = new_node
                recently_added = new_node

            current = current.below
            level -= 1

    def remove(self, value):
        """ Find and remove a value from the skip list.
            Raises a KeyError if the value is not in the list.
        """
        if value not in self:
            raise KeyError('No such value %s' % value)

        current = self._head
        while current:
            while current.next and value > current.next.value:
                current = current.next
            if current.next and current.next.value == value:
                current.next = current.next.next
            current = current.below

    def __contains__(self, value):
        """ Returns True if the given value is in the list; False otherwise """
        current = self._head

        while current:
            while current.next and value >= current.next.value:
                current = current.next
            if current.value == value:
                return True
            current = current.below
        return False

    def __iter__(self):
        """ Returns an iterator for the list """
        current = self._head
        while current.below:
            current = current.below
        current = current.next
        while current:
            yield current.value
            current = current.next


# s = SkipList()
# # print(s.viz())
# N = 100
# for i in range(N):
#     s.add(N-i)
#     # print(s.viz())

# s = SkipList([1, 2, 3])
# print(s.viz())
# s.remove(1)
# print(s.viz())

# print(s.viz())
# print(list(s))
# print([(i, i in s) for i in range(3)])

