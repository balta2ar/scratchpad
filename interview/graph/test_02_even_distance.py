"""
http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
http://practice.geeksforgeeks.org/problems/nodes-at-even-distance/0

Applications:
    http://www.geeksforgeeks.org/?p=11644

Given a connected acyclic graph with N nodes and N-1 edges, find out the pair of nodes that are at even distance from each other.

Input:

The first line of input contains an integer T denoting the number of test cases.

First line of each test case contains a single integer N denoting the number of nodes in graph.

Second line of each test case contains N-1 pair of nodes xi , yi denoting that there is an edges between them.


Output:

For each test case output a single integer denoting the pair of nodes which are at even distance.


Constraints:

1<=T<=10

1<=N<=10000

1<=xi,yi<=N

Example

Input

1

3

1 2 2 3

Output

1

Explanation:

Only such pair is (1,3) where distance b/w them is 2


SOLUTION:

The idea is to find even and odd distances from some root node. Next, given
e = number of even distances, o = number of odd distances, the solution is

    answer = e * (e-1) / 2 + o * (o-1) / 2.

Why? We split all vertices into two sets: those that have even distances, and
those that have odd distances. Now we need to find all possible pairs in both
of these two sets. Notice that the order of vertices in a pair is not important,
i.e. (1,3) == (3,1). To find that number, we use binonial coefficient C(n, k),
in our case n={e,o}, k=2, i.e.:

    C(e,2) + C(o,2)
"""

from sys import stdin
from io import StringIO
from queue import deque
from itertools import zip_longest
import queue


TEST1 = """3
5
1 2 2 3 3 4 4 5
5
1 2 2 3 2 5 4 5
6
1 2 1 3 1 4 1 5 1 6"""

TEST1_OUTPUT = """4
4
10"""


class Graph:
    def __init__(self, n):
        self.n = n
        self.num_even = 0
        self.num_odd = 0
        self._edges = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self._edges[a].append(b)
        self._edges[b].append(a)

    def run_dfs(self, start):
        front = deque()
        front.append(start)
        # visited = [False] * self.n
        distances = [-1] * self.n
        distances[start] = 0
        self.num_even = 0
        self.num_odd = 0

        while front:
            vertice = front.popleft()
            for neighbor in self._edges[vertice]:
                if distances[neighbor] > 0:
                    continue

                distances[neighbor] = distances[vertice] + 1
                if distances[neighbor] % 2 == 0:
                    self.num_even += 1
                else:
                    self.num_odd += 1
                front.appendleft(neighbor)

        # print('edges', self._edges)
        # print('dis', distances, start, self.n)
        # print(self.num_even, self.num_odd)

        result = self.num_even * (self.num_even - 1) / 2 + \
            self.num_odd * (self.num_odd - 1) / 2
        return int(result)


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def read_input(input):
    num_tests = int(input.readline().strip())
    # print('num-tests', num_tests)

    for _ in range(num_tests):
        n = int(input.readline().strip())
        # print('N', n)
        graph = Graph(n)
        line = list(map(int, input.readline().strip().split()))
        # print('line', line)
        grouped = grouper(line, 2)
        # print('grouped', list(grouped))
        for a, b in grouped:
            graph.add_edge(a-1, b-1)
        yield graph


def solve_even_distance(input):
    result = []
    for graph in read_input(input):
        result.append(str(graph.run_dfs(0)))
    return '\n'.join(result)


def test_even_distance():
    output = solve_even_distance(StringIO(TEST1))
    assert TEST1_OUTPUT.strip().split() == output.strip().split()


if __name__ == '__main__':
    print(solve_even_distance(stdin))