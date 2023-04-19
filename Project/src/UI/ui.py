import sys
sys.path.append("../src")
from Dijkstra import Dijkstra
from IDA_star import IDA_star
from graphGen import graphGen

class UI:
    def __init__(self):
        self.graphgen = graphGen(7,10)
        self.graph = self.graphgen.get_fixed_graph()
        self.start = "A"
        self.goal = "G"
        
        self.commands = {
            "exit":"Exit the program",
            "plot":"Show current graph",
            "generate":"Generate a randomized weighted graph",
            "path":"Path the current graph from X to Y",
            "shortest":"Plot the shortest path",
            "help":"Print the list of available commands"
        }
    
    def help(self):
        for cmd, desc in self.commands.items():
            print(f"'{cmd}': {desc}")
            
    def plot(self):
        self.graphgen.gen_graph_plot(self.graph[0], self.graph[1], None)
    
    def generate(self):
        random_graph = self.graphgen.gen_random_graph()
        print("Graph generated.")
        self.graph = random_graph
    
    def path(self):
        start = input("Starting point:  ")
        goal = input("Goal:  ")
        self.start = start
        self.goal = goal
    
    def shortest(self):
        try:
            dijkstra = Dijkstra(self.graph[0], self.start, self.goal)
            ida = IDA_star(self.graph[0], self.graph[1], self.start, self.goal)
            path = ida.get_path()
            print(f"Shortest path from {self.start} to {self.goal} = {path}")
            self.graphgen.gen_graph_plot(self.graph[0], self.graph[1], path)
        except:
            print("Error")
                     
    
    def initialize(self):
        while True:
            cmd = input("Input command, 'exit' to close, 'help' for a list of commands" + "\n")
            if cmd == "exit":
                break
            elif cmd in self.commands:
                eval(f"self.{cmd}")()
            else:
                print("Not a command")
            
def main():
    ui = UI()
    ui.initialize()

if __name__ == "__main__":
    main()