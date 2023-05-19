from time import sleep, time
from threading import Thread, Lock
from collections import deque

class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = [] if children is None else children
    def add_child(self, obj):
        self.children.append(obj)
    def get_children(self):
        sleep(0.1)
        return self.children
    @staticmethod
    def sample():
        return Node(0, [
            Node(1, [
                Node(2),
                Node(3),
            ]),
            Node(4, [
                Node(5),
                Node(6),
                Node(7),
                Node(8, [
                    Node(9),
                    Node(10),
                ]),
            ]),
        ])

def sequential(node):
    out = [node.data]
    for child in node.get_children():
        out += sequential(child)
    return out

class MyQueue:
    def __init__(self):
        self.lock = Lock()
        self.xs = []
        self.running = 0
    def add(self, obj):
        with self.lock:
            self.xs.append(obj)
    def take(self):
        with self.lock:
            if len(self.xs) > 0:
                self.running += 1
                return self.xs.pop(0)
            else:
                return None
    def release(self):
        with self.lock:
            self.running -= 1
    def empty(self):
        with self.lock:
            return len(self.xs) == 0 and self.running == 0

def parallel(root):
    queue = MyQueue()
    queue.add(root)
    out = deque()
    def work():
        while not queue.empty():
            node = queue.take()
            if node is None:
                sleep(0.05)
                continue
            out.append(node.data)
            for child in node.get_children():
                queue.add(child)
            queue.release()
    threads = []
    for _ in range(10):
        t = Thread(target=work, args=())
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return list(out)

if __name__ == '__main__':
    node = Node.sample()

    t0 = time()
    print(sorted(sequential(node)))
    print(time() - t0)

    t0 = time()
    print(sorted(parallel(node)))
    print(time() - t0)
