from Graph import Graph
# We only need Graph and Stack for this Challenge!

def detect_cycle(g):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices
    # rec_node_stack keeps track of the nodes which are part of
    # the current recursive call
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True
    return False

def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if rec_node_stack[node]:
        return True
    # It has been visited before this recursion
    if visited[node]:
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True
    head_node = g.array[node].head_node
    while head_node is not None:
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head_node = head_node.next_element
    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False

if __name__ == "__main__" :
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)
    
    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))
