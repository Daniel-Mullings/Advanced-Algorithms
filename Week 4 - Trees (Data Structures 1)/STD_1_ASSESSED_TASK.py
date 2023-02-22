'''Section Start - Implementation of Advanced Algorithms - Standard Assessed Task 1
   Author: Daniel Mullings
'''
A = [11, 22, 14, 67, 2, 9]                                      #Initialise List 'A' with 6 unsorted integer values

'''Define function called "Selection_Sort": Implements selection sort for Lists w/ One parameters:
   Input:  "listToSort" = Unsorted List to be sorted
   Output: Return sorted List
'''
def SelectionSort(listToSort):
    for i in range(len(listToSort) - 1):                        #Loop over List from beginning to end (-1 from the List length as List is indexed from 0)
        minn = i                                                #Assume 'i'-th element is the smallest in the unsorted List
        for j in range(i + 1, len(listToSort)):                 #Loop over the remaining elements of the List that appear after the 'i'-th element
            if listToSort[j] < listToSort[minn]:                #If any 'j'-th element in the unsorted list after the 'i'-th element less than the 'i'-th element
                minn = j				                        #Set "minn" to store the 'j'-th element
        #Swap(listToSort, i, minn)                               #Swap smallest element ("minn"-th) with first element ('i'-th) in unsorted List
        listToSort[i], listToSort[minn] = listToSort[minn], listToSort[i] 
    return listToSort                                           #Return sorted List to caller

'''Define function called "Swap": Implement swap of two elements in a List w/ Three parameters:
   Input: "listToSort" = Unsorted List to be sorted, 'i' = 'i'-th element currently at in List to be sorted,
          "minn" = "minn"-th element containing smallest value in unsorted section of List
   Output: No return, List with two element values swapped
'''
def Swap(listToSort, i, minn):
    i_temp = listToSort[i]                                      #Set "i_temp" to 'i'-th element in “listToSort”
    listToSort[i] = listToSort[minn]                            #Overwrite 'i'-th element with value of "minn"-th element
    listToSort[minn] = i_temp                                   #Overwrite "minn"-th element with value of "i-temp"-th element

print("Unsorted List: " + str(A))                               #Print unsorted List
print("Sorted List  : " + str(SelectionSort(A)))                #Test/Print return from "SelectionSort", testing function with unsorted List ('A', List of integer values)
'''!Section End - Implementation of Advanced Algorithms - Standard Assessed Task 1
'''