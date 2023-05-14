from IDA_star import IDA_star
from Dijkstra import Dijkstra
from util.graphGen import graphGen
from statistics import mean
import time
import random
import signal

def timeout_handler(signum, frame):
    raise Exception("Function timed out")

class Analysis:
    def __init__(self):
        pass
    
    def avg_times(self, times):
        """
        Laskee listan sisältämien arvojen keskiarvon.
        
        Args:
            times: Lista ajoista tuple:ina.

        Returns:
            Aikojen keskiarvot tuple -muodossa.
        """
        
        avg_timelist = []
        for list in times:
            avg = (mean([x for x, y in list]), mean([y for x, y in list]))
            avg_timelist.append(avg)
        return avg_timelist
    
    def measure(self, alg):
        """
        Laskee algoritmin suoritusajan ja palauttaa ajan float-
        muodossa. Jos polkua ei löydy, palauttaa myös arvon 0, muutoin 1.
        
        Args:
            alg: halutun algoritmin olio. 

        Returns:
            float, int: Aika ja binäärinen arvo, löytyikö polkua.
        """
        
        timeout = 4
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        
        try:
            start_time = time.time()
            path = alg.get_path()
            end_time = time.time()
            signal.alarm(0)
        except Exception:
            print("Function timed out")
            
        if path != None:
            return end_time - start_time, 1
        
        return end_time - start_time, 0
    
    def comparison(self):
        """
        Vertaa Dijkstran ja IDA*:in nopeutta löytää polku.
        "node_list" sisältää solmujen määriä, joita halutaan testata.
        Generoi esimerkiksi verkon, jossa on 100 solmua, sitten 1000 jne.

        Returns:
            list, list: lista ajoista tupleina ja listan solmumääristä.
        """
        
        node_list = [100, 1000, 2500]
        timelist = []
        for node_count in node_list:
            print(f"Node count: {node_count}")
            for x in range(10):
                print(f"Iteration {x+1}")
                graphgen = graphGen(node_count)
                graphgen.gen_random_graph()
                graph = graphgen.get_graph()
                coords = graphgen.get_coords()
                D_times = []
                IDA_times = []
                
                for i in range(10):
                    print(i+1)
                    start = random.randint(0, node_count-1)
                    goal = random.randint(0, node_count-1)
                    dijkstra = Dijkstra(graph, start, goal)
                    ida_star = IDA_star(graph, coords, start, goal)
                
                    IDA_time, IDA_path = self.measure(ida_star)
                    D_time, D_path = self.measure(dijkstra)
                    if IDA_path == 0:
                        continue
                    D_times.append(D_time)
                    IDA_times.append(IDA_time)
                    
        
            D_avg = mean(D_times)
            IDA_avg = mean(IDA_times)
            timelist.append((round(D_avg, 7), round(IDA_avg, 7)))
        
        return timelist, node_list

                
            
        