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

""" BST class with insert and display methods. display pretty prints the tree """
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

    #Define method called "find_i" to iteratively search Binary Tree to find target value w/ Two parameters:
    #"self" = Instance of "BinaryTree" object class the method is called from is the argument, "target" = Value to search for in instance of "BinaryTree" object class
    def find_i(self, target):

        #Set the "cur_node" (Current Node) value to the "Root Node" of the Binary Tree
        cur_node = self.root

        #If the "cur_node" value is "None", return "None" to caller
        if cur_node == None:
            return None

        #While the "cur_node" value is not "None", execute the "while" code block
        while cur_node != None:

            #If the "cur_node" value is equal to "target" value, return "True" to caller
            if cur_node.data == target:
                return True
            
            #Else if the "cur_node" value greater than "target" value
            #Set the "cur_node" value to the left child node of the current node and continue searching in left sub-tree
            elif cur_node.data > target:
                cur_node = cur_node.left
            
            # Else set the "cur_node" value to the right child node of the current node and continue searching in right sub-tree
            else:
                cur_node = cur_node.right

        #Return "False" to caller if "cur_node" value is not "None" OR "target" value
        return False

    #Define method called "find_r" to recursively search Binary Tree (Using a recursive sub-method) to find target value w/ Two parameters:
    #"self" = Instance of "BinaryTree" object class the method is called from is the argument, "target" = Value to search for in instance of "BinaryTree" object class
    def find_r(self, target):
        #If "self.root" value is not "None" (i.e. Exists), exexute the "if" code block
        if self.root:
            #If "._find_r" sub-method returns "True" after recursively searching instance of "BinaryTree" object class for "target" value starting from the "self.root" (Root Node), 
            #Return "True" to caller, otherwise return "False" to caller
            if self._find_r(target, self.root):
                return True
            return False

        #Else "self.root" is "None" (i.e. Dosen't exist), return "None" to caller
        else:
            return None

    #Define sub-method called "_find_r" to recursively search Binary Tree to find target value w/ Three parameters:
    #"self" = Instance of "BinaryTree" object class the method is called from is the argument, "target" = Value to search for in instance of "BinaryTree" object class, 
    #"cur_node" = Current Node we are at within Binary Tree
    def _find_r(self, target, cur_node):
        #If the "target" value greater than the "cur_node" value AND the right child node of the "cur_node", 
        #Recursilvy search for the "target" value from the right child node of the current node, continuing the search in the right sub-tree
        #Return the resulting return value of that sub-method call to caller
        if target > cur_node.data and cur_node.right:
            return self._find_r(target, cur_node.right)
        
        #Else if the "target" value less than the "cur_node" value AND the left child node of the "cur_node", 
        #Recursilvy search for the "target" value from the left child node of the current node, continuing the search in the left sub-tree
        #Return the resulting return value of that sub-method call to caller
        elif target < cur_node.data and cur_node.left:
            return self._find_r(target, cur_node.left)
        
        #If the "target" value is equal to the "cur_node" value, return "True" to caller
        if target == cur_node.data:
            return True

#Example calls, which construct and display the tree       
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

bst.display(bst.root)

#Testing iterative find ("find_i") method with values both present and not present in "bst" instance of "BinaryTree" object class and print the return value; "True", "False" or "None", 
#Dependent on value presence in Binary Tree ("bst" instance of "BinaryTree" object class)
print("Is value '7' present in \"bst\" object insance of \"Binary Tree\": " + str(bst.find_i(7)))
print("Is value '8' present in \"bst\" object insance of \"Binary Tree\": " + str(bst.find_i(8)) + '\n')

#Testing recursive find ("find_r" w/ "_find_r" sub-method) method with values both present and not present in "bst" instance of "BinaryTree" object class and print the return value; "True", "False" or "None", 
#Dependent on value presence in Binary Tree ("bst" instance of "BinaryTree" object class)
print("Is value '7' present in \"bst\" object insance of \"Binary Tree\": " + str(bst.find_r(7)))
print("Is value '8' present in \"bst\" object insance of \"Binary Tree\": " + str(bst.find_r(8)) + '\n')