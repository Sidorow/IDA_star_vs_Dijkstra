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
        path = [start]
        while True:
            distance, path = self.search(graph, start, goal, 0, bound, path)
            if distance <= 0:
                return -distance, path
            if distance == float('inf'):
                return -1, None
            bound = distance

    def successors(self, node):
        elements = self.graph[node].keys()
        sorted_elem = sorted(elements, key=lambda x:
            self.graph[node][x]['weight'] + self.heuristic(x,self.goal))
        return sorted_elem

    def search(self, graph, node, goal, distance, bound, path):
        node = path[-1]
        estimate = distance + self.heuristic(node, goal)
        if estimate > bound:
            return estimate, None
        if node == goal:
            return -distance, path
        min_val = float('inf')

        for neighbor in self.successors(node):
            if neighbor not in path:
                path.append(neighbor)
                cost = self.graph[node][neighbor]['weight']
                val, t_path = self.search(graph, neighbor, goal, distance + cost, bound, path)
                if val < 0:
                    return val, t_path
                if val < min_val:
                    min_val = val
                path.pop()
        return min_val, path

    def get_path(self):
        try:
            return self.ida_star(self.graph, self.start, self.goal)[1]
        except:
            return None
