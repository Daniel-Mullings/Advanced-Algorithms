class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def Insert(self, val_before, newdata):
        if val_before is None:
            print("No node to insert after")
            return
        else:

            '''!Section Start - Implementation of Advanced Algorithms - Standard Assessed Task 5
               !Author: Daniel Mullings
            '''

            '''!Finish implementation of method to insert element into linked list
            '''
            insertedNode = Node(newdata)                        #Instantiate instance of "Node" object with "newdata"

            if insertedNode is not None:                        #If "insertedNode" is not equal "None" (i.e. Empty), execute "if" statement code block
                insertedNode.nextval = val_before.nextval       #Set the node after "insertedNode" to the node after the node before ("val_before")                 
                val_before.nextval = insertedNode               #Set the node after the node before (val_before) "insertedNode" to "insertedNode"

                if self.headval == None:                        #If "headval" equal to "None" (i.e. Empty)
                    self.last = insertedNode                    #Set "last" to "instertedNode"
                    self.headval = self.last                    #Set "heaqval" to "last"

            '''!Section End - Implementation of Advanced Algorithms - Standard Assessed Task 5
            '''

list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
list.AtEnd("Sun\n")

list.listprint()
list.Insert(e2, "Weds")                                         #Test "Insert" method with node to insert after ("e2") and value ("Weds) in "list" instance of "SLinkedList" object
list.listprint()