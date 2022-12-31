from dataclasses import dataclass, field
from typing import Optional, List, Tuple, Callable
from math import floor

@dataclass
class Endpoint:
    v: float
    ix: int

@dataclass
class Node:
    b: int
    e: int
    key: int = 0
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    aux: List[Tuple[int, int]] = field(default_factory=list)
    _query: Optional[Callable[[float], List[Tuple[float, float]]]] = None
    __repr__ = lambda self: f'Node({self.b} {self.e} {self.aux})'

    @staticmethod
    def build(intervals: List[Tuple[float, float]]) -> 'Node':
        def _build(s: int, t: int) -> 'Node':
            v = Node(s, t)
            print(f'built {v}')
            if s+1 == t: return v
            m = floor((v.b+v.e)/2)
            v.key = m
            v.left = _build(s, m)
            v.right = _build(m, t)
            return v

        eps = []
        for ix, (start, end) in enumerate(intervals):
            eps.append(Endpoint(start, ix))
            eps.append(Endpoint(end, ix))
        eps = sorted(eps, key=lambda e: e.v)
        root = _build(0, len(eps)-1)

        def _insert(v, b: int, e: int) -> None:
            #if v is None: return
            if (b <= v.b) and (v.e <= e):
                interval = (eps[b].v, eps[e].v)
                v.aux.append(interval)
                #print(f'inserted {interval} into {v}')
                return
            if b < v.key: _insert(v.left, b, e)
            if v.key < e: _insert(v.right, b, e)

        def _tree(v, indent=0) -> str:
            n = 3
            out = '\n'
            if v is None:
                out += ' '*indent + '<nil>'
                return out
            out += ' '*indent + str(v)
            out += '\n' + ' '*indent + 'L:' + _tree(v.left, indent+n)
            out += '\n' + ' '*indent + 'R:' + _tree(v.right, indent+n)
            return out

        print(f'intervals: {intervals}')
        print(f'eps: {eps}')
        seen = dict()
        for i, ep in enumerate(eps):
            if ep.ix not in seen: seen[ep.ix] = i # remember first encounter
            else: _insert(root, seen[ep.ix], i)

        def _query(v, q: float) -> List[Tuple[float, float]]:
            out = set()
            if v == None:
                print('v is None')
                return []
            if eps[v.b].v <= q <= eps[v.e].v:
                print(f'fully inside q={q} in <{v}>')
                out.update(v.aux)
            if q <= eps[v.key].v: out.update(_query(v.left, q))
            if q >= eps[v.key].v: out.update(_query(v.right, q))
            return out
        root._query = lambda q: _query(root, q)
        root.tree = lambda: _tree(root)
        return root

    def query(self, q: float) -> List[Tuple[float, float]]:
        return self._query(q)

def test(node, q):
    print('')
    print(f'query {q}: {node.query(q)}')


if __name__ == '__main__':
    intervals = [(1,3), (2,4), (0,5)]
    #intervals = [(1,3), (0,5)]
    # intervals = [
    #     (0,5),
    #     (1,3),
    # ]
    t = Node.build(intervals)
    print(t.tree())
    print('')
    print('intervals:', intervals)
    test(t, -1)
    test(t, 0)
    test(t, 1)
    test(t, 2)
    test(t, 3)
    test(t, 4)
    test(t, 5)
    test(t, 6)
    test(t, 9)
