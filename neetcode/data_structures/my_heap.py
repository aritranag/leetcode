class MyHeap:
    def __init__(self,type = 'min'):
        '''
        type = min/max, defines the type of heap, default is a min heap
        '''
        self.heap = []
        self.type = type

    def insert(self,value):
        if not value:
            raise ValueError('Value of the node must be provided')

        self.heap.append(value)
        self.__bubble_up(len(self.heap)-1)

    def pop(self):
        # TODO
        pass

    def heapify(self,n):
        # TODO
        pass
    

    def __bubble_up(self,i):
        # find the right position of the element at index i by comparing the parent and the element
        # if we are at the root then return
        if i == 0:
            return 
        
        parent_i = self.__parent(i)
        # Implementation of min-heap, if child is already greater than parent, do nothing, else swap the values and recurse
        if self.heap[i] >= self.heap[parent_i]:
            return
        else:
            # swap the value of i and its parent and continue with the parent index
            self.__swap(i, parent_i)
            self.__bubble_up(parent_i)

    def __swap(self,i,j):
        # Swap the elements at position i and j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __parent(self,i):
        # Internal method to return the parent of a node
        return (i-1)//2

    def __left_child(self,i):
        # Returns the index of the left child
        return (2*i + 1)

    def __right_child(self,i):
        # Returns the index of the right child
        return (2*i + 2)



    def __str__(self):
        # Prints the heap in tree fashion
        return str(self.heap)
        




x = MyHeap(type='min')
for i in range(10,0,-1):
    x.insert(i)
    print(x)
