"""
Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input:

l1 = [2,4,3]
l2 = [5,6,4]

Output:

[7,0,8]

Explanation:

342 + 465 = 807
Example 2:

Input:

l1 = [0]
l2 = [0]

Output:

[0]
Example 3:

Input:

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

Output:

[8,9,9,9,0,0,0,1]
"""
class Node:
    def __init__(self,item,next=None):
        self.item =item
        self.next = next
    

def addList(head1, head2):

    if not head1:
        return head2

    if not head2:
        return head1

    dummy = Node(0)
    current = dummy

    temp1 = head1
    temp2 = head2

    carry = 0

    while temp1 or temp2 or carry:

        # Get values of current nodes
        digit1 = temp1.item if temp1 else 0
        digit2 = temp2.item if temp2 else 0

        # Add the two digits + carry
        total = digit1 + digit2 + carry

        # Digit to store in the new node
        write = total % 10

        # Carry for the next position
        carry = total // 10

        # Create new node
        current.next = Node(write)
        current = current.next

        # Move pointers if they exist
        if temp1:
            temp1 = temp1.next

        if temp2:
            temp2 = temp2.next

    return dummy.next