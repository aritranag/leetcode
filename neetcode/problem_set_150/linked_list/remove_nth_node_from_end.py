'''
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Input: head = [1,2], n = 2
Output: [2]

Input: head = [5], n = 1
Output: []
'''
import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from my_data_structures.my_linked_list import ListNode


def removeNthFromEnd(head : ListNode,n:int):
    # uses recursion to find the nth node from the end
    cur = head

    def _recurse(cur,n):
        if cur is None:
            return n-1
        else:
            n = _recurse(cur.next,n)
            if n == -1:
                _tmp = cur.next.next
                cur.next = _tmp
                return n-1
            else:
                return n-1

    n = _recurse(cur,n)

    if n == -1:
        # the first element itself needs to be removed
        head = head.next

    return head

def removeNthFromEnd_Pointer(head : ListNode,n : int):
    # use 2 pointer technique, one n steps removed from another but moves at the same speed
    dummy = ListNode(-1) # dummy node to point to the head, such that head can be removed if needed
    dummy.next = head

    left, right = dummy, head

    # move the right pointer n nodes
    while n>0:
        right = right.next
        n -= 1

    # iterate both pointers till the right pointer is at the end, then left will be exactly n nodes before the end
    while right:
        right = right.next
        left = left.next

    # skip the needed node 
    left.next = left.next.next

    return dummy.next




arr = [1,2,4,8]
head = ListNode(arr[0])
for i in range(1,len(arr)):
    head.append(arr[i])

n = 4
head.display()
head = removeNthFromEnd_Pointer(head, n)
head.display()