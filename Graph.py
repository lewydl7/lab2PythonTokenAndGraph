import numpy


class Graph:

    lista = {}
    def add_point(self, a):
        self.lista[a] = []

    def add_edge(self, a, b):
        self.lista[a].append(b)
        self.lista[b].append(a)

    def delete_point(self, a):
        for i in self.lista:
            self.lista[i].remove(a)
        self.lista.pop(a)

    def delete_edge(self, a, b):
        self.lista[a].remove(b)
        self.lista[b].remove(a)

    def neighbors_edge(self, a):
        return self.lista[a]

    def dfs(self, a=None):
        visited = set()
        bfsResult = []

        def visit(self, v):
            if v not in visited:
                visited.add(v)
                bfsResult.append(v)
                for x in self.lista_sasiedztw[v]:
                    visit(self, x)

        if a == None:
            a = self.lista[1]
        visit(self, a)
        print(bfsResult)

    def bfs(self, a=None):
        visited = []
        queue = []

        visited.append(a)
        queue.append(a)

        while queue:
            s = queue.pop(0)

            for v in self.lista[s]:
                if v not in visited:
                    visited.append(v)
                    queue.append(v)
        return visited

ab = Graph()
ab.add_point(1)
ab.add_point(2)
ab.add_point(3)
ab.add_point(4)
ab.add_edge(4, 3)
ab.add_edge(3, 2)
ab.add_edge(2, 1)
print(ab.neighbors_edge(2))