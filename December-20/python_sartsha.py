class Graph(): 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = 0

	def printSolution(self, dist): 
		print("Vertex \tDistance from Source")
		for node in range(self.V): 
			print(node,'\t',dist[node]) 

	def minDistance(self, dist, sptSet): 

		min = 999999

		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 

	def dijkstra(self, src): 

		dist = [999999] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 
			u = self.minDistance(dist, sptSet) 
			sptSet[u] = True

			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
						dist[v] = dist[u] + self.graph[u][v] 

		self.printSolution(dist) 

n= int(input('Enter number of nodes in graph :'))
g = Graph(n) 
grph = [[0 for column in range(n)] for row in range(n)]
print('Enter values of nodes of graph one by one')
for i in range(n):
	for j in range(n):
		grph[i][j] = int(input())
g.graph = grph
g.dijkstra(0); 

#input:
"""Enter number of nodes in graph :9
Enter values of nodes of graph one by one
0
4
0
0
0
0
0
8
0
4
0
8
0
0
0
0
11
0
0
8
0
7
0
4
0
0
2
0
0
7
0
9
14
0
0
0
0
0
0
9
0
10
0
0
0
0
0
4
14
10
0
2
0
0
0
0
0
0
0
2
0
1
6
8
11
0
0
0
0
1
0
7
0
0
2
0
0
0
6
7
0"""
#output:
"""
Vertex  Distance from Source
0        0
1        4
2        12
3        19
4        21
5        11
6        9
7        8
8        14
"""
