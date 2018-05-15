import math

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkNode(root, -math.inf, math.inf)
    
def checkNode(root, lowerbound, upperbound):
    if root is None:
        return True
    else:
        # Check the following:
        # 1. The data is between the lowerbound and upperbound
        # 2. The right side of the tree is a BST
        # 3. The left side of the tree is a BST
        return (root.data > lowerbound and root.data < upperbound) and \
               checkNode(root.right, max(root.data, lowerbound), upperbound) and \
               checkNode(root.left, lowerbound, min(root.data, upperbound))
        
        
    