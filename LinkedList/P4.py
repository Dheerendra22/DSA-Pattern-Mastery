class Node:
    def __init__(self,item,next=None):
        self.item=item 
        self.next=next 

def solution(head):
    if not head or not head.next:
        return head 
    length =0
    curr=head 
    while curr:
        length+=1
        curr=curr.next
    
    temp=Node(0)
    temp.next=head
    step=1

    while step<length:
        prev=temp
        curr=temp.next

        while curr:
            left=curr
            right=split(left,step)
            curr=split(right,step)
            prev.next=merge(left,right)

            while prev.next:
                prev=prev.next 
            
        step *=2
    return temp.next

def split(head, n):
    for i in range(n-1):
        if not head:
            break
        head=head.next
    if not head:
        return None
    next_part=head.next
    head.next=None
    return next_part 

def merge(list1,list2):
    temp=Node(0)
    current=temp
    while list1 and list2:
        if list1.item < list2.item:
            current.next=list1 
            list1=list1.next
        else:
            current.next=list2 
            list2=list2.next
        current=current.next

    if list1:
        current.next=list1 
    elif list2:
        current.next=list2 
    return temp.next   

def list_to_linkedlist(arr):
    temp=Node(0)
    current=temp 
    for value in arr:
        current.next=Node(value)
        current=current.next 
    return temp.next 
def linkedlist_to_list(temp):
    result=[]
    while temp:
        result.append(temp.item)
        temp=temp.next
    return result 