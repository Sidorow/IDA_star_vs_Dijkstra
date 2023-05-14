import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

class graphGen:
    """
    Vastaa satunnaisen verkon generoinnista.
    Saa parametrinä haluttujen solmujen määrän.
    """

    def __init__(self, nodes):
        self.nodes = nodes
        self.nx_graph = nx.DiGraph()
        self.coords = None
        self.pos = None

    def get_graph(self):
        return nx.to_dict_of_dicts(self.nx_graph)

    def get_coords(self):
        return self.coords

    def euclidean_distance(self, coord1, coord2):
        """
        Laskee kahden solmun euklidisen etäisyyden.

        Args:
            coord1: ensimmäisen solmun koordinaatit
            coord2: toisen solmun koordinaatit

        Returns:
            Float: matka solmujen välillä
        """

        return math.dist(coord1, coord2)

    def gen_weights(self, coords):
        """
        Generoi solmujen kaarten painot
        laskemalla niiden suorat etäisyydet toisistaan

        Args:
            coords: jokaisen solmun koordinaatit tuple -muodossa.
        """

        for node, neighbor in self.nx_graph.edges:
            weight = self.euclidean_distance(coords[node], coords[neighbor])
            self.nx_graph[node][neighbor]['weight'] = round(weight, 4)

    def gen_coordinates(self):
        """
        Ottaa networkx verkon solmujen sijaintien koordinaatit ja asettaa ne
        dictionaryyn tuple -muodossa.
        """

        coords = {node: self.pos[node] for node in self.nx_graph.nodes()}
        coord_tuple = {}
        for key, value in coords.items():
            coord_tuple[key] = (value[0], value[1])

        self.coords = coord_tuple
        self.gen_weights(coord_tuple)

    def gen_random_planar_graph(self):
        """
        Generoi satunnaisen planaarisen tasoverkon.
        Solmujen sijainnit satunnaistetaan Delaunay -
        triangulaatiolla, jotta verkko on oikeasti
        planaarinen.
        """

        self.nx_graph.clear()
        points = np.random.rand(self.nodes, 2)

        tri = Delaunay(points)
        vertices = tri.points

        self.nx_graph.add_nodes_from(range(len(vertices)))
        for simplex in tri.simplices:
            self.nx_graph.add_edge(simplex[0], simplex[1])
            self.nx_graph.add_edge(simplex[1], simplex[2])
            self.nx_graph.add_edge(simplex[2], simplex[0])

        self.pos= {i: v for i, v in enumerate(vertices)}
        self.gen_coordinates()

    def gen_random_graph(self):
        """
        Generoi täysin satunnaisen verkon.
        Solmut ja niiden väliset kaaret satunnaistetaan
        networkx kirjaston algoritmilla.
        """

        self.nx_graph.clear()
        self.nx_graph = nx.fast_gnp_random_graph(self.nodes, 0.2)
        self.pos = nx.random_layout(self.nx_graph)
        self.gen_coordinates()

    def gen_graph_plot(self, path):
        """
        Piirtää kuvan ruudulle verkosta ja jos polku on annettu,
        korostaa kuljetun reitin punaisella.

        Args:
            path: algoritmin palauttama lista läpikäydyistä solmuista
        """

        pos = self.pos

        try:
            algo_edges = [[path[i], path[i+1]]
                        for i in range(len(path)-1)]
        except:
            print("No path")
            algo_edges = None

        options = {
            "node_color": "#A0CBE2",
            "width": 1,
            "edge_cmap": plt.cm.Blues
        }

        labels = nx.get_edge_attributes(self.nx_graph, 'weight')

        plt.figure(figsize=(11,8))
        nx.draw(self.nx_graph, pos, with_labels=True, **options)
        if algo_edges:
            nx.draw_networkx_edges(self.nx_graph, pos, edgelist=algo_edges, edge_color='r', width=3, arrowsize=12)
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=labels, font_size=7)
        plt.show()
