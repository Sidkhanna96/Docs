### Videos

- N/A

### When is it used ?

- For tree like data Strutures

### Under what Context can it be used ?

- Used for file systems
- Category organization
- DB indexing - efficient searching and retrieval of data

### What to know ?

- Trees (& Binary Tree):
  - DFS:
    - Iterative DFS (Stacks)
    - Inorder
      - Iterative Inorder
    - PreOrder
    - PostOrder
  - BFS (Queues)
  - Backtracking - Finding all possible solutions
  - Segment Tree
  - Min Heaps
  - Tries
- Graphs:
  - Adjacency List
  - Top Sort
  - Greedy
    - MST (No Cycles)
      - DSU
      - Kruskals
      - Prims
    - Dijkstra

### Questions:

### How it works ?

- DFS:
  - It goes down the tree first - Could be useful to find depth of a tree

```
def dfs(self, root):

    node = root

    for children in node.neighbors:
        self.dfs(children)
```

- Iterative DFS:
  - It uses stack to go down the tree

```
def dfs(self, root):
    stack = [root]

    while stack:
        node = stack.pop()

        for children in node.neighbors:
            stack.append(children)

```

- Inorder:
  - InOrder -> left tree -> root -> right tree
  - PreOrder -> root -> left tree -> right tree
  - PostOrder -> left tree -> right tree -> root

```
def dfs(self, root):
    if not root:
        return

    self.dfs(root.left)
    root
    self.dfs(root.right)
```

- Iterative Inorder:
  - through stack

```
def dfs(self, root):
    stack = [root]

    while stack:
        node = stack.pop()

        if node.left:
            stack.append(node)
        else:
            nextNode = stack.pop()
            print(nextNode)

            node.append(nextNode.right)
```

- BFS

  - Use queues - traverse all the neighbors before going down the tree

```
def bfs(self, root):
queue = [root]

while queue:
    node = queue.pop(0)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
```

- Backtracking:

  - This is used to go down all the trees and find all the solutions (If a solution is not meeting a criteria we prune it)

```
// All Combinations of an array of nums - but this forms a tree to do that
def backtracking(self, nums, path):

    for i in range(len(nums)):
        self.backtracking(nums[:i] + numd[i+1:], path + [nums[i]])

def example(self, nums):
    self.res = []
    self.backtracking(nums, [])

```

- Segment Tree:
  - In a way prefixSum

```
// This is how each node in a segment tree looks
class Node:
def __init__(self, start, end):
    self.start = start // Start Index
    self.end = end // End Index
    self.total = 0 // Total Sum between the index
    self.left = None // Left tree
    self.right = None // Right tree

def __init__(self, nums: List[int]):
        def createTree(nums, start, end):
            if start == end:
                root = Node(start, end)
                root.total = nums[start]
                return root

            root = Node(start, end)

            mid = (start + end)//2

            root.left = createTree(nums, start, mid)
            root.right = createTree(nums, mid+1, end)

            root.total = root.left.total + root.right.total

            return root

        self.root = createTree(nums, 0, len(nums)-1)
```

- Min Heaps:

  - It just has the minimum element in the tree bubbled to top

```
import heapq

heapq.heapify(nums)
heapq.heappush(nums, 5)
heapq.heappop(nums)
```

- Tries:
  - Helps in searching algorithm

```
def trieFunc(self, word)
    self.trie = {}

    node = self.trie

    for letter in word:
        if letter not in node:
            node[letter] = {}
        node = node[letter]

    node["*"] = "\n"
```

- Graphs:

  - Can have cycles within it
  - AdjacencyList:
    - Its a dictionary to map all the connected neighbors for a given node
    - You can use the adjacency list to parse through the graph - using above tree structures - like DFS - Recursive is a good start
  - Top Sort:

    - Essentially when we need to parse a graph with some of them not having an invertex and we want to see if all graphs are reachable we use this

    ```
    adjacencyList = {}
    for start, end in node:
        adjacencyList[start].append(end)

    queue = []

    while queue:
        node = queue.pop(0)

        for nextNode in adjacencyList[node]:
            queue.append(nextNode)

    ```

  - [Greedy](./Greedy.md)
