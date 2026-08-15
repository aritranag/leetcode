'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
'''

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from my_data_structures.my_linked_list import MyLinkedList,ListNode

def mergeTwoLists(list1 : MyLinkedList, list2 : MyLinkedList) -> MyLinkedList:
    res = MyLinkedList()
    res.append(-1)
    head = res.head
    list1, list2 = list1.head, list2.head

    # while there are nodes in both lists, compare and add
    while list1 and list2:
        if list1.val <= list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next

    head.next = list1 or list2
    
    res.head = res.head.next

    return res

l_list1, l_list2 = MyLinkedList(),MyLinkedList()
list1 = [1,2,4]
list2 = [1,3,5]

for val in list1:
    l_list1.append(val)

for val in list2:
    l_list2.append(val)


res = mergeTwoLists(l_list1,l_list2)
res.display()