import heapq
from heap import MinHeap

class Dijkstra:
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
        #pq = [(0, start)]
        while pq:
            (dist, node) = pq.pop()
            #(dist, node) = heapq.heappop(pq)
            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = predecessors[node]
                return path[::-1], distances
            if dist > distances[node]:
                continue
            for neighbor, cost in graph[node].items():
                new_dist = dist + cost
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = node
                    pq.push((new_dist, neighbor))
                    #heapq.heappush(pq, (new_dist, neighbor))
        return None

    def get_distances(self):
        try:
            return self.search(self.graph, self.start, self.goal)[1]
        except:
            return None

    def get_path(self):
        try:
            return self.search(self.graph, self.start, self.goal)[0]
        except:
            return None