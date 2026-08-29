"""
=======Merge K Sorted list ======== 

Problem Description
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1
Input:
lists = [[1,4,5],[1,3,4],[2,6]]
Output:
[1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
    1 -> 4 -> 5,
    1 -> 3 -> 4,
    2 -> 6
]
Merging them into one sorted list:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
Example 2
Input:
lists = []
Output:
[]
Example 3
Input:
lists = [[]]
Output:
[]

"""


import heapq 
class Node:
    def __init__(self,item=0,next=None):
        self.item=item 
        self.next=next 

def array_to_sll(arr):
    if not arr:
        return None 
    start=Node(arr[0])
    temp=start 
    for data in arr[1:]:
        temp.next=Node(data)
        temp=temp.next 
    return start 
def print_linked_list(start):
    vals =[]
    while start:
        vals.append(str(start.item))
        start=start.next 
    print(" -> ".join(vals) if vals else "Empty")

def sortUsingHeap(list):
    dummy =Node(0)
    current=dummy
    mylists=[]
    for l in list: 
        mylists.append(array_to_sll(l))
    
    min_heap=[]

    for i in range(len(mylists)):
        heapq.heappush(min_heap,(mylists[i].item,i,mylists[i]))

    while min_heap:
        item,i,node=heapq.heappop(min_heap)
        current.next=node 
        current=current.next 

        if node.next:
            heapq.heappush(min_heap,(node.next.item,i,node.next))
    return dummy.next 


print_linked_list(sortUsingHeap([[1,4,5],[1,3,4],[2,6]]))