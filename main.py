from graph import Graph
graph = Graph()
graph.populate(45)
#graph.add_vertex("A")
#graph.add_vertex("B")
#graph.add_vertex("C")
#graph.add_vertex("D")

#graph.add_edge("A", "B", 5)
#graph.add_edge("A", "C", 1)
#graph.add_edge("B", "D", 2)
#graph.add_edge("C", "D", 1)

print graph

start = graph.vertices[0]
end = graph.vertices[-1]

print "Start: " + str(start)
print "End: " + str(end)
distance = graph.dijkstras(start.name, end.name)

print "Distance from " + start.name + " to " + end.name + ": " + str(distance)

