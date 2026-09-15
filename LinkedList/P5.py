class Node:
    def __init__(self,item,next=None):
        self.item=item 
        self.next=next 

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