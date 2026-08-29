"""
Problem Description
Given the head of a linked list, remove the n<sup>th</sup> node from the end of the list and return its head.
Examples
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Explanation: The second node from the end is 4. After removing it, the list becomes:

1 -> 2 -> 3 -> 5

"""
class Node:
    def __init__(self,item=0,next=None):
        self.item=item 
        self.next=next
def solution(head,n):
    temp_node=Node(0,head)
    slow=temp_node
    fast=temp_node

    for _ in range(n+1):
        fast=fast.next 

    while fast:
        fast=fast.next 
        slow=slow.next 
    
    slow.next=slow.next.next 

    return temp_node.next 

