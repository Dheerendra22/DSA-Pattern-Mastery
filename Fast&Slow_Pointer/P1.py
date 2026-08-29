"""
Problem Description
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Examples
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

def checkCycle(head):
    if not head or not head.next:
        return False
    slow=head
    fast=head
    while True:
        if fast.next==None or fast.next.next==None:
            return False
        fast = fast.next.next
        slow = slow.next
        if fast==slow:
            return True

# If give error in while condition then use try block

def solution2(head):
    if not head or not head.next:
        return False
    slow=head 
    fast=head

    while True:
        try:
            slow=slow.next 
            fast=fast.next.next
            if slow == fast:
                return True
        except:
            return False
