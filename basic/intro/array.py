from array import *

arr1=array('i',[1,2,3,4,5])
arr2=array('i',arr1.tolist())

arr1[4]=7
print(arr1)
print(arr2) 
