### Videos

- https://www.youtube.com/watch?v=ARvQcqJ_-NY&list=PLfFeAJ-vQopt_S5XlayyvDFL_mi2pGJE3
- https://www.youtube.com/watch?v=wU6udHRIkcc 
- https://www.youtube.com/watch?v=4ZlRH0eK-qQ 

### When is it used ?
- Optimization Problems: A problem that requires min or max result out of possible solutions - On each step we have a set of pre-existing condition we can check to see if its met then thats the feasible s`olution

### Under what Context can it be used ?
- If we wanted to construct the most optimal and efficient way to connect a set of cities for a train infrastructure with minimum distance travelled between all cities or minimum distance from one point to another

### What to know ?
- **Minimum Spanning Tree:**
    - If given a weighted graph we want to find no cycles within it (its a tree - subgraph of a graph)
    - and we want to find the minimum distance between each edge 
    - Finding all possible spanning tree would have high time complexity
    - **Algorithms:**
        - Kruskals Algorithm
            - Disjoint Set Union (By Rank)
        - Prims Algorithm
        
- **Dijkstra Algorithm:**
    - Used for find the shortest path from point A to point B

- Differences:
    - Pure Disjoint Set Union (By Rank) - Used to detect cycles (Tree don't have cycles)
    - Kruskals Algorithm - Utilizes DSU but works under weighted Graph - MST
    - Prims Algorithm - Weighted Graph - MST
    - Dijkstra - Does may not utilize all the edges it just find the minimum distance from point A to B in a graph - that does not mean all the edges are used even if they're checked



### Questions:
-  [Disjoint Set Union by Rank (Kruskals in a way - but does not care about finding minimum just finding cycle - Kruskal Operate with weighterd unidirected graph)](https://leetcode.com/problems/redundant-connection/description/)
- [Prims or Kruskals](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)
- [Dijkstra](https://leetcode.com/problems/network-delay-time/description/)


### How it works ?
- [Disjoint Set Union by Rank](https://www.youtube.com/watch?v=wU6udHRIkcc):
    - Disjoint is when 2 sets don't have an edge in common then perform union on those disjoint sets ({1,2}, {3,4} - (2,3))
    - if we find an edge eventually that belongs to same set then there is a cycle - or that edge is a cycle so don't use ({1,2,3,4} - (2,3))
    - Question:
        - Find the one additional edge that should not be there that converts the tree into a graph making it have a cycle
        - 2 functions union and find
            - Union is used if not the same parent then the edges are not connected we can connect them and give one of the edges a common parent
                - If same root found in both nodes of edges then cycle found! 
            - find is used to find the root most parent of a node (-ve value)
- Kruskals Algorithm:
    - Always select minimum edge (We don't care if we have visited it or not)
    - if selected edge forms a cycle then ignore it
    - Question:
        - we calculate all the manhattan distances
        - then we sort if based on weight
        - for each edge we can do a DSU if it is part of the cycle then ignore it
- Prims:
    - you select an edge and from there you select the minimum edge you can take from the list of connected edges
        - Have a list to track the point that have been visited 
        - use minHeap for all the fistances you can measure from current point 
- Dijkstra:
    - Purpose is to select the shortest path from source A to B




