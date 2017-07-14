#FUNCTIONS

def bubbleSort(lissy):
   for index in range(len(lissy)-1,0,-1):
      for index2 in range(index):
         if (lissy[index2] > lissy[index2+1]):
            num = lissy[index2]
            lissy[index2] = lissy[index2+1]
            lissy[index2+1] = num
      

def binSearch(lissy, num):
    first = 0
    last = len(lissy)-1
    found = False


    while(first<=last) and not found:
       mid = (first+last)//2
       if (lissy[mid] == num):
          found = True
       else:
            if (num<lissy[mid]):
               last = mid-1
            else:
               first = mid+1
    return found
      


    
   

#RUNNING CODE
myList = [19, 0, 45, 9, 67, 2, 100, 30]
bubbleSort(myList)
#print(myList)    
print(binSearch(myList, 8))
print(binSearch(myList, 0))
