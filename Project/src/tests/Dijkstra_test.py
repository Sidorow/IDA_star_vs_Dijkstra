import unittest
from Dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        start = 'A'
        goal = 'F'
        graph = {
            'A': {'B': 2, 'C': 4},
            'B': {'C': 1, 'D': 5, 'E': 12},
            'C': {'E': 2, 'F': 10},
            'D': {'F': 3},
            'E': {'F': 8},
            'F': {}
        }
        self.dijkstra = Dijkstra(graph, start, goal)


    def test_correct_distances(self):
        self.assertEqual(str(self.dijkstra.get_distances()),
                         "{'A': 0, 'B': 2, 'C': 3, 'D': 7, 'E': 5, 'F': 10}")

    def test_correct_shortest_path(self):
        self.assertEqual(str(self.dijkstra.get_path()),
                         "['A', 'B', 'D', 'F']")
