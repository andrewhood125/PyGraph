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

    def dijkstras(self, start, end):
        visited = [start]
        # Initialize distances
        distances = {}
        for vertex in self.vertices:
            distances[vertex.name] = float("inf")

        # Set start_vertex neighbors weights
        start_vertex = self.get_vertex(start)
        for vertex_name in start_vertex.neighbors:
            distances[vertex_name] = start_vertex.neighbors[vertex_name]
        # distances to itself is 0
        distances[start] = 0

        for node in distances:
            print node + " => " + str(distances[node])

        # select node with min distance in distances that is not in visited
        while len(visited) < len(self.vertices):
            min_node = None
            min_distance = float("inf")
            for node in distances:
                if node not in visited:
                    if distances[node] < min_distance:
                        min_node = node
                        min_distance = distances[node]
            visited.append(min_node)

            print "min node: " + min_node
            # calculate new shortest distances with min_node
            min_node_vertex = self.get_vertex(min_node)
            for neighbor in min_node_vertex.neighbors:
                # if the weight to min_node + min_node to neighbor
                # is less than distances[neighbor] update it.
                temp_distance = distances[min_node] + min_node_vertex.neighbors[neighbor]
                if temp_distance < distances[neighbor]:
                    distances[neighbor] = temp_distance

            for node in distances:
                print node + " => " + str(distances[node])


    def get_vertex(self, char):
        for vertex in self.vertices:
            if vertex.name == char:
                return vertex
        return None

    def add_vertex(self, new_vertex):
        self.vertices.append(Vertex(new_vertex))

    def add_edge(self, start, end, weight):
        start_vertex = self.get_vertex(start)
        end_vertex = self.get_vertex(end)

        start_vertex.connect(end_vertex, weight)
        end_vertex.connect(start_vertex, weight)

