import networkx as nx
import matplotlib.pyplot as plt
import math

graph = {
    'A': {'B': 1.41, 'C': 1.41, 'D': 2.23},
    'B': {'E': 1.0},
    'C': {'E': 1.0, 'F': 2.23},
    'D': {'F': 2.23},
    'E': {'G': 1.0},
    'F': {'G': 3.16},
    'G': {}
}

coordinates = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (1, -1),
    'D': (-1, 1),
    'E': (2, 0),
    'F': (0, -2),
    'G': (3, 0)
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def gen_weights(graph):
    for node1 in graph:
        for node2 in graph[node1]:
            weight = euclidean_distance(coordinates[node1], coordinates[node2])
            graph[node1][node2] = weight



# create a networkx graph object
nx_graph = nx.Graph()

for node in graph.keys():
    nx_graph.add_node(node, pos=coordinates[node])

# add edges to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        nx_graph.add_edge(node, neighbor, weight=weight)

# position nodes using a spring layout
#pos = nx.spring_layout(nx_graph)
pos = nx.get_node_attributes(nx_graph, 'pos')

# draw the graph nodes and edges
nx.draw(nx_graph, pos, with_labels=True)

# draw edge labels
labels = nx.get_edge_attributes(nx_graph, 'weight')
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)

# show the plot
plt.show()
