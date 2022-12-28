def mid(l, r): return (l+r)//2
def left(v): return v+1
def right(v, l, r): return v+2*(mid(l, r)-l+1)
class SegmentTreeSum:
    ROOT = 1
    def __init__(self, vs):
        self.n = len(vs)
        self.xs = [0]*2*self.n
        self._build(vs, self.ROOT, 0, self.n-1)
    def _build(self, vs, v, tl, tr):
        # tl, tr -- the range v is responsible for
        if tl == tr: self.xs[v] = vs[tl]
        else:
            lchild, tm, rchild = left(v), mid(tl, tr), right(v, tl, tr)
            self._build(vs, lchild, tl, tm)
            self._build(vs, rchild, tm+1, tr)
            self.xs[v] = self.xs[lchild] + self.xs[rchild]
    def _query(self, v, tl, tr, l, r):
        # tl, tr -- the range v is response for
        # l, r -- query boundary, inclusive
        if (l > r): return 0
        if ((l == tl) and (r == tr)): return self.xs[v]
        lchild, tm, rchild = left(v), mid(tl, tr), right(v, tl, tr)
        a = self._query(lchild, tl, tm, l, min(r, tm))
        b = self._query(rchild, tm+1, tr, max(l, tm+1), r)
        return a+b
    def query(self, l, r):
        return self._query(self.ROOT, 0, self.n-1, l, r)
    def _update(self, v, tl, tr, pos, val):
        if tl == tr: self.xs[v] = val
        else:
            lchild, tm, rchild = left(v), mid(tl, tr), right(v, tl, tr)
            if pos <= tm: self._update(lchild, tl, tm, pos, val)
            else: self._update(rchild, tm+1, tr, pos, val)
            self.xs[v] = self.xs[lchild] + self.xs[rchild]
    def update(self, pos, val):
        return self._update(self.ROOT, 0, self.n-1, pos, val)

def test(tree, vs, l, r):
    expected = sum(vs[l:r+1])
    actual = tree.query(l, r)
    assert expected == actual, 'sum(%s,%s) != %s, actual=%s' % (l, r, expected, actual)

if __name__ == '__main__':
    vs = [1,1,1,1,1]
    t = SegmentTreeSum(vs)
    test(t, vs, 0, 0)
    test(t, vs, 0, 1)
    test(t, vs, 0, 2)
    test(t, vs, 0, 3)
    test(t, vs, 1, 3)
    test(t, vs, 2, 3)
    test(t, vs, 3, 3)
    t.update(1, 10)
    vs[1] = 10
    test(t, vs, 0, 1)
    test(t, vs, 1, 2)
