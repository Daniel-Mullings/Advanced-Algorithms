import sys                                                      #Needed for "maxsize"

class Graph():

    def __init__(self, vertices):                               #Implements graph as adjacency matrix
        self.V = vertices                                       #Number of vertices
        self.graph = [[0 for column in range(vertices)]         #Adjacency matrix with no edges (all connections set to zero)
                    for row in range(vertices)]

    def printMST(self, parent):
        print ("Edge \t Weight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

                                                                #From reached nodes find the unreached node with the minimum cost
    def minKey(self, key, mstSet):
        min = sys.maxsize                                       #Set "min" to infinity (Use "maxsize" which is next best thing!)
        for v in range(self.V):                                 #Count through number of vertices
            if key[v] < min and mstSet[v] == False:             #If vertex is less than "min" and unreached
                min = key[v]                                    #Assign to "min"
                min_index = v                                   #"min_index" is position of "min" in "key"
        return min_index                                        #Return "min_index"

                                                                #Find MST
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

                #!Section Start - Implementation of Advanced Algorithms - Standard 4 Assessed Task
                #!Author: Daniel Mullings

                if (self.graph[u][v] > 0                        #If edge from "u" to connected node "v" greater than '0' (If there is an edge)
                    and mstSet[v] == False                      #And "mstSet[v]" is unreached
                    and key[v] > self.graph[u][v]):             #And "key[v]" greater than the edge cost
                    
                                                                #(Only if the current edge cost greater will need to change)
                    key[v] = self.graph[u][v]                   #"key[v]"" takes edge cost

                #!Section End - Implementation of Advanced Algorithms - Standard 1 Assessed Task

                    parent[v] = u                               #"parent[v]" is index of node; so list of parents (nodes) is the MST
        self.printMST(parent)                                   #Print the list of parents, i.e. the MST

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

g.primMST()
