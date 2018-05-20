"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    
    has_cycle = False
    dict = {}
    dict[head] = 1
    
    current = head
    while current.next != None:
        
        if current.next in dict:
            has_cycle = True
            break
        else:
            dict[current.next] = 1
    
    return has_cycle
        