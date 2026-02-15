## DSA:

### Datastructures:

- Arrays / Strings / Hashmap / Sets
- Stacks / queues -> Monotonic Stack
- Linked List
- Matrix
- Priority Queues
- Trees / Tries
- Graphs
- DSU / Segment Tree / SortedDict (by key) - Not the most important

## DataStructures and Algorithms:

- Arrays / Strings / Hashmap / Sets

  - 2 pointers
    - Removing Duplicates / Elements
    - Merging Arrays
    - Partitioning / Sorting Colors / Dutch National Flag
    - Detecting Cycles
    - Move Zeros
  - Sliding window
    - Longest Substring / Subarray
      - Fails on negative values with exact sum
      - Code:
        - Have a start index + Moving Index
        - Collect information between the 2 indices
        - The moment some condition is violated start moving the start index
  - prefix sum
    - Find range sum
    - Works for exact values (Sum == k) whereas sliding window works for <= k
    - Sum all the elements for an array and find the diff
  - kadanes algorithm
    - Max subarray sum overall in an array
  - intervals
    - min number of meetings rooms available
      - Line Sweep Code:
        - +1 on start and -1 on end+1 of interval in a dictionary
        - then parse the dictionary and create a count
      - Alternative
        - Separate the start and end in 2 separate arrays -> Then parse the start and end to see violation
  - binary search

    - In sorted array find a value
      - Code:
        - ```
          while left <= right:
            if left < mid:
              left += 1
            else:
              right -= 1
          ```
    - first / last occurence

      - Given array of duplicates find the first or last occurence
        - Code: First
          - ```
            while left <= right:
              if nums[mid] == target:
                ans = mid
                right = mid - 1
              elif nums[mid] < target:
                left = mid + 1
              else:
                right = mid - 1
            ```

    - Upper bound and lower bound types
      - First index where value >= target (Lower) OR value > target (Upper)
        - Insert position, first occurence, count occurence
        - Code Lower:
          - ```
            while left < right:
              if nums[mid] < target: # nums[mid] <= target -> Upper value > target
                left = mid + 1
              else:
                right = mid
            ```

  - Removing Duplicates / Frequency
    - Hashmap / Sets

### Algorithms:

- Arrays / Strings / Hashmap / Sets
  - 2 Pointer Algorithm -> Removing duplicates, merging arrays, partitioning / sorting colors / dutch national flag, detect cycles, move zeros, remove elements,
  - Sliding Window -> Longest substring, subarray
    - Have a start pointer and then an index moving
    - Moment there is a scenario where the index and start pointer somehow violate a condition you start moving the start pointer forward in while loop
    - Unique scenario where queues can exist for min and max
    - fails on negative values
  - Kadanes Algorithm -> Max Subarray Sum overall in an array
  - Prefix Sum (Can be used in trees too) -> Find range sum
    - sum the arrays and then find diff that meets a parameter
    - https://leetcode.com/problems/path-sum-iii/
    - prefix sum works for exact values (sum == k) -> sliding window works for <=type
  - Intervals -> Meeting rooms
    - Line Sweep algorithm - +1 on start and -1 on end+1 placed in dictionary - then parse the dictionary and create a count
    - Alternatively, separate the intervals start and end in 2 separate arrays - then parse the start and end to see violations
  - hashmap/set -> removing duplicates
  - Binary Search -> Sorting
    - ```while left <= right:
            if left < mid:
              left += 1
            else:
              right -= 1
      ```
- Stacks / queues
- Linked List
- Matrix
- Priority Queues
- Trees / Tries
  - DFS / BFS / iterative DFS
- Graphs

Optimization:

- Dynamic Programming
- Backtracking
- Greedy -> DSU, Prims, Kruskals, Bellman Ford

## Topics:

- Matrix:
  - Integral Sum - https://leetcode.com/problems/matrix-block-sum/description/?envType=problem-list-v2&envId=prefix-sum
- Stack
  - Monotonic Increasing, Decreasing Stack
  - Building strings or finding distance
  - Find nearest or greatest element
  - **Code**:
    - monotonic decreasing
    - add to stack if the element being added is greater than the pre-existing elements in the stack you keep popping until you find a bigger element
- MinHeap / priority queue
  - Continuously finding the minimum/max of something
  - OR need to do computation for the max of min continously
  - Can use dictionary in adjacent (value, key)
  - import heapq
  - when need to figure out the minimum of something overall - maybe assigning time to taken to complete the task
- Linked List
  - Reverse
  - 2 pointer midpoint
  - **Doubly linked list**
    - LRU Cache
    - Height Balanced Binary Search Tree
    - Browser History
    - Convert BST to DLL
- Tree / Tries
  - DFS
  - BFS / Top Sort
    - Find minimum distance from specific points on 2D matrix
  - Segment Trees ??
- Graphs
  - Above Trees +
  - Create an Adjacency List and then leverage DFS/BFS
- Backtracking

  - Find all possible combinations
  - **Code**
    - recursively select current element or don't select current element (BOTH) increment idexes
    - Another option could be to parse the array entirely and then you omit the element from that idx point

- Greedy

  - Local optimal choices lead to global optimal results
  - DSU: if need to find no cycles in a graph leverage and don't care about weight
    - **Code**:
      - Assign all nodes -1 parents in hash
      - then for 2 nodes find their parents recursively - eventually when get to -1 return the node itself
      - if both nodes are equal return cycle found
      - if one node parent is lower than equal to another node - we further add the parent value of the other node (-ve value) - and that increases the ndoe parent further
        - then we assign the other nodes parent to this new node
        - This enables that if we find the parent of the same node in a hashmap then eventually both will have the same parent
  - Minimum Spanning Tree/Graph problems / Weighted Minimum Spanning Tree - Connect All Nodes:
    - Kruskals (Similar to DSU but cares about weight)
      - Similar to DSU but before doing DSU - you find the Distance or weight between the 2 points and parse it in small to high point distance
    - Prims (Similar to Dijsktra)
      - Have a minHeap for each distance
      - Seen hash/set
      - and then parse through minHeap and keep adding along with distance
      - Store weight from given point
      - https://leetcode.com/problems/min-cost-to-connect-all-points/description/
  - Dijkstra (Does not connect all Nodes - just finds shortest path)

    - Same as prims but the heap stores the minimum cumulative distance as opposed to weight from the given point

      - https://leetcode.com/problems/network-delay-time/description/

    - id dijkstra umbrella under bfs just priority queue and and prims is same just weighted at a given point as opposed to dijkstra which is cumulative?

- DP:
  - Decisions are dependent on each other
  - Recusrion - Top Down vs Bottom up -> Go Top Down it has Recursion in it
  - There is memoization to make it O(n) as opposed to O(branches^depth)
  - 1D DP
    - Bounded (Each item chosen once) vs UnBounded (Each item chosen multiple times)
    - Similar to backtracking - pass the value increment the array - select or do some form of computation
  - 2D DP
    - Bounded vs UnBounded()
    - Different values for same target and how you store those values i.e. (idx, target)
      https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

**How to Spot them**:

## Below shall highlight:

- How to spot which topic to apply
- How do these algorithms work

## Topics:

- Arrays & Strings

  - Binary Search
    - finding target or shrinking in Log(N) of time
    - Sorted
    - **Code**:
      - ```
        left <= right
        left = mid - 1
        right = mid + 1
        ```
      - Mid hasn't been ruled out and we doing bounded search
        ```
        left < right
        left = mid + 1
        right = mid
        ```
  - Sliding Window

    - Finding a substring or another string into another OR sum of subArray
    - Or finding consecutive of something
    - **Code**:
      - have a start pointer and then regular index through a for loop
      - Nested while loop if condition is met increment the start pointer
      - Hashmap to track frequency of a substring/string

  - 2 Pointers
    - need to check both sides and can't traverse the entire array due to TTL

- Hashmap + Set
  - Want to find something unique OR quick lookup O(1)
- Line Sweep:
  - when we need overlapping intervals:
  - +1 and -1 after interval ends in dictionary and then parse through the dictionary keys to track maxval
- Prefix Sum
  - Range sum of something (Tree, array - Sliding Window, and the subrange is calculated by subtracting end point to beginning start point of the range)
  - https://leetcode.com/problems/path-sum-iii/
- Matrix:
  - Integral Sum - https://leetcode.com/problems/matrix-block-sum/description/?envType=problem-list-v2&envId=prefix-sum
- Stack
  - Monotonic Increasing, Decreasing Stack
  - Building strings or finding distance
  - Find nearest or greatest element
  - **Code**:
    - monotonic decreasing
    - add to stack if the element being added is greater than the pre-existing elements in the stack you keep popping until you find a bigger element
- MinHeap / priority queue
  - Continuously finding the minimum/max of something
  - OR need to do computation for the max of min continously
  - Can use dictionary in adjacent (value, key)
  - import heapq
  - when need to figure out the minimum of something overall - maybe assigning time to taken to complete the task
- Linked List
  - Reverse
  - 2 pointer midpoint
  - **Doubly linked list**
    - LRU Cache
    - Height Balanced Binary Search Tree
    - Browser History
    - Convert BST to DLL
- intervals
  - split the intervals into 2 separate arrays and then, parse it individually using 2 pointers
- Tree / Tries
  - DFS
  - BFS / Top Sort
    - Find minimum distance from specific points on 2D matrix
  - Segment Trees ??
- Graphs
  - Above Trees +
  - Create an Adjacency List and then leverage DFS/BFS
- Backtracking

  - Find all possible combinations
  - **Code**
    - recursively select current element or don't select current element (BOTH) increment idexes
    - Another option could be to parse the array entirely and then you omit the element from that idx point

- Greedy

  - Local optimal choices lead to global optimal results
  - DSU: if need to find no cycles in a graph leverage and don't care about weight
    - **Code**:
      - Assign all nodes -1 parents in hash
      - then for 2 nodes find their parents recursively - eventually when get to -1 return the node itself
      - if both nodes are equal return cycle found
      - if one node parent is lower than equal to another node - we further add the parent value of the other node (-ve value) - and that increases the ndoe parent further
        - then we assign the other nodes parent to this new node
        - This enables that if we find the parent of the same node in a hashmap then eventually both will have the same parent
  - Minimum Spanning Tree/Graph problems / Weighted Minimum Spanning Tree - Connect All Nodes:
    - Kruskals (Similar to DSU but cares about weight)
      - Similar to DSU but before doing DSU - you find the Distance or weight between the 2 points and parse it in small to high point distance
    - Prims (Similar to Dijsktra)
      - Have a minHeap for each distance
      - Seen hash/set
      - and then parse through minHeap and keep adding along with distance
      - Store weight from given point
      - https://leetcode.com/problems/min-cost-to-connect-all-points/description/
  - Dijkstra (Does not connect all Nodes - just finds shortest path)

    - Same as prims but the heap stores the minimum cumulative distance as opposed to weight from the given point

      - https://leetcode.com/problems/network-delay-time/description/

    - id dijkstra umbrella under bfs just priority queue and and prims is same just weighted at a given point as opposed to dijkstra which is cumulative?

- DP:
  - Decisions are dependent on each other
  - Recusrion - Top Down vs Bottom up -> Go Top Down it has Recursion in it
  - There is memoization to make it O(n) as opposed to O(branches^depth)
  - 1D DP
    - Bounded (Each item chosen once) vs UnBounded (Each item chosen multiple times)
    - Similar to backtracking - pass the value increment the array - select or do some form of computation
  - 2D DP
    - Bounded vs UnBounded()
    - Different values for same target and how you store those values i.e. (idx, target)
      https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
