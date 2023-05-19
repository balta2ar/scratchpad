from graphviz import Digraph
from math import log2, ceil

def hue_to_rgb(p, q, t):
    if t < 0: t += 1
    if t > 1: t -= 1
    if t < 1/6: return p + (q - p) * 6 * t
    if t < 1/2: return q
    if t < 2/3: return p + (q - p) * (2/3 - t) * 6
    return p

def hsl_to_rgb(h, s, l):
    h /= 360
    q = l * (1 + s) if l < 0.5 else l + s - l * s
    p = 2 * l - q
    r = hue_to_rgb(p, q, h + 1/3)
    g = hue_to_rgb(p, q, h)
    b = hue_to_rgb(p, q, h - 1/3)
    return r, g, b

def rgb_to_hex(r, g, b):
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def hue(h):
    return rgb_to_hex(*hsl_to_rgb(h, 0.5, 0.5))

def dfs(node, val):
    if node.val == val: return node
    for child in node.children:
        found = dfs(child, val)
        if found: return found
    return None

def bfs(node, val):
    q = [node]
    while q:
        node = q.pop(0)
        if node.val == val: return node
        q.extend(node.children)
    return None

class Node:
    def __init__(self, val, children=None, parent=None):
        self.id = str(val)
        self.val = val
        self.parent = parent
        self.depth = -1
        self.size = -1
        self.index = -1
        self.attrs = {}
        self._index = []
        self.children = children if children else []
        for child in self.children: child.under(self)
    def by_index(self, index): return self._index[index]
    def process(self, root):
        index = Counter()
        def dfs(node, depth):
            node.depth = depth
            node.size = 1
            node.index = index.inc()
            root._index.append(node)
            for child in node.children:
                dfs(child, depth + 1)
                node.size += child.size
        dfs(root, 0)
    def adopt(self, child): self.children.append(child)
    def under(self, parent): self.parent = parent
    def __repr__(self): return f'{self.val} (d{self.depth} s{self.size})'
    def render(self):
        dot = Digraph(format=FORMAT,
                      node_attr={'shape': 'plaintext'},
                      edge_attr={'arrowsize': '0.5'},
        )
        self.render_(dot)
        dot.render('binary_lifting', view=True)
    def render_(self, dot):
        dot.node(self.id, str(self), **self.attrs)
        for child in self.children:
            dot.edge(self.id, child.id)
            child.render_(dot)
    def find(self, val):
        return dfs(self, val)

def example():
    g = Node(1, [
        Node(2, [
            Node(4), Node(5, [
                Node(8), Node(9, [
                    Node(10), Node(11, [
                        Node(18), Node(19, [
                            Node(22), Node(23), Node(24)
                        ]), Node(20), Node(21)
                    ])
                ])
            ])
        ]),
        Node(3, [
            Node(6, [
                Node(12), Node(13, [
                    Node(14), Node(15, [
                        Node(16), Node(17)
                    ])
                ])
            ]), Node(7)
        ])
    ])
    g.process(g)
    return g

dummy = Node(-1)

def climb(node):
    path = [node]
    while node.parent:
        node = node.parent
        path.append(node)
    return path

class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        count, self.count = self.count, self.count + 1
        return count

class Lifting:
    def __init__(self, root):
        self.root = root
        self.up = []
        self.process(root)
    @property
    def l(self):
        n = self.root.size
        return ceil(log2(n))
    def process(self, root):
        timer = Counter()
        tin, tout = {}, {}
        n = root.size
        up = []
        for _ in range(n): up.append([None] * (self.l+1))
        def dfs(node, parent):
            print('visit', node.index)
            tin[node.index] = timer.inc()
            up[node.index][0] = parent.index
            for i in range(1, self.l+1): up[node.index][i] = up[up[node.index][i-1]][i-1]
            for child in node.children:
                if child != parent: dfs(child, node)
            tout[node.index] = timer.inc()
        dfs(root, root)
        self.up = up
        self.tin = tin
        self.tout = tout
        print(tin)
        print(tout)
    def is_ancestor(self, a, b):
        ai, bi = a.index, b.index
        return self.tin[ai] <= self.tin[bi] and self.tout[ai] >= self.tout[bi]
    def lca(self, a, b):
        if self.is_ancestor(a, b): return a
        if self.is_ancestor(b, a): return b
        for i in range(self.l, -1, -1):
            print('i', i, 'index', a.index)
            index = self.up[a.index][i]
            p = self.root.by_index(index)
            if not self.is_ancestor(p, b): a = p
        index = self.up[a.index][0]
        return self.root.by_index(index)
    def lca_slow(self, a, b):
        path_a = climb(a)[::-1]
        path_b = climb(b)[::-1]
        for i in range(len(path_a)):
            if path_a[i] != path_b[i]:
                return path_a[i - 1]
        return path_a[-1]
    def render(self):
        dot = Digraph(format=FORMAT,
                      node_attr={'shape': 'plaintext'},
                      edge_attr={'arrowsize': '0.5'},
                      engine='dot',
        )
        self.root.render_(dot)
        for i in range(len(self.up)):
            angle = i/len(self.up)*360.0 + i%2*180.0
            color = hue(angle)
            for j in range(self.l+1):
                p = self.up[i][j]
                if p != 0:
                    a = self.root.by_index(i)
                    b = self.root.by_index(p)
                    dot.edge(a.id, b.id, style='dashed', color=color)
        dot.render('binary_lifting', view=True)


FORMAT = 'svg'

if __name__ == '__main__':
    g = example()
    l = Lifting(g)
    #p = l.lca_slow(g.find(10), g.find(17))
    a = g.find(8)
    b = g.find(20)
    p = l.lca(a, b)
    a.attrs['fontcolor'] = 'red'
    b.attrs['fontcolor'] = 'red'
    p.attrs['fontcolor'] = 'green'
    l.render()
