'''
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.
'''
import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from my_data_structures.my_linked_list import ListNode

def hasCycle(head : ListNode) -> bool:
    # use slow and fast pointers, if they meet then there is a cycle, if fast pointers goes to None, then there is no cycle
    slow, fast = head, head

    if not head or not head.next:
        return False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


arr = [1,2,4]
head = ListNode(arr[0])
for i in range(1,len(arr)):
    head.append(arr[i])

# store the 2nd Node address
second_node = head.next
cur = head
while cur.next is not None:
    cur = cur.next

# create the cycle
#cur.next = second_node
print(hasCycle(head))

