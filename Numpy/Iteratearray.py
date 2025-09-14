#we will see indexing,slicing and iterating in numpy array
import numpy as np
arr1 = np.array([1,2,3,4,5])
# print(arr1[0])  #indexing
# print(arr1[0:4]) #slicing
# for i in arr1:   #iterating
    # print(i)
    
#reshape of our array
arr2=np.arange(24).reshape(6,4)
print(arr2)

#because we need all the rows and only 2nd column
print(arr2[:,2])  #slicing in 2-d array

print(arr2[1:4,2]) #1 to 3 rows and 2nd column