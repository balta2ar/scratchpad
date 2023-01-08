from bisect import bisect_left
from random import randint, seed
from time import time

def even(xs): return [x for i, x in enumerate(xs) if i % 2 == 1]

class FractionalCascading:
    def __init__(self, ls):
        self.ls = ls
        self.ms = []
        self.pointers = []
        self.build(ls)
    def build(self, ls):
        ms = [[]] * len(ls)
        pointers = [[]] * len(ls)
        for i in range(len(ls)-1, -1, -1):
            extra = even(ms[i+1]) if i < len(ls)-1 else []
            ms[i] = sorted(ls[i] + extra)
        for k in range(len(ls)):
            ms[k].insert(0, float('-inf'))
            ms[k].append(float('inf'))
        for i in range(len(ls)):
            ps = []
            for x in ms[i]:
                right = bisect_left(ls[i], x)
                down = bisect_left(ms[i+1], x) if i < len(ls)-1 else 0
                ps.append((right, down))
            pointers[i] = ps
        self.ms = ms
        self.pointers = pointers
        from pprint import pprint
        pprint(ms)
    def query(self, q):
        out = []
        ix = bisect_left(self.ms[0], q)
        right, down = self.pointers[0][ix]
        v = self.ms[0][ix]
        print(f'k=0 q={q} v={v} right={right} down={down}')
        out.append(right)
        for k in range(1, len(self.ms)):
            if q <= self.ms[k][down-1]:
                right, down = self.pointers[k][down-1]
            else:
                right, down = self.pointers[k][down]
            print(f'k={k} q={q} v={v} right={right} down={down}')
            out.append(right)
        return out

class Naive:
    def __init__(self, ls):
        self.ls = ls
    def query(self, x):
        out = []
        for _, ls in enumerate(self.ls):
            ix = bisect_left(ls, x)
            out.append(ix)
        return out

def test(fc, naive, q):
    res_naive = naive.query(q)
    res_fc = fc.query(q)
    assert res_naive == res_fc, f'query: "{q}" => {res_naive} vs {res_fc}'

def test_n(impl, nruns):
    times = []
    for _ in range(nruns):
        q = randint(0, 1000)
        t0 = time()
        impl.query(q)
        times.append((time() - t0)*1000*1000)
    times.sort()
    return times[len(times)//2]

def make_catalog(n, k):
    """
    n: number of items in a single list
    k: number of lists
    """
    max_value = 1000
    catalog = []
    for _ in range(k):
        catalog.append(sorted([randint(0, max_value) for _ in range(n)]))
    return catalog, max_value

def test_simple():
    catalog = [
        [1, 4, 9],
        [2, 3, 7, 10],
        [5, 6, 8, 9, 10, 11]
    ]
    naive = Naive(catalog)
    fc = FractionalCascading(catalog)
    test(fc, naive, 4)
    test(fc, naive, 3)
    test(fc, naive, 9)
    test(fc, naive, 0)
    test(fc, naive, 100)

def test_simple2():
    catalog = [
        [1, 3, 7],
        [2, 5, 9, 13, 25],
        [7, 9, 12, 15],
        [0, 4, 6, 10, 11],
    ]
    naive = Naive(catalog)
    fc = FractionalCascading(catalog)
    test(fc, naive, 11)

def test_random():
    seed(time())
    for _ in range(100):
        catalog, max_value = make_catalog(1000, 100)
        naive = Naive(catalog)
        fc = FractionalCascading(catalog)
        for _ in range(100):
            q = randint(0, max_value)
            test(fc, naive, q)

def test_bench():
    # python ./fractional_cascading.py > fractional_cascading.tsv
    seed(time())
    k = 10
    for i in range(1, 20):
        n = 2**i
        catalog, max_value = make_catalog(n, k)
        naive = Naive(catalog)
        fc = FractionalCascading(catalog)
        times_naive = test_n(naive, 10)
        times_fc = test_n(fc, 10)
        print(f'{n}\tnaive\t{times_naive:.0f}')
        print(f'{n}\tfc\t{times_fc:.0f}')

def bench_show(filename):
    # python -c 'from fractional_cascading import bench_show; bench_show("fractional_cascading.tsv")'
    import pandas as pd
    import plotly.express as px
    df = pd.read_table(filename, names=['n','impl','microseconds'],
                       dtype={'n':'string','impl':'string','microseconds':'int'},
                       parse_dates=['n'])
    fig = px.line(df, x='n', y='microseconds', hover_name='impl', color='impl', log_x=True)
    fig.update_layout({
        'plot_bgcolor': 'rgb(255, 255, 255)',
        'paper_bgcolor': 'rgb(255, 255, 255)',
    })
    fig.show()

if __name__ == '__main__':
    # test_simple()
    test_simple2()
    # test_random()
    # test_bench()
