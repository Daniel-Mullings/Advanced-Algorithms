class Graph(object):

    def __init__(self, size):

        self.numberOfVertex = size

        #Adjacency matrix represented using Two Dimensional Array
        self.adjMatrix = []
        for i in range(self.numberOfVertex):
            self.adjMatrix.append([0 for i in range(self.numberOfVertex)])
        print(self.adjMatrix)

    #Methods for (1): Adding a vertex; (2): Adding an edge; (3): Removing an edge; (4) Printing the adjacency matrix

    #!Section Start - Implementation of Advanced Algorithms - Standard 5 Assessed Task
    #!Author: Daniel Mullings

    #Define method called "AddVertex" to add a vertex to the adjacency matrix w/ One parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument
    def AddVertex(self):
        #For each row in adjacency matrix, append an additional element with value '0', representing the vertex's edge connection
        for row in self.adjMatrix:
            row.append(0)
        #Increment "self.numberOfVertex" by '1', representing increased size of adjacency matrix
        self.numberOfVertex += 1
        #Append new row to the adjacency matrix, with amount of elements the equal to "self.numberOfVertex", with the value '0', representing the vertex's edge connection
        self.adjMatrix.append([0] * self.numberOfVertex)

    #Define method called "AddEdge" to add an edges between two vertices within the adjacency matrix w/ Three parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument, 
    #"vertex1" = First vertex in the pair to add an edge between, #"vertex2" = Second vertex in the pair to add an edge between 
    def AddEdge(self, vertex1, vertex2):

        #If "vertex1" greater than "self.numberOfVertex" or "vertex2" greater than "self.numberOfVertex", print message stating vertex pair doesn’t exist in adjacency matrix
        if vertex1 >= self.numberOfVertex or vertex2 >= self.numberOfVertex:
            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Does not exist")
        else:
            #Set value for the edge between two vertices in the adjacency matrix, represented as (2D-Array) to 1 (1 = True (For edge state))
            self.adjMatrix[vertex1 - 1][vertex2 - 1] = 1
            #Set value for the edge between two vertices in the adjacency matrix, represented as (2D-Array) to 1 (1 = True (For edge state)) 
            #(We do this for the mirror of the vertex pair as this adjacency matrix is undirected, unweighted)
            self.adjMatrix[vertex2 - 1][vertex1 - 1] = 1

            #Print message stating vertex pair edge has been added (With vertex pair detailed within message)
            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Edge added")

    #Define method called "RemoveEdge" to add an edges between two vertices within the adjacency matrix w/ Three parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument,
    #"vertex1" = First vertex in the pair to remove an edge between, #"vertex2" = Second vertex in the pair to remove an edge between 
    def RemoveEdge(self, vertex1, vertex2):
        #If "vertex1" greater than "self.numberOfVertex" or "vertex2" greater than "self.numberOfVertex", print message stating vertex pair doesn’t exist in adjacency matrix
        if vertex1 >= self.numberOfVertex or vertex2 >= self.numberOfVertex:
            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Does not exist")
        else:
            #Set value for the edge between two vertices in the adjacency matrix, represented as (2D-Array) to 0 (0 = False (For edge state))
            self.adjMatrix[vertex1 - 1][vertex2 - 1] = 0
            #Set value for the edge between two vertices in the adjacency matrix, represented as (2D-Array) to 0 (0 = False (For edge state)) 
            #(We do this for the mirror of the vertex pair as this adjacency matrix is undirected, unweighted)
            self.adjMatrix[vertex2 - 1][vertex1 - 1] = 0

            #Print message stating vertex pair edge has been removed (With vertex pair detailed within message)
            print("Vertex pair (" + str(vertex1) + ", " + str(vertex2) + "): " + "Edge removed")

    #Define method called "PrintMatrix" to print the adjacency matrix as a grid w/ One parameter
    #"self" = Instance of "Graph" object class the method is called from is the argument
    def PrintMatrix(self):
        
        #Print message displaying title for following adjacency matrix to be printed
        print("\nAdjacency Matrix Output:\n")

        #Initalize variable "colHeadBuffer" with the value '2', responsible for storing the whitespace at the begin of the Adjacency  Matrix grid header labelling columns with associate Vertex 
        colHeadBuffer = 2

        #Initalize variable "rowNum" with the value '1', responsible for storing row vertex label
        rowNum = 1
        #Initalize variable "colNum" with the value '1', responsible for storing column vertex label
        colNum = 1

        #Print message adding whitespace buffer to beginning of column header, "end=""" parameter to prevent newline for subsequent "print()" statement
        print(' ' * colHeadBuffer, end="")

        #For each "vertex" print "colNum", "end=" "" parameter to add whitespace between column header and prevent newline for subsequent "print()" statements
        #"colNum" incremented by '1' for each column header
        for vertex in range(self.numberOfVertex): 
            print(str(colNum), end=" ")
            colNum += 1
        #Empty "print()" statement insert newline for subsequent "print()" statements after using "end=""" parameter
        print()

        #For each "row" in "adjMatrix" print "rowNum" value, "end=" "" parameter to add whitespace between "row" header and "row" content and prevent newline for subsequent "print()" statements
        for row in self.adjMatrix:
            print (str(rowNum), end=" ")
            #For each "edgeVal" in "row" print "edgeVal" value, "end=" "" parameter to add whitespace between each "edgeVal" value and prevent newline for subsequent "print()" statements
            for edgeVal in row:
                print(str(edgeVal), end=" ")
            #"rowNum" incremented by '1' for each row header
            rowNum += 1
            #Empty "print()" statement insert newline for subsequent "print()" statements (Print subsequent "row" in "adjMatrix") after using "end=""" parameter
            print()
        #Empty "print()" statement insert newline for subsequent "print()" statements after using "end=""" parameter
        print()

    #!Section End - Implementation of Advanced Algorithms - Standard 5 Assessed Task

#Remember List indexing - This is 1 out, unless we start the matrix at 0 (Not a postivie Integer)     
def main():
        g = Graph(6)

        #Testing add vertex ("AddVertex") method for 'g' instance of "Graph" object class
        g.AddVertex()

        #Testing add edge ("AddEdge") method with vertex pairs both present and not present in 'g' instance of "Graph" object class
        g.AddEdge(4, 1)
        g.AddEdge(6, 3)
        g.AddEdge(3, 4)
        g.AddEdge(7, 7)

        g.PrintMatrix()

        #Testing remove edge ("RemoveEdge") method with vertex pairs both present and not present in 'g' instance of "Graph" object class
        g.RemoveEdge(4, 1)
        g.RemoveEdge(8, 8)

        #Testing print matrix ("PrintMatrix") method to print adjacency matrix as grid for 'g' instance of "Graph" object class
        g.PrintMatrix()

if __name__ == '__main__':
   main()