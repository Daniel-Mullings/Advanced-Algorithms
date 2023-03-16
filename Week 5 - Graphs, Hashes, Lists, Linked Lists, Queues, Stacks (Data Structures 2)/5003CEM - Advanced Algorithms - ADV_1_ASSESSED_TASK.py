''' Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
'''

import math
from multiprocessing import parent_process

'''Node class'''
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

'''BST class with insert and display methods, display pretty prints the tree'''
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    #!Section Start - Implementation of Advanced Algorithms - Advanced Assessed Task 1
    #!Author: Daniel Mullings

    #Define method called "IF_LEFT_AND_RIGHT" to remove parent node with left and right child w/ Two parameters:
    #"self" =  Instance of "BinaryTree" object the method is called from is the argument, 
    #"node" = Node to be removed which is parent of left and right child
    def IF_LEFT_AND_RIGHT(self, node):
        delNodeParent = node                                    #Initialise variable "delNodeParent" with "node", responsible for storing parent node to be deleted
        delNode = node.right                                    #Initialise variable "delNode" with right child node of current node, responsible for storing child node to be deleted

        while delNode.left:                                     #While left child node of "delNode" node exists, execute "while" code block
            delNodeParent = delNode                             #Set "delNodeParent" to "delNode"
            delNode = delNode.left                              #Set "delNode" to left child node of "delNode" node

        node.data = delNode.data                                #Set "node" data to "delNode" data

        if delNode.right:                                       #If right child node of "delNode" exists, execute "if" code block
            if delNodeParent.data > delNode.data:               #If "delNodeParent" data greater than "delNode" data, set left child node of "delNodeParent" to right child node of "delNode"
                delNodeParent.left = delNode.right
            else:                                               
                delNodeParent.right = delNode.right             #Set right child node of "delNoteParent" to right child node of "delNode"
        else:                                                   #Else right child node of "delNode" doesn't exist, execute "else" code block
            if delNode.data < delNodeParent.data:               #If "delNode" value less than "delNodeParent" value, set left child node of "delNodeParent" to "None"
                delNodeParent.left = None
            else:                                               
                delNodeParent.right = None                      #Set right child node of "delNodeParent" to "None"

    #Define method called "remove" to iteratively search Binary Tree to find target value and remove Node w/ Two parameters:
    #"self" =  Instance of "BinaryTree" object the method is called from is the argument,
    #"target" = Value to search for in instance of "BinaryTree" object
    def remove(self, target):
        if self.root is None:                                   #If "root" node is "None" (i.e. Doesn’t Exist)
            return False                                        #Return "False" to caller

        elif self.root.data == target:                          #Else if "root" node value equal to "target", execute "elif" code block
            if self.root.left is None and self.root.right is None:
                                                                #If the "root" node has no child node, remove "root" node (i.e. Cessation of Binary Tree existence)
                self.root = None
            elif self.root.left and self.root.right is None:    #Else if "root" node has only a left child node 
                self.root = self.root.left                      #Set "root" node to left child node
            elif self.root.left is None and self.root.right:    #Else if "root" node has only a right child node
                self.root = self.root.right                     #Set "root" node to right child node
            elif self.root.left and self.root.right:            #Else if "root" node has a right and left child node                   
                self.IF_LEFT_AND_RIGHT(self.root)               #Call "IF_LEFT_AND_RIGHT" method with "root" node as argument

        parent = None                                           #Initialise variable "parent" with value "None", responsible for storing parent of current node
        node = self.root                                        #Initialise variable "node" with "self.root", responsible for storing current node
        
        while node.data != target:                              #While "node" value not equal to "target", execute "while" code block
            parent = node                                       #Set the "parent" node to the current "node"
            
            if target < node.data:                              #If "target" greater than "node" value
                node = node.left                                #Set "node" to left child node
            elif target > node.data:                            #Else if "target" less than "node" value
                node = node.right                               #Set "node" to right child node

        #Case 1: Target Not Found
        if node is None or node.data != target:                 #If "node" is "None" or "node" value not equal to "target"
            return False                                        #Return False to caller, info only
        
        #Case 2: Target has no Child
        elif node.left is None and node.right is None:          #Else if left child node is "None" and right child node is "None", execute "elif" code block
            if target < parent.data:                            #If "target" less than "parent" node value
                parent.left = None                              #Set "parent" left node to "None"
            else: 
                parent.right = None                             #Set "parent" right node to "None"
            return True                                         #Return "True" to caller, info only
        
        #Case 3: Target has only left Child
        elif node.left and node.right is None:                  #Else if left child node exists and right child node is "None", execute "elif" code block
            if target < parent.data:                            #If "target" less than "parent" node value
                parent.left = node.left                         #Set "parent" left child node to current "node" left child node
            else:
                parent.right = node.left                        #Set "parent" right child node to current node left child node
            return True                                         #Return "True" to caller, info only
        
        #Case 4: Target has only right Child
        elif node.right and node.left is None:                  #Else if right child node exists and left child node is "None", execute "elif" code block
            if target < parent.data:                            #If "target" less than "parent" node value
                parent.right = node.right                       #Set "parent" right child node to current node right child node
            else:                                               
                parent.left = node.right                        #Set "parent" left child node to current node right child node
            return True                                         #Return "True" to caller, info only

        #Case 5: Target has left and right Child
        else:                                                   #Else current node value equal to target
           self.IF_LEFT_AND_RIGHT(node)                         #Call "IF_LEFT_AND_RIGHT" method with current "node" as argument
    #!Section End - Implementation of Advanced Algorithms - Advanced Assessed Task 1

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)
        print()

    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

#Example calls, which construct and display the Binary Tree
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)

bst.display(bst.root)                                           #Print binary tree of "bst" instance of "BinaryTree" object using "display" method (Before node removal)
bst.remove(6)                                                   #Test iterative "remove" method with value present in "bst" instance of "BinaryTree" object
bst.display(bst.root)                                           #Print binary tree of "bst" instance of "BinaryTree" object using "display" method (After node removal)
