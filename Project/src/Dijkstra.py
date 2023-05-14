from util.heap import MinHeap

class Dijkstra:
    """
    Dijkstran algoritmin implementaatio.
    Palauttaa listan läpikäydyistä solmuista.
    """

    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def search(self, graph, start, goal):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        predecessors = {node: None for node in graph}
        nodes = (0,start)
        pq = MinHeap()
        pq.push(nodes)
        while pq:
            (dist, node) = pq.pop()
            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = predecessors[node]
                return path[::-1]
            if dist > distances[node]:
                continue
            for neighbor, cost in graph[node].items():
                new_dist = dist + cost['weight']
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = node
                    pq.push((new_dist, neighbor))
        return None

    def get_path(self):
        try:
            return self.search(self.graph, self.start, self.goal)
        except:
            return None
        