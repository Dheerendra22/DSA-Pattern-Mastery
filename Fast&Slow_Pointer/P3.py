"""
Problem Description
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
A palindrome is a sequence that reads the same forward and backward.
Examples
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
Constraints
The number of nodes in the list is in the range [1, 10⁵]
0 <= Node.val <= 9

"""
def checkPalindrome(head):
    if not head :
        return False
    if not head.next:
        return True
    fast=head
    slow = head
    l1=[]
    while True:
        if not fast.next.next:
            l1.append(slow.data)
            break
        elif not fast.next:
            break
        l1.append(slow.data)
        slow = slow.next
        fast = fast.next

    slow = slow.next
    while slow.next:
        if slow.data == l1[-1]:
                l1.pop()
        else:
           return False

    return True
            
# Another way by not using any extra space 
# reverse the second half list !

def solution(head):
    if not head or not head.next:
        return True 
    
    # find middle node

    slow=head
    fast=head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    
    prev = None
    cur = slow 
    while cur: 
        temp=cur.next 
        cur.next=prev 
        prev= cur 
        cur = temp 
    
    t1=head 
    t2=prev 

    result =True 
    while result and t2:
        if t1.item != t2.item:
            result = False 
        t1=t1.next
        t2=t2.next

    return result

