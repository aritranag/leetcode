import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from my_data_structures.my_linked_list import MyLinkedList,ListNode

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Navigate up 3 levels from 'a.py' to find the folder containing 'x'


def reverseList(head: MyLinkedList) -> MyLinkedList:
    # use 2 pointers, one to point to the current node
    newLinkedList = MyLinkedList()
    _new, _prev = head.head, None
    while _new is not None:
        _tmp = _prev # store the current previous
        _prev = _new # move the previous to the current new
        _new = _new.next # Move the new pointer to point to the next node
        _prev.next = _tmp # update the pointer for the previous node

    newLinkedList.head = _prev
    return newLinkedList

def reverseUsingRecursion(head: MyLinkedList) -> MyLinkedList:

    # TODO
    return None


head1 = [0,1,2,3]
_myLinkedList = MyLinkedList()

for i in head1:
    _myLinkedList.append(i)

_myLinkedList.display()
print()

newLinkedList = reverseList(_myLinkedList)
newLinkedList.display()

         