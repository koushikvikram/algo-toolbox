# Exploring Undirected Graphs

Topics:
* [Exploring graphs](https://github.com/koushikvikram/algo-toolbox/blob/master/notes/graph_algorithms/1_exploring_undirected_graphs.md#exploring-graphs)
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
    -----------------------------------------------------------------------------
    Inputs: G, s    where G -> Graph, s -> vertex of interest
    Output: {v_1, v_2, ..., v_n} belonging to G, such that there is a "path" from s to v_i

Example: 
- Input: [(A, B), (A, C), (C, D), (D, E)], C
- Output: [A, B, C, D, E]

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
    
**Refining the pseudocode:**


