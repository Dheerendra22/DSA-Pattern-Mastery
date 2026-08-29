"""
Problem Description

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Examples
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""
def returnMiddle(head):
    if not head :
        return None
    slow = head
    fast = head

    while True:
        if not fast.next or not fast:
            return slow
        else:
           slow = slow.next
           fast = fast.next.next    

# ============ more short form ===========
def solution(head):
    slow =head
    fast=head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    
    return slow 