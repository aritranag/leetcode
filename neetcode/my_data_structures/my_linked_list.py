class ListNode:
    '''
    Defines a single node of a linked list
    '''
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    '''
    Defines my own version of a single Linked List
    '''
    def __init__(self):
        # Creates a linked list with a single node val
        self.head = None
        self.tail = None

    def append(self, val=0):

        _newNode = ListNode(val)

        # if the list is empty then update the head
        if not self.head:
            self.head = _newNode
            self.tail = _newNode
            return
        else:
            # append it to the tail
            self.tail.next = _newNode
            self.tail = _newNode
        

    def prepend(self,val=0):
        # Adds a node to the beginning of the list
        _newNode = ListNode(val,self.head)
        self.head = _newNode

    def display(self):
        # A string representation of the linked list
        _tmp = self.head
        while _tmp is not None:
            print(_tmp.val,end='')
            if _tmp.next is not None:
                print(' -> ',end='')
            _tmp = _tmp.next
