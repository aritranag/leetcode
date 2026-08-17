class ListNode:
    '''
    Defines a single node of a linked list
    '''
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def append(self, data):
        # Traverse from the head and append the node at the end
        current = self
        while current.next is not None:
            current = current.next
        current.next = ListNode(data)

    
    def display(self):
        # Displays the nodes of the linked list
        current = self
        while current is not None:
            print(current.val, end="")
            current = current.next
            if current:
                print(' -> ',end="")
        print()


# node = ListNode(1)
# node.append(2)
# node.append(4)
# node.append(10)
# node.display()
