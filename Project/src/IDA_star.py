class IDA_star:
    def __init__(self, graph, coords, start, goal):
        self.graph = graph
        self.coords = coords
        self.start = start
        self.goal = goal
        self.heuristic = lambda node, goal: ((coords[node][0] - coords[goal][0])**2 + (coords[node][1] - coords[goal][1])**2)**0.5

    def ida_star(self, graph, start, goal):
        bound = self.heuristic(start, goal)
        while True:
            distance, path = self.search(graph, start, goal, 0, bound, [start])
            if distance == float('inf'):
                return -1, None
            elif distance < 0:
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
            val, t_path = self.search(graph, neighbor, goal, distance+cost, bound, new_path)
            if val < 0:
                return val, t_path
            elif val < min_val:
                min_val = val
                min_path = new_path
        return min_val, min_path

    def get_path(self):
        return self.ida_star(self.graph, self.start, self.goal)[1]

    def get_total_cost(self):
        return self.ida_star(self.graph, self.start, self.goal)[0]
