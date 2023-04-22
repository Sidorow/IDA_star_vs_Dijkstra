import math
import random
import networkx as nx
import matplotlib.pyplot as plt

class graphGen:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.nx_graph = nx.DiGraph()
        self.pos = None

    def euclidean_distance(self, coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

    def gen_weights(self, graph, coords):
        for node1 in graph:
            for node2 in graph[node1]:
                weight = self.euclidean_distance(coords[node1], coords[node2])
                graph[node1][node2] = round(weight,2)
        return graph

    def gen_coordinates(self, graph):
        for node in graph.keys():
           self.nx_graph.add_node(node)

        self.pos = nx.fruchterman_reingold_layout(self.nx_graph)

        coords = {node: self.pos[node] for node in self.nx_graph.nodes()}
        coord_tuple = {}
        for key, value in coords.items():
            coord_tuple[key] = (round(value[0],2), round(value[1],2))

        graph = self.gen_weights(graph,coord_tuple)
        return graph, coord_tuple

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

        ready_graph, coordinates = self.gen_coordinates(graph)
        return ready_graph, coordinates

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

        weighted_graph, coordinates = self.gen_coordinates(graph)
        return weighted_graph, coordinates

    def gen_graph_plot(self, graph, coordinates, path):
        for node in graph.keys():
            self.pos[node] = coordinates[node]

        pos = self.pos

        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                self.nx_graph.add_edge(node, neighbor, weight=weight)

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

        labels = nx.get_edge_attributes(self.nx_graph, 'weight')

        plt.figure(figsize=(15,12))
        nx.draw(self.nx_graph, pos=self.pos, with_labels=True, **options)
        if algo_edges:
            nx.draw_networkx_edges(self.nx_graph, pos, edgelist=algo_edges, edge_color='r', width=3, arrowsize=12)
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=labels)
        plt.show()
