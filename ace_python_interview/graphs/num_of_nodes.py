# Python3 program to print
# count of nodes at given level.
from collections import defaultdict
from collections import deque
  

class Graph(object):
    def __init__(self):
        self.adj = defaultdict(list)
  
    def addEdge(self,v, w):
        
        # Add w to v’s list.
        self.adj[v].append(w)
    
        # Add v to w's list.
        self.adj[w].append(v)
  
def BFS(adj, s, l):
     
    V = 100
     
    # Mark all the vertices
    # as not visited
    visited = [False] * V
    level = [0] * V
  
    for i in range(V):
        visited[i] = False
        level[i] = 0
  
    # Create a queue for BFS
    queue = deque()
  
    # Mark the current node as
    # visited and enqueue it
    visited[s] = True
    queue.append(s)
    level[s] = 0
  
    while (len(queue) > 0):
         
        # Dequeue a vertex from
        # queue and prit
        s = queue.popleft()
        #queue.pop_front()
  
        # Get all adjacent vertices
        # of the dequeued vertex s.
        # If a adjacent has not been
        # visited, then mark it
        # visited and enqueue it
        for i in adj[s]:
            if (not visited[i]):
  
                # Setting the level
                # of each node with
                # an increment in the
                # level of parent node
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)
  
    count = 0
    for i in range(V):
        if (level[i] == l):
            count += 1
             
    return count
  
# Driver code
if __name__ == '__main__':
     
    # Create a graph given
    # in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
  
    level = 2
  
    print(BFS(g.adj,0, level))