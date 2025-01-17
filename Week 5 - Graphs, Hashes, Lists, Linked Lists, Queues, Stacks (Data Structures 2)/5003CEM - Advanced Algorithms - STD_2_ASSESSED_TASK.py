'''Basic BST code for inserting (i.e. building) and printing a tree

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

    '''!Section Start - Implementation of Advanced Algorithms - Standard Assessed Task 2
       !Author: Daniel Mullings
    '''

    '''Define method called "find_i" to iteratively search binary tree to find target value w/ Two parameters:
       Input:  "self" = Instance of "BinaryTree" object the method is called from is the argument, 
               "target" = Value to search for in instance of "BinaryTree" object
       Output: Returns "None" if binary tree is empty, Returns boolean representing state of "target" in binary tree
    '''
    def find_i(self, target):
        cur_node = self.root                                    #Initalise variable "cur_node (Current Node)" with "self.root (Root Node)" of the Binary Tree
        
        if cur_node == None:                                    #If the "cur_node" value is "None"
            return None                                         #Return "None" to caller

        while cur_node != None:                                 #While "cur_node" value is not "None", execute the "while" code block
            if cur_node.data == target:                         #If "cur_node" value equal to "target"
                return True                                     #Return "True" to caller
            elif cur_node.data > target:                        #Else if "cur_node" value greater than "target"
                cur_node = cur_node.left                        #Set "cur_node" to left child node of current node and continue searching in left sub-tree
            else:
                cur_node = cur_node.right                       #Set "cur_node" to right child node of current node and continue searching in right sub-tree
        return False                                            #Return "False" to caller if "cur_node" is not "None" OR "target" value

    '''Define method called "find_r": Implements recursive search of binary tree (Using a recursive sub-method) to find target value w/ Two parameters:
       Input:  "self" = Instance of "BinaryTree" object the method is called from is the argument,
               "target" = Value to search for in instance of "BinaryTree" object
       Output: Returns "None" if binary tree is empty,
               Returns boolean representing state of "target" in binary tree dependent on return value of recursive search method ("_find_r")
    '''
    def find_r(self, target):
        if self.root:                                           #If "self.root" is not "None" (i.e. Exists), execute the "if" code block
            if self._find_r(target, self.root):                 #If "._find_r" sub-method returns "True" after recursively searching instance of object that called method
                                                                #for "target" starting from the "self.root" (Root Node)

                return True                                     #Return "True" to caller
            return False                                        #Otherwise return "False" to caller
        else:                                                   #Else "self.root" is "None" (i.e. Doesn�t exist)
            return None                                         #Return "None" to caller

    '''Define sub-method called "_find_r": Implements recursive search of binary tree to find target value w/ Three parameters:
       Input:  "self" = Instance of "BinaryTree" object the method is called from is the argument, 
               "target" = Value to search for in instance of "BinaryTree" object
       Output: Returns boolean "True" if node value equal to "target" value for each method call in stack
    '''
    def _find_r(self, target, cur_node):
        if target > cur_node.data and cur_node.right:           #If "target" greater than "cur_node" value AND right child node of "cur_node", 
            return self._find_r(target, cur_node.right)         #Recursilvy search for "target" value from right child node of the current node, continuing search in right sub-tree
                                                                #Return resulting return value of sub-method call to caller
        elif target < cur_node.data and cur_node.left:          #Else if "target" less than "cur_node" value AND left child node of "cur_node"
            return self._find_r(target, cur_node.left)          #Recursilvy search for "target" value from left child node of current node, continuing search in left sub-tree
                                                                #Return resulting return value of sub-method call to caller
        if target == cur_node.data:                             #If "target" is equal to the "cur_node" value
            return True                                         #Return "True" to caller
        if cur_node is None:
            return False
    '''!Section End - Implementation of Advanced Algorithms - Standard Assessed Task 2
    '''

bst = BinaryTree()                                              #Example calls, which construct and display the binary tree   
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)

bst.display(bst.root)

print("Is value '7' present in \"bst\" binary tree (Iterative BFS): " + str(bst.find_i(7)))
                                                                #Test/Print return from "find_i (Iterative Find)" method with values present 
print("Is value '8' present in \"bst\" binary tree (Iterative BFS): " + str(bst.find_i(8)) + '\n')
                                                                #and not present in "bst" instance of "BinaryTree" object and print the return value; "True", "False" or "None"

print("Is value '8' present in \"bst\" binary tree (Recursive BFS): " + str(bst.find_r(7)))
                                                                #Test/Print "find_r (Recursive Find)" w/ "_find_r" sub-method method with values present 
print("Is value '8' present in \"bst\" binary tree (Recursive BFS): " + str(bst.find_r(8)) + '\n')
                                                                #and not present in "bst" instance of "BinaryTree" object and print the return value; "True", "False" or "None"