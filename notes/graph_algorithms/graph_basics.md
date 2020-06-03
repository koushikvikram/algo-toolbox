# Graph basics

* Graph: An abstract concept that represents *connections* between objects.
* *Undirected* Graph: A collection ***V*** of ***vertices*** and a collection ***E*** of ***edges*** each of which *connects a pair of vertices*.

**Unusual patterns in graphs**

* Loops: Connect a vertex to itself
* Multiple edges between same vertices

A *simple graph* is a graph that has no unusual patterns.

Most common operations on graphs:
* Is edge?
* List all edges
* List all neighbors

Graph algorithm runtimes depend on 2 measures of sizes: 
- **|V|** (number of vertices) 
- **|E|** (number of edges) 

**Things to consider while building and working with graphs** (influences runtime of common operations on graphs)
* Graph representation
    * Edge list
    * Adjacency matrix (Lookup Table)
    * Adjacency list
* Graph density
    * Sparse graph: |E| ~= |V| 
    * Dense graph: |E| ~= |V|^2
    
    

| Operation        | Is Edge? | List Edges | List Neighbors |
|------------------|----------|------------|----------------|
| Adjacency matrix |    O(1)  |   O(V^2)   |      O(V)      |
| Edge list        |    O(E)  |   O(E)     |      O(E)      |
| Adjacency list   |   O(deg) |   O(E)     |     O(deg)     |

