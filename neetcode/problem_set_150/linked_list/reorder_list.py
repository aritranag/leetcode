'''
You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example, can intially be represented as: [0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order: [0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order: [0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Input: head = [2,4,6,8]
Output: [2,8,4,6]

Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]
'''
import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from my_data_structures.my_linked_list import ListNode

def reorderListUsingStack(head:ListNode) -> None:
    # store the head
    cur = head
    if not head or not head.next:
        return

    stack = []
    # append all nodes to the stack
    while cur:
        stack.append(cur)
        cur = cur.next

    # use 2 pointers technique
    i,j = 0,len(stack)-1
    while i<j:
        stack[i].next = stack[j]
        i += 1
        stack[j].next = stack[i]
        j -= 1

    stack[i].next = None

    
arr = [2,4,8]
head = ListNode(arr[0])
for i in range(1,len(arr)):
    head.append(arr[i])

head.display()
reorderListUsingStack(head)
head.display()
    

        
    
