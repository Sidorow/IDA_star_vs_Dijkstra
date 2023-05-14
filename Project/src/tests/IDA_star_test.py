import unittest
import numpy as np
from util.graphGen import graphGen
from IDA_star import IDA_star

class testIDA_star(unittest.TestCase):
    def setUp(self):
        np.random.seed(123)
        graphgen = graphGen(20)
        graphgen.gen_random_planar_graph()
        start = 8
        goal = 3
        graph = graphgen.get_graph()
        coordinates = graphgen.get_coords()

        self.ida_star = IDA_star(graph, coordinates, start, goal)

    def test_correct_shortest_path(self):
        self.assertEqual(str(self.ida_star.get_path()),
                         "[8, 13, 17, 4, 9, 11, 3]")