from Dijkstra import Dijkstra
from IDA_star import IDA_star
from graphGen import graphGen

def main():
    graphgen_obj = graphGen(10,14) # Graph generator object
    fixed_graph = graphgen_obj.get_fixed_graph() # Fixed graph for easy illustration purposes
    random_graph = graphgen_obj.gen_random_graph()

    start = 'A'
    goal = 'G'

    dijkstra = Dijkstra(random_graph[0], start, goal)
    ida_star = IDA_star(random_graph[0], random_graph[1], start, goal)

    distances = dijkstra.get_distances()
    path_dijkstra = dijkstra.get_path()
    path_ida = ida_star.get_path()

    print(f"Distances from {start}: {distances} \n")
    print(f"Dijkstra path = {path_dijkstra} \n")
    print(f"IDA* path = {path_ida} \n")
    graphgen_obj.gen_graph_plot(random_graph[0], random_graph[1], path_ida)


if __name__ == "__main__":
    main()