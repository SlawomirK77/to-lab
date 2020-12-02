from collections import defaultdict
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        """Returns Boolean whether at end of collection or not"""

    @staticmethod
    @abstractmethod
    def next():
        """Return the object in collection"""


class Graph(Iterator):
    def __init__(self):
        self.graph = defaultdict(list)
        self.index = 0
        self.maximum: int

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.maximum = len(self.graph)

    def bfs(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def next(self):
        if self.index < self.maximum:
            x = self.index
            self.index += 1
            return self.graph[x]
        else:
            raise Exception("AtEndOfIteratorException", "At End Of Iterator")

    def has_next(self):
        return self.index < self.maximum


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(3, 4)
    g.add_edge(4, 3)
    g.add_edge(4, 5)
    g.add_edge(5, 4)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(3, 3)


    g.bfs(3)

    print("\n")
    print(g.graph)
    for i in range(6):
        print(g.graph[i])

    while g.has_next():
        print(g.next())
