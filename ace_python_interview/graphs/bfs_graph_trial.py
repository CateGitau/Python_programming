from collections import defaultdict
from collections import deque

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS_graph(self, start):
        result = ''
        queue = deque()
        visited = [False]*(max(self.graph) + 1)

        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.popleft()
            visited[start] = True
            result += str(start) + '-'

            for i in self.graph[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return result

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
print(g.BFS_graph(2))