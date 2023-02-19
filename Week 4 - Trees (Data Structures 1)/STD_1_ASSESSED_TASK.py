#!Section Start - Implementation of Advanced Algorithms - Standard 1 Assessed Task
#!Author: Daniel Mullings

#Initalize List 'A' with 6 unsorted integer values
A = [11, 22, 14, 67, 2, 9]

#Define function called "Selection_Sort" to sort Lists (Smallest to Largest) w/ One parameter:
#"listToSort" = Unsorted List to be sorted
def Selection_Sort(listToSort):
    #Loop over List from beginning to end (-1 from the List length as List is indexed from 0)
    for i in range(len(listToSort) - 1):
        #Assume 'i'-th element is the smallest in the unsorted List
        minn = i
        #Loop over the remaining elements of the List that appear after the 'i'-th element
        for j in range(i + 1, len(listToSort)):
            #If any 'j'-th element in the unsorted list after the 'i'-th element less than the 'i'-th element, then update "minn" to store the 'j'-th element
            if listToSort[j] < listToSort[minn]:
                minn = j
        #Call funtion "Swap" to swap the smallest element, "minn"-th with the first element, 'i'-th in the unsorted List
        Swap(listToSort, i, minn)
    #Return sorted list to caller
    return A

#Define function called "Swap" to swap of two elements in a List w/ Three parameters:
#"listToSort" = Unsorted List to be sorted, 'i' = 'i'-th element currently at in List to be sorted, 
#"minn" = "minn"-th element containing smallest value in unsorted section of List
def Swap(listToSort, i, minn):
    #Store 'i'-th element in variable called "i_temp"
    i_temp = listToSort[i]
    #Overwrite 'i'-th element with value of "minn"-th element
    listToSort[i] = A[minn]
    #Overwrite "minn"-th element with value of "i-temp"-th element
    listToSort[minn] = i_temp

#Printing unsorted List before being sorted using "Selection_Sort" function
print(A)

#Testing selection sort ("Selection_Sort") function with an unsorted List ('A', List of integer values) and print the return value, sorted List ('A', List of sorted values)
print(Selection_Sort(A))

#!Section End - Implementation of Advacned Algorithms - Standard 1 Assessed Task