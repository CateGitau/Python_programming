'''
Implement a function which will take a directed graph and two vertices, A and B. The result will be the
shortest path from A to B.

Remember, the shortest path will contain the minimum number of edges
'''

#graph = {
#    0 -> 1
#    0 -> 2
#    0 -> 3
#    3 -> 5
#    5 -> 4
#    2 -> 4
#}

#Vertex A = 0 
#Vertex B = 4

from Graph import Graph
from Queue import MyQueue
# We only need Graph and Queue for this Question!


def find_min(g, a, b):
    # result = 0
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices

    # For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Breadth First Traversal and enqueue source in it
    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data] or temp.data is b:
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element
    # end of while
    return -1

if __name__ == "__main__" :

    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)

    print(find_min(g, 1, 5))

