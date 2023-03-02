'''Section Start - Implementation of Advanced Algorithms - Standard Assessed Task 1
   Author: Daniel Mullings
'''
A = [11, 22, 14, 67, 2, 9]                                      #Initialise List 'A' with 6 unsorted integer values

'''Define function called "Selection_Sort": Implements selection sort for Lists w/ One parameters:
   Input:  "listToSort" = Unsorted List to be sorted
   Output: Returns sorted List "listToSort", Modifies List passed by reference as argument
'''
def SelectionSort(listToSort):
    for x in range(len(listToSort) - 1):                        #Loop over List from beginning to end (-1 as index start at 0)
        minn = x                                                #Assume 'x'-th element is the smallest in the unsorted List
        for y in range(x + 1, len(listToSort)):                 #Loop over the rightmost elements of 'x'-th element
            if listToSort[y] < listToSort[minn]:                #If any 'y'-th element less than the 'x'-th element
                minn = y                                        #Set "minn" to store the 'y'-th element
        Swap(listToSort, x, minn)                               #Swap "minn"-th element with 'x'-th element in unsorted List
    return listToSort                                           #Return sorted List to caller

'''Define function called "Swap": Implement swap of two elements in a List w/ Three parameters:
   Input: "listToSort" = Unsorted List to be sorted, 'x' = 'x'-th element currently at in List to be sorted,
          "minn" = "minn"-th element containing smallest value in unsorted section of List
   Output: No return, List with two element values swapped
'''
def Swap(listToSort, x, minn):
    x_temp = listToSort[x]                                      #Set "x_temp" to 'x'-th element in “listToSort”
    listToSort[x] = listToSort[minn]                            #Overwrite 'x'-th element with value of "minn"-th element
    listToSort[minn] = x_temp                                   #Overwrite "minn"-th element with value of "x-temp"-th element

print("Unsorted List    : " + str(A))                           #Print the unsorted list
print("Sorted List      : " + str(SelectionSort(A)))            #Test/Print return from "SelectionSort", testing function with unsorted List ('A', List of integer values)

'''!Section End - Implementation of Advanced Algorithms - Standard Assessed Task 1
'''