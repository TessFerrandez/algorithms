import sys


# Implementing "Min Heap"
class MinHeap:
    def __init__(self, heap_size):
        # Create a complete binary tree using an array
        # Then use the binary tree to construct a Heap
        self.heap_size = heap_size
        # the number of elements is needed when instantiating an array
        # heapSize records the size of the array
        self.min_heap = [0] * (heap_size + 1)
        # realSize records the number of elements in the Heap
        self.real_size = 0

    # Function to add an element
    def add(self, element):
        self.real_size += 1
        # If the number of elements in the Heap exceeds the preset heapSize
        # print "Added too many elements" and return
        if self.real_size > self.heap_size:
            print("Added too many elements!")
            self.real_size -= 1
            return
        # Add the element into the array
        self.min_heap[self.real_size] = element
        # Index of the newly added element
        index = self.real_size
        # Parent node of the newly added element
        # Note if we use an array to represent the complete binary tree
        # and store the root node at index 1
        # index of the parent node of any node is [index of the node / 2]
        # index of the left child node is [index of the node * 2]
        # index of the right child node is [index of the node * 2 + 1]
        parent = index // 2
        # If the newly added element is smaller than its parent node,
        # its value will be exchanged with that of the parent node
        while (self.min_heap[index] < self.min_heap[parent] and index > 1):
            self.min_heap[parent], self.min_heap[index] = self.min_heap[index], self.min_heap[parent]
            index = parent
            parent = index // 2

    # Get the top element of the Heap
    def peek(self):
        return self.min_heap[1]

    # Delete the top element of the Heap
    def pop(self):
        # If the number of elements in the current Heap is 0,
        # print "Don't have any elements" and return a default value
        if self.real_size < 1:
            print("Don't have any element!")
            return sys.maxsize
        else:
            # When there are still elements in the Heap
            # self.realSize >= 1
            remove_element = self.min_heap[1]
            # Put the last element in the Heap to the top of Heap
            self.min_heap[1] = self.min_heap[self.real_size]
            self.real_size -= 1
            index = 1
            # When the deleted element is not a leaf node
            while (index <= self.real_size // 2):
                # the left child of the deleted element
                left = index * 2
                # the right child of the deleted element
                right = (index * 2) + 1
                # If the deleted element is larger than the left or right child
                # its value needs to be exchanged with the smaller value
                # of the left and right child
                if (self.min_heap[index] > self.min_heap[left] or self.min_heap[index] > self.min_heap[right]):
                    if self.min_heap[left] < self.min_heap[right]:
                        self.min_heap[left], self.min_heap[index] = self.min_heap[index], self.min_heap[left]
                        index = left
                    else:
                        self.min_heap[right], self.min_heap[index] = self.min_heap[index], self.min_heap[right]
                        index = right
                else:
                    break
            return remove_element

    # return the number of elements in the Heap
    def size(self):
        return self.real_size

    def __str__(self):
        return str(self.min_heap[1: self.real_size + 1])


# Test cases
minHeap = MinHeap(5)
minHeap.add(3)
minHeap.add(1)
minHeap.add(2)

# [1,3,2]
assert str(minHeap) == "[1, 3, 2]"
assert minHeap.peek() == 1
assert minHeap.pop() == 1
assert minHeap.pop() == 2
assert minHeap.pop() == 3

minHeap.add(4)
minHeap.add(5)

# [4,5]
assert str(minHeap) == "[4, 5]"
