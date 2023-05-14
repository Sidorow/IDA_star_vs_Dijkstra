import unittest
import numpy as np
from util.graphGen import graphGen
from Dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        np.random.seed(123)
        graphgen = graphGen(20)
        graphgen.gen_random_planar_graph()
        start = 8
        goal = 3
        graph = graphgen.get_graph()
        
        self.dijkstra = Dijkstra(graph, start, goal)

    def test_correct_shortest_path(self):
        self.assertEqual(str(self.dijkstra.get_path()),
                         "[8, 13, 17, 4, 9, 11, 3]")
