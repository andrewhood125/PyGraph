class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def __str__(self):
        ret_str = self.name + " has neighbors: "
        for vertex in self.neighbors:
            ret_str += vertex + "(" + str(self.neighbors[vertex]) + "), "
        return ret_str

    def connect(self, vertex, weight=0):
        self.neighbors[vertex.name] = weight
