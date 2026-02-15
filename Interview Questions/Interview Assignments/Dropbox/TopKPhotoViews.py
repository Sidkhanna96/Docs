# Q: Track Photo Views and return top k

# Requirements:
# User views an imageId and we increment a count
# We need the top k of those images

# Intuitive:
# track count of images through dict for frequency O(1)
# then convert the count, imageId into maxHeap O(n)
#   OR can just not care about conversion and have a running heap and a set to track the imageId for the top k for repeated values
#   Issue becomes if we pop from the heap OR do a deepcopy - its O(n)
# Then pop the maxHeap k times to get the top K images

# Doubly linked List ? which is in decrementing order where head equates to high number and tail low number
# dictionary that has pointer to index if the photoId already exist
# remove from linkedList and then past the element within the linkedlist


# img1 -> img2 ->


class Node:
    def __init__(self, val, nNext=None, prev=None):
        self.val = val
        self.next = nNext
        self.prev = prev


class DLL:
    def __init__(self):
        self.tail = Node((-1, -1))
        self.head = Node((-1, -1))

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        dllNode = self.head.next

        while dllNode.val[1] > node.val[1]:
            dllNode = dllNode.next

        prevNode = dllNode.prev

        prevNode.next = node
        node.prev = prevNode

        node.next = dllNode
        dllNode.prev = node

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode


class Views:
    def __init__(self):
        self.images = {}
        self.DLL = DLL()

    def viewed(self, imageId):
        node = None
        if imageId not in self.images:
            node = Node((imageId, 1))
        else:
            node = self.images[imageId]
            self.DLL.remove(node)
            node.val[1] += 1

        self.DLL.add(node)
        self.images[imageId] = node

    def topK(self, k):
        arr = []
        cur = self.DLL().head

        while k > 0 and cur:
            cur = cur.next
            arr.append(cur.val[0])
            k -= 1

        return arr


# Overly complicated above - there is not value of DLL here - this is not LRU
