import sys   
class Graph(): 
  
    def __init__(self, vert): 
        self.V = vert 
        self.graph = [[0 for column in range(vert)]  
                      for row in range(vert)] 
  
    def print(self, d): 
        print("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node,"\t",d[node])  
    def mindist(self, d, sptSet): 
        min = sys.maxsize 
        for v in range(self.V): 
            if d[v] < min and sptSet[v] == False: 
                min = d[v] 
                min_index = v 
        return min_index 
  
    def dijkstra(self, src): 
  
        d = [sys.maxsize] * self.V 
        d[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
            u = self.mindist(d,sptSet) 
            sptSet[u] = True 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and d[v] > d[u] + self.graph[u][v]: 
                        d[v] = d[u] + self.graph[u][v] 
  
        self.print(d) 
  
g  = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]
  
g.dijkstra(0) 
  
