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


arr = [1,2,4,8]
head = ListNode(arr[0])
for i in range(1,len(arr)):
    head.append(arr[i])

n = 1
head.display()
head = removeNthFromEnd(head, n)
head.display()