import math
class IDA_star:
    """
    IDA* algoritmin implementaatio.
    Palauttaa listan läpikäydyistä solmuista.
    Heuristiikkana euklidinen etäisyys solmusta maalisolmuun.
    """

    def __init__(self, graph, coords, start, goal):
        self.graph = graph
        self.coords = coords
        self.start = start
        self.goal = goal
        self.heuristic = lambda node, goal: math.dist(self.coords[node], self.coords[goal])

    def ida_star(self, graph, start, goal):
        bound = self.heuristic(start, goal)
        while True:
            distance, path = self.search(graph, start, goal, 0, bound, [start])
            if distance == float('inf'):
                return -1, None
            if distance < 0:
                return -distance, path
            else:
                bound = distance

    def search(self, graph, node, goal, distance, bound, path):
        if node == goal:
            return -distance, path
        estimate = distance + self.heuristic(node, goal)
        if estimate > bound:
            return estimate, None
        min_val = float('inf')
        min_path = None
        for neighbor, cost in graph[node].items():
            new_path = path + [neighbor]
            val, t_path = self.search(graph, neighbor, goal, distance+cost['weight'], bound, new_path)
            if val < 0:
                return val, t_path
            if val < min_val:
                min_val = val
                min_path = new_path
        return min_val, min_path

    def get_path(self):
        try:
            return self.ida_star(self.graph, self.start, self.goal)[1]
        except:
            return None
