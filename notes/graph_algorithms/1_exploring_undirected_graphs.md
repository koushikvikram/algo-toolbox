# Exploring Undirected Graphs

Topics:
* [Exploring graphs](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#exploring-graphs)
    * [Basic Pseudocode](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#basic-idea-and-pseudocode)
    * [Refined Pseudocode](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#refining-the-pseudocode)
    * [Python Code - Depth First Exploration](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#python-code)
    * [Reach all vertices](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#reach-all-vertices)
* [Connectivity](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#connectivity)
* [Previsit and Postvisit orderings](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#previsit-and-postvisit-orderings)

Example graph (G):

                   A
                  / \
                 B   C
                    / \
                   D   E

## Exploring graphs

Algorithms for exploring graphs.

**Objectives:**
* Implement the **"explore"** algorithms
* Figure out whether or not one vertex of a graph is **"reachable"** from another


        A "path" in a graph G is a sequence of vertices [v_0, v_1, ..., v_n] such that for all i,  (v_i, v_i+1) is an "edge" of G. 


Example: 

- [A, C, D] is a path in G, where (A, C), (C, D) are edges of G. 


        Reachability (from a particular vertex) - Formal Description
        -------------------------------------------------------------------------
        Inputs: G, s            where G -> Graph, s -> vertex of interest
        Output: {v_1, v_2, ..., v_n} belonging to G, such that there is a "path" from s to v_i

Example: 
- Input: [(A, B), (A, C), (C, D), (D, E)], C
- Output: [C, A, B, D, E]

### The "Explore" algorithm

#### Basic idea and pseudocode

We want to make sure that we have "explored" every edge leaving every vertex we have found.

**Basic pseudocode:**

    Component(s)
    -----------------------------------------------------------------------------
    DiscoveredNodes <- {s}
    while there is an edge 'e' leaving DiscoveredNodes that has not been explored:
        add vertex at other end of 'e' to DiscoveredNodes
    return DiscoveredNodes
    
#### Refining the pseudocode

We need to do some work to handle the 'bookkeeping' for this algorithm.
* How do we **keep track** of which edges/vertices we have dealt with?
    * Solution: Make a list called **"visited"** and **add** these **vertices** to it
* What **order** do we explore new edges in?
    * Solution: Let's use the **depth first** order.

**Detailed explanation of 'bookkeeping'**

**Visited:**
- Visit markers:
    - To keep track of vertices found: Give each vertex boolean **visited(v)**
    
- Unprocessed vertices:
    - Keep a list of vertices with edges left to check. This will end up getting hidden in the program stack.
    

**Depth first:**
- We will explore new edges in **Depth First** order. We will follow a long path forward, only backtracking when we hit a dead end.
- We're going to follow some really long path forward until one of two things happen:
    1. We could stumble across a vertex that we've **already seen before**, in which case there's no reason to have followed that edge. So, we'll just go back up to here we were before.
    2. We could hit a **dead end**. Now, since we can't go any further forward, we go back up (not all the way to the beginning) by one step and then try going forward again from the new vertex we found.
    
**Refined pseudocode: (simple recursive algorithm)**

        Explore(v)
        ------------------------------------------------------------
        visited(v) <- true
        for (v, w) belonging to E:
            if not visited(w):
                Explore(w)
            
Simplified explanation:

        for each neighbor of v:
            if it has not been visited, explore it


> We need an **adjacency list representation** of the graph for our program to execute **reasonably efficiently**.

This is because we use a "for loop" to iterate over all neighbors of 'v' and an **adjacency list** can give us the **list of neighbors** in **O(deg)** time.

#### Python Code

```python
def dfs_recursive(graph, vertex, visited=[]):
    # mark vertex as visited
    visited += [vertex]  
    # explore neighbors that haven't been visited
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited = dfs_recursive(graph, neighbor, visited)
    return visited
```

```python
def dfs_iterative(graph, start):
    stack, visited = [start], []
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return visited
```

#### Result

> Theorem: If **all vertices start unvisited**, Explore(v) marks as visited exactly the vertices **reachable** from v.
        
#### Proof

1. Explore(v) only explores things reachable from 'v'.
2. Vertex 'w' is not marked as visited unless explored.
3. If 'w' gets explored, all of its neighbors also get explored.
4. Assume 'u' is reachable from 'v' by path.
    - u --> z --> w --> ... -> v   
5. Assume 'w' is the furthest along the path explored.
6. Then, we must explore the next item. 
    - because, going by point 3, if 'w' gets explored, all of its neighbors also get explored until we reach 'u', which is the end of the path.
   
   
### Reach all vertices

