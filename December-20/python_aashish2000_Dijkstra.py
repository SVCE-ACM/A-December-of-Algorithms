import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node,"\t",dist[node]) 
  
    def minDistance(self, dist, sptSet): 
  
        min = sys.maxsize 
  
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    def dijkstra(self, src): 
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
  
            for v in range(self.V): 
                if (self.graph[u][v] > 0) and (sptSet[v] == False) and (dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  

n=int(input("Size of Graph: "))
g  = Graph(n) 

mat=[]

for i in range(n):
    inp= input()
    inp=inp.replace(" ","")
    row=list(map(int,inp[1:len(inp)-1].split(',')))
    mat.append(row)

g.graph=mat  
g.dijkstra(0);