import math
import random
import networkx as nx
import matplotlib.pyplot as plt

class graphGen:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def euclidean_distance(self, coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

    def gen_weights(self, graph, coords):
        for node1 in graph:
            for node2 in graph[node1]:
                weight = self.euclidean_distance(coords[node1], coords[node2])
                graph[node1][node2] = round(weight,2)
        return graph

    def gen_coordinates(self, graph):
        coord_dict = {}
        for key in graph.keys():
            rand1 = random.randint(-10,10)
            rand2 = random.randint(-10,10)
            coord_dict[key] = (rand1,rand2)
        return coord_dict

    def gen_random_graph(self):
        graph = {}
        for i in range(self.nodes):
            graph[chr(ord('A') + i)] = {}

        edge_count = 0
        while edge_count < self.edges:
            node1 = chr(ord('A') + random.randint(0, self.nodes - 1))
            node2 = chr(ord('A') + random.randint(0, self.nodes - 1))

            if node1 != node2 and node2 not in graph[node1]:
                graph[node1][node2] = 0
                edge_count += 1

        coords = self.gen_coordinates(graph)
        ready_graph = self.gen_weights(graph, coords)

        return ready_graph, coords

    def get_fixed_graph(self):
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
        return graph, coordinates

    def gen_graph_plot(self, graph, coordinates, path):
        nx_graph = nx.DiGraph()

        for node in graph.keys():
            nx_graph.add_node(node, pos=coordinates[node])

        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                nx_graph.add_edge(node, neighbor, weight=weight)

        pos = nx.get_node_attributes(nx_graph, 'pos')

        try:
            algo_edges = [[path[i], path[i+1]]
                        for i in range(len(path)-1)]
        except:
            print("No path")
            algo_edges = None

        options = {
            "node_color": "#A0CBE2",
            "width": 2,
            "edge_cmap": plt.cm.Blues,
            "arrowsize": 10
        }

        labels = nx.get_edge_attributes(nx_graph, 'weight')

        nx.draw(nx_graph, pos, with_labels=True, **options)
        nx.draw_networkx_edges(nx_graph, pos, edgelist=algo_edges, edge_color='r', width=3, arrowsize=12)
        nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)

        plt.show()
