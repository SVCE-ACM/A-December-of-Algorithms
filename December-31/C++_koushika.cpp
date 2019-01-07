 
#include<bits/stdc++.h> 
using namespace std;  
  
class Graph 
{ 
    int V ; 
    list < int > *adj; 
public : 
    Graph( int V ) 
    { 
        this->V = V ; 
        adj = new list<int>[V]; 
    } 
    void addEdge( int s , int d ) ; 
    int BFS ( int s , int d) ; 
}; 
  
// add edge to graph 
void Graph :: addEdge ( int s , int d ) 
{ 
    adj[s].push_back(d); 
    adj[d].push_back(s); 
} 
  
// Level  BFS function to find minimum path 
// from source to sink 
int Graph :: BFS(int s, int d) 
{ 
    // Base case 
    if (s == d) 
        return 0; 
  
    // make initial distance of all vertex -1 
    // from source 
    int *level = new int[V]; 
    for (int i = 0; i < V; i++) 
        level[i] = -1  ; 
  
    // Create a queue for BFS 
    list<int> queue; 
  
    // Mark the source node level[s] = '0' 
    level[s] = 0 ; 
    queue.push_back(s); 
  
    // it will be used to get all adjacent 
    // vertices of a vertex 
    list<int>::iterator i; 
  
    while (!queue.empty()) 
    { 
        // Dequeue a vertex from queue 
        s = queue.front(); 
        queue.pop_front(); 
  
        // Get all adjacent vertices of the 
        // dequeued vertex s. If a adjacent has 
        // not been visited ( level[i] < '0') , 
        // then update level[i] == parent_level[s] + 1 
        // and enqueue it 
        for (i = adj[s].begin(); i != adj[s].end(); ++i) 
        { 
            // Else, continue to do BFS 
            if (level[*i] < 0 || level[*i] > level[s] + 1 ) 
            { 
                level[*i] = level[s] + 1 ; 
                queue.push_back(*i); 
            } 
        } 
  
    } 
  
    // return minimum moves from source to sink 
    return level[d] ; 
} 
  
bool isSafe(int i, int j, int M[][N]) 
{ 
    if ((i < 0 || i >= N) || 
            (j < 0 || j >= N ) || M[i][j] == 0) 
        return false; 
    return true; 
} 
  
// Returns minimum numbers of  moves  from a source (a 
// cell with value 1) to a destination (a cell with 
// value 2) 
int MinimumPath(int M[][N]) 
{ 
    int s , d ; // source and destination 
    int V = N*N+2; 
    Graph g(V); 
  
    // create graph with n*n node 
    // each cell consider as node 
    int k = 1 ; // Number of current vertex 
    for (int i =0 ; i < N ; i++) 
    { 
        for (int j = 0 ; j < N; j++) 
        { 
            // source index 
            if( M[i][j] == 1 ) 
                s = k ; 
  
            // destination index 
            if (M[i][j] == 2) 
                d = k; 
            k++; 
        } 
    } 
  
    // find minimum moves 
    return g.BFS (s, d) ; 
} 
  
// driver program to check above function 
int main() 
{ 
    int M[N][N],i,j;
    cin>>N;
    for(i=0;i<N;i++)
    {
    for(j=0;j<N;i++)
    {
    cin>>M[i][j];
    }
    }
    cout << MinimumPath(M) << endl; 
  
    return 0; 
} 
