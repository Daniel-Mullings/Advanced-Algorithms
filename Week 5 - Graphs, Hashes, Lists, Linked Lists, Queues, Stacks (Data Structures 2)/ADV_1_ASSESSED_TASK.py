""" 
Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
"""

import math

""" Node class """
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods, display pretty prints the tree """
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

    #!Section Start - Implementation of Advanced Algorithms - Advanced 1 Assessed Task
    #!Author: Daniel Mullings

    #Define method called "IF_LEFT_AND_RIGHT" to remove parent node with left and right child w/ Two parameters:
    #"self" =  Instance of "BinaryTree" object class the method is called from is the argument, "node" = Node to be removed which is parent of left and right child
    def IF_LEFT_AND_RIGHT(self, node):

        #Initialize variable "delNodeParent" with value "node", responsible for storing parent node to be deleted
        #Initialize variable "delNode" with right child node of current node, responsible for storing child node to be deleted
        delNodeParent = node
        delNode = node.right

        #While left child node of "delNode" node exists, execute "while" code block
        while delNode.left:
            #Set "delNodeParent" to "delNode"
            delNodeParent = delNode
            #Set "delNode" to left child node of "delNode" node
            delNode = delNode.left

        #Set "node" value to "delNode" value
        node.data = delNode.data

        #If right child node of "delNode" exists, execute "if" code block
        if delNode.right:
            #If "delNodeParent" value greater than "delNode" value, set left child node of "delNodeParent" to right child node of "delNode"
            if delNodeParent.data > delNode.data:
                delNodeParent.left = delNode.right
            #Else set right child node of "delNoteParent" to right child node of "delNode"
            else:
                delNodeParent.right = delNode.right

        #Else right child node of "delNode" dosen't exist, execute "else" code block
        else:
            #If "delNode" value less than "delNodeParent" value, set left child node of "delNodeParent" to "None"
            if delNode.data < delNodeParent.data:
                delNodeParent.left = None
            #Else set right child node of "delNodeParent" to "None"
            else:
                delNodeParent.right = None

    #Define method called "remove" to iteratively search Binary Tree to find target value and remove Node w/ Two parameters:
    #"self" =  Instance of "BinaryTree" object class the method is called from is the argument, "target" = Value to search for in instance of "BinaryTree" object class
    def remove(self, target):
        #If "root" node is "None" (i.e. Doesn’t Exist), return "False" to caller
        if self.root is None:
            return False
        
        #Else if "root" node value equal to "target" value, execute "elif" code block
        elif self.root.data == target:
            #If the "root" node has no child node, remove "root" node (i.e. Cessation of Binary Tree existence)
            if self.root.left is None and self.root.right is None:
                self.root = None
            #Else if "root" node has only a left child node, set "root" node to left child node
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            #Else if "root" node has only a right child node, set "root" node to right child node
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            #Else if "root" node has a right and left child node, call "IF_LEFT_AND_RIGHT" method with "root" node as argument
            #"IF_LEFT_AND_RIGHT" method handles removal of "root" parent node with left and right child whilst preserving Binary Tree structure
            elif self.root.left and self.root.right:
                self.IF_LEFT_AND_RIGHT(self.root)

        #Initialize variable "parent" with value "None", responsible for storing parent of current node
        parent = None
        #Initialize variable "node" with value "self.root", responsible for storing current node
        node = self.root

        #While "node" exists and "node" value not equal to "target" value, execute "while" code block
        while node and node.data != target:
            #Set the "parent" node to the current "node"
            parent = node
            #If "target" value greater than "node" value, set "node" to left child node
            if target < node.data:
                node = node.left
            #Else if "target" value less than "node" value, set "node" to right child node
            elif target > node.data:
                node = node.right

        #Case 1: Target Not Found
        #If "node" is "None" or "node" value not equal to "target" value, return False to caller
        if node is None or node.data != target:
            return False
        
        #Case 2: Target has no Child
        #Else if left child node is "None" and right child node is "None", execute "elif" code block
        elif node.left is None and node.right is None:
            #If "target" value less than "parent" node value, set "parent" left node to "None"
            if target < parent.data:
                parent.left = None
            #Else set "parent" right node to "None"
            else:
                parent.right = None
            #Return "True" to caller
            return True
        
        #Case 3: Target has only left Child
        #Else if left child node exists and right child node is "None", execute "elif" code block
        elif node.left and node.right is None:
            #If "target" value less than "parent" node value, set "parent" left child node to current "node" left child node
            if target < parent.data:
                parent.left = node.left
            #Else set "parent" right child node to current node left child node
            else:
                parent.right = node.left
            #Return "True" to caller    
            return True
        
        #Case 4: Target has only right Child
        #Else if right child node exists and left child node is "None", execute "elif" code block
        elif node.right and node.left is None:
            #If "target" value less than "parent" node value, set "parent" right child node to current node right child node
            if target < parent.data:
                parent.right = node.right
            #Else set "parent" left child node to current node right child node
            else:
                parent.left = node.right
            #Return "True" to caller
            return True

        #Case 5: Target has left and right Child
        #If current node value equal to "target" value, call "IF_LEFT_AND_RIGHT" method with current "node" as argument
        #"IF_LEFT_AND_RIGHT" method handles removal of parent node with left and right child whilst preserving Binary Tree structure
        else:
            self.IF_LEFT_AND_RIGHT(node)

    #!Section End - Implementation of Advanced Algorithms - Advanced 1 Assessed Task

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)

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

#Example calls, which construct and display the binary tree
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
#bst.insert(8)
#bst.insert(9)
#bst.insert(10)
#bst.insert(11)
#bst.insert(12)
#bst.insert(13)
#bst.insert(14)
#bst.insert(15)
#bst.insert(100)
#bst.insert(200)

#Displaying "bst" instance of "BinaryTree" object class using "display" method, before node is removed from "Binary Tree"
bst.display(bst.root)
#Testing iterative remove ("remove") method with value present in "bst" instance of "BinaryTree" object class
bst.remove(3)
#Displaying "bst" instance of "BinaryTree" object class using "display" method, after node is removed from "Binary Tree"
bst.display(bst.root)