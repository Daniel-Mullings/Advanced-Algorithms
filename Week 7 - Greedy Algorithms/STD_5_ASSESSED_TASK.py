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

            #!Section Start - Implementation of Advanced Algorithms - Standard 5 Assessed Task
            #!Author: Daniel Mullings

            #Initialize instance of "Node" object class with "newdata"
            insertedNode = Node(newdata)

            #If "insertedNode" is not equal "None" (i.e. Empty), execute "if" statement code block
            if insertedNode is not None:
                #Set the node after "insertedNode" to the node after the node before ("val_before") 
                insertedNode.nextval = val_before.nextval
                #Set the node after the node before (val_before) "insertedNode" to "insertedNode"
                val_before.nextval = insertedNode

                #If "headval" is equal to '0' (i.e. Empty), set "last" to "instertedNode" and set "heaqval" to "last"
                if self.headval == 0:
                    self.last = insertedNode
                    self.headval = self.last

                #Else if "last" is equal to "val_before.nextval", set "last" to "insertedNode"
                elif self.last == val_before.nextval:
                    self.last = insertedNode
        
            #!Section End - Implementation of Advanced Algorithms - Standard 5 Assessed Task

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

list.AtEnd("Sun")

#
list.Insert(e2, "Weds")

list.listprint()