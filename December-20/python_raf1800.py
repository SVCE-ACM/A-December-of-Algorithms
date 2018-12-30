class Graph():
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 

    def printSolution(self, dist): 
        print ("Vertex \t Distance from Source")
        for node in range(self.V): 
            print (node,"\t",dist[node] )

    def minDistance(self, dist, sptSet): 
        min = 9999
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index

    def dijkstra(self, src): 
        dist = [9999] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
        self.printSolution(dist)

def main():
    x = int(input("Enter number of vertices: "))
    g=Graph(x)
    for i in range(x):
        for j in range(x):
            val=int(input("Enter edge value for {}{}: ".format(i,j)))
            g.graph[i][j]=val
    g.dijkstra(0)

if __name__ == "__main__":
    main()
