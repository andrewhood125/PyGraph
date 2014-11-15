class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        ret_str = self.name + " has neighbors: "
        for vertex in self.neighbors:
            ret_str += str(vertex.name) + ", "
        return ret_str

    def connect(self, vertex):
        vertex.neighbors.append(self)
        self.neighbors.append(vertex)
