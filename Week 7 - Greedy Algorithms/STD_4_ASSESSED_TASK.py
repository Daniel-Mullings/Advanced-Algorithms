import sys                                                      #Import "sys" for "maxsize"

class Graph():
    #Initialzie new instance of "Graph" object class, implements graph as adjacency matrix (Two-Dimensional Array) w/ Two parameters
    #"self" = Instance of "Graph" object class the method is called from is the argument, "vertices" = Number of vertices in adjacency matrix
    def __init__(self, vertices):
        self.V = vertices                                       #Number of vertices
        self.graph = [[0 for column in range(vertices)]         #Adjacency matrix with no edges (All connections set to '0')
                    for row in range(vertices)]

    #Define method called "printMST" to print formatted MST w/ Two parameters
    #"self" = Instance of "Graph" object class the method is called from is the argument, "parent" = Parent of node
    def printMST(self, parent):
        print ("Edge \t Weight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

    #Define method called "minKey" from reached node find unreached with minimum cost w/ Three parameters
    #"self" = Instance of "Graph" object class the method is called from is the argument, "key" = Weight of edge connecting Vertex to existing MST, 
    #"mstSet" = Boolean stores status of nodes addition to MST
    def minKey(self, key, mstSet):
        min = sys.maxsize                                       #Set "min" to infinity (Use "maxsize" which is next best thing!)
        for v in range(self.V):                                 #For each vertex in instance of object class that called method
            if key[v] < min and mstSet[v] == False:             #If vertex less than "min" and unreached
                min = key[v]                                    #Set "min" to vertex
                min_index = v                                   #"min_index" is position of "min" in "key"
        return min_index                                        #Return "min_index" to caller

    #Define method called "primMST" to find MST (Minimum Spanning Tree) w/ One parameters:
    #"self" = Instance of "Graph" object class the method is called from is the argument
    def primMST(self):
        key = [sys.maxsize] * self.V                            #Initialise "key" to List of values all set to infinity; same length as "self.V"
        parent = [None] * self.V                                #List for constructed MST
        key[0] = 0                                              #Set first element of "key" to '0' (This is where we start)
        mstSet = [False] * self.V                               #"mstSet" is List of Booleans set to "False"
        parent[0] = -1                                          #First element of parent list set to '-1'

        for vertex in range(self.V):                            #Go through all vertices
            u = self.minKey(key, mstSet)                        #Call "minKey"; "minKey" returns 'u' (Index of unreached node)
            mstSet[u] = True                                    #"mstSet" at index of node is set to "True"
            for v in range(self.V):                             #Go through all vertices

                #!Section Start - Implementation of Advanced Algorithms - Standard Assessed Task 4
                #!Author: Daniel Mullings
                if (self.graph[u][v] > 0                        #If edge 'u' to connected node 'v' is greater than '0' (If there is an edge)
                    and mstSet[v] == False                      #And "mstSet[v]" is unreached
                    and key[v] > self.graph[u][v]):             #And "key[v]"" is greater than the edge cost
                    key[v] = self.graph[u][v]                   #Set "key[v]" to edge cost (Only if the current edge cost is greater will need to change)
                #!Section End - Implementation of Advanced Algorithms - Standard Assessed Task 4

                    parent[v] = u                               #"parent[v]" is index of node; so List of parents (Nodes) is the MST
        self.printMST(parent)                                   #Print List of parents, i.e. the MST

g = Graph(5)                                                    #Initalise instance of object class "Graph" called 'g', with 5 vertices in adjacency matrix
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]                                    #Define weights for each vertex pair edge in adjacency matrix (Two-Dimensional Array)
g.primMST()                                                     #Find MST of "g" instance of "Graph" object class using "primMST" method