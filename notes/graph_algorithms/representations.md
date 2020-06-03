# Graph representations

Example graph:

                   A
                  / \
                 B   C
                     /\
                    D  E
                    
**Edge list representation:**
```python
[ [A, B], [A, C], [C, D], [D, E] ]
```

**Adjacency matrix representation:**
```python
[ [0, 1, 1, 0, 0], 
  [1, 0, 0, 0, 0],
  [1, 0, 0, 1, 1],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0] ]
```
For an **undirected graph**, adjacency matrix is **symmetric**.

**Adjacency list:**

```python
[ [B, C],
  [A],
  [A, D, E],
  [C],
  [C] ]
```

Vertices in an adjacency list are not required to appear in any particular order, though it is often convenient to list them in increasing order.

**Degree** (of vertex *i*) in an adjacency list refers to how long i's adjacency list is.
e.g. Degree of "A" is 2 since it's adjacency list [B, C] has length 2.