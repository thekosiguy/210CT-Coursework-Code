#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
            
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print tree.value

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print tree.value
    if(tree.right!=None):
        in_order(tree.right)
        
'''def in_order2(tree):
    s = []
    current = tree

    s.append(current)
    while current != None:
        current = current.left
        
    if current == None and len(s) > 0:
        current = s.pop()
        print current.value
        current = current.right

        s.append(current)
        while current != None:
            current = current.left
        
    if current == None and len(s) == 0:
        return "done"'''

def recursive_in_order(tree):
    current = tree
    while current != None:
        if current.left == None:
            print current.value
            current = current.right
        else:
            #Find the right child of the node previous to current 
            prevcurrent = current.left
            while prevcurrent.right != None and prevcurrent.right != current:
                prevcurrent = prevcurrent.right
                
           #Set current to right child of node previous to current
            if prevcurrent.right == None:
                prevcurrent = current
                current = current.left
            #Set right child of previous current to null and print value of current node 
            else:
                prevcurrent.right = None
                print current.value
                current = current.right'''

def recursive_in_order(tree):
    class stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            self.items.pop()

        def isEmpty(self):
            return len(self.items) == 0
        
    current = tree
    stack = stack() 
    stack.push(current)
    
    while current != None: 
        current = current.left

        if current == None and stack.isEmpty():
            return "done"
        else:
            popped_node = stack.pop()
            current = popped_node
            if current != None:
                print current.value
                current = current.right'''

def tree_sort(array):
    t = None
    for i in array:
        t = tree_insert(t, i)
    #recursive_in_order(t)
    in_order(t)
    
if __name__ == '__main__':
  array = [6, 10, 5, 2, 3, 3, 4, 11]
  #t=tree_insert(None, 6)
  #tree_insert(t,10)
  #tree_insert(t,5)
  #tree_insert(t,2)
  #tree_insert(t,3)
  #tree_insert(t,4)
  #tree_insert(t,11)
  sortedt = tree_sort(array)





