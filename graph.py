import random, string
from vertex import Vertex

class Graph:

    def __init__(self):
        self.vertices = []

    def populate(self, vertices=10, min_weight=1, max_weight=10):
        for i in range(vertices):
            self.vertices.append(Vertex(self.generate_unique_vertex_name()))
        """ Connect the vertices together """
        self.generate_edges(min_weight, max_weight)

    def generate_unique_vertex_name(self):
        new_vertex_name = self.generate_vertex_name()
        if  self.is_unique_vertex_name(new_vertex_name):
            return new_vertex_name
        else:
            return self.generate_unique_vertex_name()

    def generate_vertex_name(self):
        return random.choice(string.letters)

    def is_unique_vertex_name(self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return False
        return True



    def generate_edges(self, min_weight, max_weight):
        for vertex in self.vertices:
            for i in range(random.randrange(1, len(self.vertices))):
                vertex.connect(random.choice(self.vertices), random.randint(min_weight, max_weight))

    def __str__(self):
        ret_str = "Graph\n"
        for vertex in self.vertices:
            ret_str += str(vertex) + "\n"
        return ret_str
