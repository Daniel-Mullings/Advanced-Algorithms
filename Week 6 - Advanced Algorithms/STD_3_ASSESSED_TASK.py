class Graph(object):

    def __init__(self, size):

        self.numberOfVertex = size

        #Adjacency matrix represented using Two-Dimensional Array
        self.adjMatrix = []
        for i in range(self.numberOfVertex):
            self.adjMatrix.append([0 for i in range(self.numberOfVertex)])
        print(self.adjMatrix)

    #Methods for (1): Adding a vertex; (2): Adding an edge; (3): Removing an edge; (4) Printing the adjacency matrix

    #!Section Start - Implementation of Advanced Algorithms - Standard Assessed Task 3
    #!Author: Daniel Mullings

    #Define method called "AddVertex" to add a vertex to the adjacency matrix w/ One parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument
    def AddVertex(self):
        for row in self.adjMatrix:                              #For each row in adjacency matrix
            row.append(0)                                       #Append an additional element with value '0', representing the vertex's edge connection
        self.numberOfVertex += 1                                #Increment "self.numberOfVertex" by '1', representing increased size of adjacency matrix
        self.adjMatrix.append([0] * self.numberOfVertex)        #Append new row to the adjacency matrix, with amount of elements the equal to "self.numberOfVertex",
                                                                #with the value '0', representing the vertex's edge connection

    #Define method called "AddEdge" to add an edges between two vertices within the adjacency matrix w/ Three parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument, 
    #"vertex1" = First vertex in the pair to add an edge between, #"vertex2" = Second vertex in the pair to add an edge between 
    def AddEdge(self, vertex1, vertex2):

        
        if vertex1 >= self.numberOfVertex or vertex2 >= self.numberOfVertex:
                                                                #If "vertex1" greater than "self.numberOfVertex" or "vertex2" greater than "self.numberOfVertex"
            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Does not exist")
                                                                #Print message stating vertex pair doesn’t exist in adjacency matrix
        else:
            self.adjMatrix[vertex1 - 1][vertex2 - 1] = 1        #Set value for the edge between two vertices in the adjacency matrix, represented as (2D-Array) to 1 (1 = True (For edge state))
            self.adjMatrix[vertex2 - 1][vertex1 - 1] = 1        #(We do this for the mirror of the vertex pair as this adjacency matrix is undirected, unweighted)

            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Edge added")
                                                                #Print message stating vertex pair edge has been added (With vertex pair detailed within message)

    #Define method called "RemoveEdge" to add an edges between two vertices within the adjacency matrix w/ Three parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument,
    #"vertex1" = First vertex in the pair to remove an edge between, #"vertex2" = Second vertex in the pair to remove an edge between 
    def RemoveEdge(self, vertex1, vertex2):
        if vertex1 >= self.numberOfVertex or vertex2 >= self.numberOfVertex:
                                                                #If "vertex1" greater than "self.numberOfVertex" or "vertex2" greater than "self.numberOfVertex"
            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Does not exist")
                                                                #Print message stating vertex pair doesn’t exist in adjacency matrix
        else:
            self.adjMatrix[vertex1 - 1][vertex2 - 1] = 0        #Set value for the edge between two vertices in the adjacency matrix, represented as (2D-Array) to 0 (0 = False (For edge state))
            self.adjMatrix[vertex2 - 1][vertex1 - 1] = 0        #(We do this for the mirror of the vertex pair as this adjacency matrix is undirected, unweighted)

            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Edge removed")
                                                                #Print message stating vertex pair edge has been removed (With vertex pair detailed within message)

    #Define method called "PrintMatrix" to print the adjacency matrix as a grid w/ One parameter
    #"self" = Instance of "Graph" object class the method is called from is the argument
    def PrintMatrix(self):
        print("\nAdjacency Matrix Output:\n")                   #Print message displaying title for following adjacency matrix to be printed

        colHeadBuffer = 2                                       #Initalise variable "colHeadBuffer" with the value '2', 
                                                                #responsible for storing the whitespace at the begin of the Adjacency Matrix grid header labelling columns with associate Vertex 

        rowNum = 1                                              #Initalise variable "rowNum" with the value '1', responsible for storing row vertex label
        colNum = 1                                              #Initalise variable "colNum" with the value '1', responsible for storing column vertex label

        print(' ' * colHeadBuffer, end="")                      #Print message adding whitespace buffer to beginning of column header, 
                                                                #"end=""" parameter to prevent newline for subsequent "print()" statement

        for vertex in range(self.numberOfVertex):               #For each "vertex" in instance of object class that called method
            print(str(colNum), end=" ")                         #Print "colNum", "end=" "" parameter to add whitespace between column header and prevent newline for subsequent "print()" statements
            colNum += 1                                         #"colNum" incremented by '1' for each column header
        print()                                                 #Empty "print()" statement insert newline for subsequent "print()" statements after using "end=""" parameter

        for row in self.adjMatrix:                              #For each "row" in "adjMatrix"
            print (str(rowNum), end=" ")                        #Print "rowNum" value, 
                                                                #"end=" "" parameter to add whitespace between "row" header and "row" content and prevent newline for subsequent "print()" statements
             
            for edgeVal in row:                                 #For each "edgeVal" in "row"
                print(str(edgeVal), end=" ")                    #Print "edgeVal" value, 
                                                                #"end=" "" parameter to add whitespace between each "edgeVal" value and prevent newline for subsequent "print()" statements
            rowNum += 1                                         #"rowNum" incremented by '1' for each row header
            
            print()                                             #Empty "print()" statement insert newline for subsequent "print()" statements 
                                                                #(Print subsequent "row" in "adjMatrix") after using "end=""" parameter
        print()                                                 #Empty "print()" statement insert newline for subsequent "print()" statements after using "end=""" parameter
    #!Section End - Implementation of Advanced Algorithms - Standard Assessed Task 3

#Remember List indexing - This is 1 out, unless we start the matrix at 0 (Not a postivie Integer)     
def main():
        g = Graph(6)
        
        g.PrintMatrix()                                         #Test "PrintMatrix" method to print adjacency matrix as grid for 
                                                                #'g' instance of "Graph" object class (Before changes made to adjacency matrix using methods)
  
        g.AddVertex()                                           #Test "AddVertex" method for 'g' instance of "Graph" object class

        g.AddEdge(4, 1)                                         #Test "AddEdge" method with vertex pairs both present 
        g.AddEdge(8, 8)                                         #and not present in 'g' instance of "Graph" object class
        g.AddEdge(6, 3)
        g.AddEdge(3, 4)

        g.PrintMatrix()
        
        g.RemoveEdge(4, 1)                                      #Test "RemoveEdge" method with vertex pairs both present 
        g.RemoveEdge(8, 8)                                      #and not present in 'g' instance of "Graph" object class

        
        g.PrintMatrix()                                         #Test "PrintMatrix" method to print adjacency matrix as grid for 
                                                                #'g' instance of "Graph" object class (After changes made to adjacency matrix using methods)

if __name__ == '__main__':
   main()