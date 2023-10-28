class Graph():
    def __init__(self, V=[], directed = True):
        self.vertices = {}
        for x in V:
            self.vertices[x] = []
        self.directed = directed

    def __str__(self):
        s = 'Vertices: {}\nEdges:\n'.format(list(self.vertices.keys()))
        for v in self.vertices:
            for x in self.vertices[v]:
                s += '({}->{}, weight:{}) '.format(v, x[0], x[1])
            if (len(self.vertices[v]) > 0):
                s += '\n'
        return s

    def Vertices(self):
        return self.vertices.keys()

    def Edges(self):
        edges = []
        for v in self.vertices:
            for x in self.vertices[v]:
                edges.append((v, x[0], x[1]))
        return edges

    def IncidentEdges(self, v):
        return self.vertices[v]

    def AddVertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = []
        return self

    def AddEdge(self, x, y, weight = 1):
        self.vertices[x].append((y, weight))
        if not self.directed:
            self.vertices[y].append((x, weight))
        return self

    def AddEdges(self, edges):
        for e in edges:
            if len(e) > 2:
                self.AddEdge(e[0], e[1], e[2])
            else:
                self.AddEdge(e[0], e[1])

    def RemoveVertex(self, v):
        del self.vertices[v]
        for u in self.vertices:
            self.vertices[u] = [i for i in self.vertices[u] if i[0] != v]
        return self

    def RemoveEdge(self, x, y):
        def RemoveHelper(self, x, y):
            self.vertices[x] = [i for i in self.vertices[x] if i[0] != y]
        RemoveHelper(self, x, y)
        if not self.directed:
            RemoveHelper(self, y, x)
        return self
