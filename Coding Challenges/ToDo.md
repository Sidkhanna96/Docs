# Coding Interview Overview:

- What is Data Structures ? Types of structures where data can be stored
- What is Algorithms ? Specific Pattern with code that can be used to solve certain types of problems
- Time Complexity and Space Complexity
  - Common Algorithms that have said complexity (DFS, backtracking, etc)

## Different types of Data Structures (& their associated algorithms):

- Arrays -> 2 pointers, Binary Search, Sliding Window, Backtracking, prefixSum, Kadanes Algorithm √
  - 2D Arrays (Matrix)
  - Queue / Stack
  - Interval
- Set / Hashmap
- String -> 2 pointers, Sliding Window
- Linked List -> 2 pointers, Running Pointers
- Heap / Priority Queue
- Trees: -> DFS, BFS, Backtracking, TopSort, Backtracking, prefixSum (Creating Adjacency List)
  - Trie
  - Segment Tree
  - Binary Search Tree
- Graphs -> Above + Greedy

## Different Types of Algorithms - (& how to spot them):

- 2 Pointers
- Running Pointers
- Binary Search
- Sliding Window
- DFS (iterative, InOrder, inOrder iterative, PreOrder, postOrder)
- BFS
- TopSort
- Backtracking (Find all possible solution)
- Prefix Sum
- interval
- Greedy (Optimization Problem - we have a predefined method of selecting a given edge (i.e. always pick the minimum edge) - find the max or min of something)
  - Dijkstra
  - Disjoint Set Union
  - Minimum Spanning Tree
    - Prims
    - Kruskals
- Dynamic Programming: (Optimization Problem - find all solution pick the best one - find the max or min of something, collection of simpler subproblems -> Solving those subproblems -> storing their solution in memory - Top Down vs Bottom Up -> Recursion -> Memoization)
  - Kadanes
  - Knapsack 0/1 - 1-Dimensional
  - Knapsack 0/2 - 2-Dimensional
- Monotonic Stack

[Optimization](https://www.youtube.com/watch?v=5dRGRueKU3M&list=PLJULIlvhz0rE83NKhnq7acXYIeA0o1dXb)

[Backtracking](https://www.youtube.com/watch?v=DKCbsiDBN6c)

Optimization Problem: - Aim to find the best solution from a set of possible solutions

Backtracking: - find all possible solutions

## Tackling the above DSA problems order:

- Arrays:
  - Algorithm - 2 Pointers, Binary Search, Backtracking, PrefixSum
- Interval
- Monotonic Stack
- String:
  - Algorithm - 2 Pointers, Sliding Window
- Heap / Priority Queue - minHeap tree which has the minimum value on the top
- matrix - Integral Sum(Prefix Sum), layer parsing rotation, rotating matrix
- Trees:
  - Binary Search Tree
  - Trie
  - Segment Tree
    - Algorithms:
      - DFS (Iterative DFS, inOrder, inOrder iterative, preOrder, postOrder)
      - BFS
      - Backtracking
      - TopSort
    - Pattern:
      - Create an Adjacency list and then use above algorithms to solve it
- Graphs:
  - Above + Adjacency list
  - Greedy:
    - Dijkstra
    - Disjoint Set Union
    - Minimum Spanning Tree:
      - Prims
      - Kruskals
- Linked List - 2 Pointers, running pointers
- Dynamic Programming:
  - Top Down vs Bottom Up (Always go Top Down)
  - 1-Dimensional vs 2-Dimensional
  - Memo
  - Kadanes
  - Knapsack 0/1
  - Knapsack 0/2

## Greedy vs Dynamic Programming vs Backtracking:

Optimization Problem - To find the minimum or maximum result

- Greedy - Solve Optimization
  - Follow the same predefined procedure to get best result - Always select shortest path vertex to get vertex
  - local optimal choices hoping would lead to global optimal solution
- Dynamic Programming - Solve Optimization
  - Find all possible solutions instead of per step basis and pick the best one - its a bit more time consuming
  - Principle of Optimality
- Backtracking:
  - Brute Force all possible solutions
  - Not for Optimization - we don't want the best solution - we want all solutions

# Template:

### Videos

### When is it used ?

### Under what Context can it be used ?

### What to know ?

### Questions:

### How it works ?
