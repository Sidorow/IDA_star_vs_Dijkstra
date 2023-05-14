from Dijkstra import Dijkstra
from IDA_star import IDA_star
from util.graphGen import graphGen
from util.analysis import Analysis
import statistics
import time

class UI:
    def __init__(self):
        self.analyze = Analysis()
        self.graphgen = graphGen(20)
        self.graphgen.gen_random_planar_graph()
        self.start = 0
        self.goal = 19
        self.means = []

        self.commands = {
            "exit":"Exit the program",
            "plot":"Show current graph",
            "gen":"Generate a randomized weighted graph",
            "choose":"Choose start and goal",
            "path":"Plot the shortest path",
            "times":"Prints the mean of execution times when finding shortest paths",
            "clear":"Clear the list of execution times",
            "help":"Print the list of available commands",
            "compare":"Compare the speed of Dijkstra and IDA* algorithms in a randomized graph"
        }

    def help(self):
        for cmd, desc in self.commands.items():
            print(f"'{cmd}': {desc}")

    def plot(self):
        self.graphgen.gen_graph_plot(None)

    def gen(self):
        random_graph = self.graphgen.gen_random_planar_graph()
        self.graph = random_graph
        print("Graph generated.")

    def choose(self):
        try:
            start = input("Start: ")
            goal = input("Goal:  ")
            self.start = int(start)
            self.goal = int(goal)
        except:
            print("Input needs to be a number!")

    def path(self):
        try:
            graph = self.graphgen.get_graph()
            coords = self.graphgen.get_coords()
            dijkstra = Dijkstra(graph, self.start, self.goal)
            ida = IDA_star(graph, coords, self.start, self.goal)
            
            D_start = time.time()
            path_D = dijkstra.get_path()
            D_end = time.time()
            
            IDA_start = time.time()
            path_IDA = ida.get_path()
            IDA_end = time.time()
            
            D_time = D_end - D_start
            IDA_time = IDA_end - IDA_start
            
            print(f"\nTime taken with Dijkstra = {D_time}")
            print(f"Time taken with IDA* = {IDA_time}")
            print(f"\nShortest path between {self.start} and {self.goal}:\n{path_D}\n")
            self.means.append((D_time,IDA_time))
            self.graphgen.gen_graph_plot(path_IDA)
        except:
            print("No path")
    
    def times(self):
        try:
            d_times, ida_times = zip(*self.means)
            mean_d = statistics.mean(d_times)
            mean_ida = statistics.mean(ida_times)
            print(f"\nAverage times of Dijkstra: {mean_d}\nAverage times of IDA*: {mean_ida}\n")
        except:
            print("Timelist is empty!")
        
    def clear(self):
        self.means.clear()
        print("Timelist cleared")
    
    def compare(self):
        list1, list2 = self.analyze.comparison()
        for times, nodes in zip(list1, list2):
            print(f"\nAvg times with {nodes} nodes: \n Dijkstra:{times[0]}\n IDA*:{times[1]}\n")


    def initialize(self):
        while True:
            cmd = input("Input command, 'exit' to close, 'help' for a list of commands" + "\n")
            if cmd == "exit":
                break
            elif cmd in self.commands:
                func = f"self.{cmd}()"
                exec(func)
            else:
                print("Not a command")
    