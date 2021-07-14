from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for i in range(self.V)]

    def addEdge(self, u, v):
        self.adj[u].append(v) 
        self.adj[v].append(u)


    def countEdges(self):
        # For undirected graph, just sum up the size of
        # all the adjacency lists for each vertex
        Sum = 0
        
        for i in range(self.V):
            # add all the edges that are linked
            #to the current vertex
            Sum+= len(self.adj[i])

        # The count of edge is always even  
        # because in undirected graph every edge  
        # is connected twice between two vertices 
        return Sum//2


# Driver Code
if __name__ == '__main__':
      
    V = 9
    g = Graph(V) 
  
    # making above uhown graph 
    g.addEdge(0, 1 ) 
    g.addEdge(0, 7 ) 
    g.addEdge(1, 2 ) 
    g.addEdge(1, 7 ) 
    g.addEdge(2, 3 ) 
    g.addEdge(2, 8 ) 
    g.addEdge(2, 5 ) 
    g.addEdge(3, 4 ) 
    g.addEdge(3, 5 ) 
    g.addEdge(4, 5 ) 
    g.addEdge(5, 6 ) 
    g.addEdge(6, 7 ) 
    g.addEdge(6, 8 ) 
    g.addEdge(7, 8 ) 

    print(g)
  
    print(g.countEdges())

