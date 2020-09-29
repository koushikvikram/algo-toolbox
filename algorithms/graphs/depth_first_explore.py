# Depth First Exploration - for Adjacency List Representation

def dfe_recursive(graph, vertex):
    visited = [] # can also be named path for an intuitive understanding
    
    def explore(vertex):
        # mark vertex as visited
        visited.append(vertex)
        # explore neighbors that haven't been visited
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                explore(neighbor)
    
    explore(vertex)
    return visited


def dfe_iterative(graph, start):
    stack, visited = [start], []
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return visited


#def dfs_explore_all(graph):
#    visited = []
#    
#    def explore(vertex):
#        # mark vertex as visited
#        visited.append(vertex)
#        # explore neighbors that haven't been visited
#        for neighbor in graph[vertex]:
#            if neighbor not in visited:
#                explore(neighbor)
#    
#    for vertex in graph:
#        if vertex not in visited:
#            explore(vertex)
#    
#    return visited

def dfs_explore_all(graph):
    # same as above code
    visited = []
    
    for vertex in graph:
        if vertex not in visited:
            visited += dfe_recursive(graph, vertex)
            
    return visited


# adjacency list representation of graph
G = { 'A': {'B', 'C'},
      'B': {'A'},
      'C': {'A', 'D', 'E'},
      'D': {'C'},
      'E': {'C'},
      'J': {'K'},
      'K': {'J'},
      'X': {'Y', 'Z'},
      'Y': {'X', 'Z'},
      'Z': {'X', 'Y'} }

'''

                   A            J---K
                  / \
                 B   C          X
                    / \        / \
                   D   E      Y---Z


'''

#print("Reachable from {}: {}".format('A', dfe_recursive(G, 'A')))
#print("Reachable from {}: {}".format('B', dfe_recursive(G, 'B')))
#print("Reachable from {}: {}".format('C', dfe_recursive(G, 'C')))
#print("Reachable from {}: {}".format('D', dfe_recursive(G, 'D')))
#print("Reachable from {}: {}".format('E', dfe_recursive(G, 'E')))
#print("Reachable from {}: {}".format('J', dfe_recursive(G, 'J')))
#print("Reachable from {}: {}".format('K', dfe_recursive(G, 'K')))
#print("Reachable from {}: {}".format('X', dfe_recursive(G, 'X')))
#print("Reachable from {}: {}".format('Y', dfe_recursive(G, 'Y')))
#print("Reachable from {}: {}".format('Z', dfe_recursive(G, 'Z')))

#print("Reachable from {}: {}".format('A', dfe_iterative(G, 'A')))
#print("Reachable from {}: {}".format('B', dfe_iterative(G, 'B')))
#print("Reachable from {}: {}".format('C', dfe_iterative(G, 'C')))
#print("Reachable from {}: {}".format('D', dfe_iterative(G, 'D')))
#print("Reachable from {}: {}".format('E', dfe_iterative(G, 'E')))
#print("Reachable from {}: {}".format('J', dfe_iterative(G, 'J')))
#print("Reachable from {}: {}".format('K', dfe_iterative(G, 'K')))
#print("Reachable from {}: {}".format('X', dfe_iterative(G, 'X')))
#print("Reachable from {}: {}".format('Y', dfe_iterative(G, 'Y')))
#print("Reachable from {}: {}".format('Z', dfe_iterative(G, 'Z')))

print(dfs_explore_all(G))


# Depth First Exploration - for Edge List Representation

E = [('A', 'B'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('J', 'K'), ('X', 'Y'), ('Y', 'Z'), ('X', 'Z')]

def dfe_recursive_edge_list(graph, vertex):
    visited = []
    
    def get_neighbor(edge, vertex):
        vertex_index = edge.index(vertex)
        neighbor_index = 1 - vertex_index
        neighbor = edge[neighbor_index]
        return neighbor
    
    def explore(vertex):
        visited.append(vertex)
        for edge in graph:
            if vertex in edge:
                neighbor = get_neighbor(edge, vertex)
                if neighbor not in visited:
                    explore(neighbor)
    
    explore(vertex)
    return visited


#def dfs_explore_all_edge_list(graph):
#    visited = []
#    
#    def get_neighbor(edge, vertex):
#        vertex_index = edge.index(vertex)
#        neighbor_index = 1 - vertex_index
#        neighbor = edge[neighbor_index]
#        return neighbor
#    
#    def explore(vertex):
#        visited.append(vertex)
#        for edge in graph:
#            if vertex in edge:
#                neighbor = get_neighbor(edge, vertex)
#                if neighbor not in visited:
#                    explore(neighbor)
#    
#    for edge in graph:
#        vertex = edge[0]
#        if vertex not in visited:
#            explore(vertex)
#    return visited


def dfs_explore_all_edge_list(graph):
    # same as above code
    visited = []
    
    for edge in graph:
        vertex = edge[0]
        if vertex not in visited:
            visited += dfe_recursive_edge_list(graph, vertex)
    return visited


#print(dfe_recursive_edge_list(E, 'A'))
#print(dfe_recursive_edge_list(E, 'B'))
#print(dfe_recursive_edge_list(E, 'C'))
#print(dfe_recursive_edge_list(E, 'D'))
#print(dfe_recursive_edge_list(E, 'E'))
#print(dfe_recursive_edge_list(E, 'J'))
#print(dfe_recursive_edge_list(E, 'K'))
#print(dfe_recursive_edge_list(E, 'X'))
#print(dfe_recursive_edge_list(E, 'Y'))
#print(dfe_recursive_edge_list(E, 'Z'))

# let's shuffle the order of edges and check
E = [('A', 'B'), ('A', 'C'), ('X', 'Y'), ('Y', 'Z'), ('X', 'Z'), ('J', 'K'), ('C', 'D'), ('C', 'E')]

print(dfs_explore_all_edge_list(E))

