## Arrays:

- List of same elements are arrays
- List in python can store mix of elements

`testArray = [1,2,3]`

### Queue: First In First Out

### Stack: Last In First Out

## String:

- character - Represent the Unicode characters
- String - a sequence of characters

`testString = "test"`

## Dictionary:

- Key Value map - Calculate the hash value of the key and map it to array of indexes (Index access is constant time since it maps the hash key to the address directly)

`testHashMap = {"a": [1,2,3], "b": [6,7,8]}`

## Linked List:

- Value and pointer to next address in a node

```
 Class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

## Trees:

- Normal Tree and then Binary Tree

### Tries:

- Normal tree with linking of characters at each level
- If character exist at a certain level then its propogated down that path as opposed to going down another path

## Graphs:

- Trees are Graphs but not all Graphs are trees
- They can be interconnected or not, they can have cycles

## Heap / Priority Queue:

- minHeap (default) / maxHeap - Tree data structure
- smallest element on top wit others just added and once the element is deleted on the top the nexxt smallest one is bubbled up

## Segment Trees:

- segment of parts of different arrays are represented by each node of a tree
- then the tree is propogated down to smaller segments of different indexes
