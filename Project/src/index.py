from Dijkstra import Dijkstra
from IDA_star import IDA_star

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

def main():
    start = 'A'
    goal = 'G'

    dijkstra = Dijkstra(graph, start, goal)
    ida_star = IDA_star(graph, coordinates, start, goal)

    distances = dijkstra.get_distances()
    path_dijkstra = dijkstra.get_path()
    path_ida = ida_star.get_path()

    print(f"Distances from {start}: {distances} \n")
    print(f"Dijkstra path = {path_dijkstra} \n")
    print(f"IDA* path = {path_ida} \n")


if __name__ == "__main__":
    main()