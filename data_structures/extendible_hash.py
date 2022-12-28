import random

class Page:
    def __init__(self, local_depth, page_size):
        self.page_size = page_size
        self.local_depth = local_depth
        self.items = []
    def full(self):
        return len(self.items) >= self.page_size
    def insert(self, key, value):
        if self.full(): raise RuntimeError('page is full')
        self.items.append((key, value))
        return True
    def update(self, key, value):
        for i, (k, old_value) in enumerate(self.items):
            if k == key:
                self.items[i] = (key, value)
                return True
        return False
    def get(self, key):
        for k, v in self.items:
            if k == key: return v
        return None
    def remove(self, key):
        N = len(self.items)
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items[i] = self.items[N-1]
                self.items.pop()
                return v
        return None

class ExtendibleHash:
    def __init__(self, page_size):
        self.page_size = page_size
        self.global_depth = 1
        self.directory = [Page(0, page_size), Page(0, page_size)]
        self.num_pages = 2
    def _index(self, key):
        mask = (1 << self.global_depth) - 1
        return hash(key) & mask
    def _get_page(self, key):
        return self.directory[self._index(key)]
    def insert(self, key, value):
        page = self._get_page(key)
        if page.get(key) != None:
            return page.update(key, value)
        if not page.full():
            print('insert')
            return page.insert(key, value)
        if page.local_depth < self.global_depth:
            self._redistribute(page, key)
            return self.insert(key, value)
        elif page.local_depth == self.global_depth:
            self._grow()
            self._redistribute(page, key)
            return self.insert(key, value)
        raise RuntimeError('impossible condition: local_depth > global_depth')
    def _grow(self):
        print('grow')
        self.directory *= 2
        self.global_depth += 1
    def _redistribute(self, page, key):
        print('redistribute')
        d = page.local_depth
        D = self.global_depth
        d1 = d+1
        p0 = Page(d1, self.page_size)
        p1 = Page(d1, self.page_size)
        def high_bit(key):
            mask = 1 << (D-1)
            return self._index(key) & mask
        for k, v in page.items:
            if high_bit(k) == 0: p0.insert(k, v)
            else: p1.insert(k, v)
        # there are 2**(D-d) directory entries that use this page
        mask = (1<<d)-1
        hb = 1<<(D-1)
        for index in range(self._index(key) & mask, len(self.directory), 1<<d):
            if index & hb == 0: self.directory[index] = p0
            else: self.directory[index] = p1
    def get(self, key):
        return self._get_page(key).get(key)
    def remove(self, key):
        return self._get_page(key).remove(key)

if __name__ == '__main__':
    PAGE_SIZE = 2
    h = ExtendibleHash(PAGE_SIZE)
    assert True == h.insert(1, 'a')
    assert True == h.insert(2, 'b')
    assert True == h.insert(3, 'c')
    assert True == h.insert(4, 'd')
    assert True == h.insert(5, 'e')
    assert True == h.insert(5, 'f')
    assert 'f' == h.get(5)
    assert None == h.get(0)
    assert 'f' == h.remove(5)
    assert None == h.get(5)
    assert 'a' == h.get(1)

    for i in range(100):
        print(i)
        h.insert(random.randint(0, 1000000), 'x')
