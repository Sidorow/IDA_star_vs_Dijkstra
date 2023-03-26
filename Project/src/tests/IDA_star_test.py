import unittest
from IDA_star import IDA_star

class testIDA_star(unittest.TestCase):
    def setUp(self):
        start = 'A'
        goal = 'G'
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

        self.ida_star = IDA_star(graph, coordinates, start, goal)

    def test_correct_shortest_path(self):
        self.assertEqual(str(self.ida_star.get_path()),
                         "['A', 'B', 'E', 'G']")