#Numpy Operations
import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])
#print(arr1-arr2)
#print(arr1*arr2)
#print(arr2>3)  #gives boolean array
#print(arr1%2==0) #boolean array for even numbers

arr3=np.arange(6).reshape(2,3)
arr4=np.arange(6,12).reshape(3,2)

#print(arr3)
print(arr4)

#print(np.dot(arr3,arr4))  #matrix multiplication

print(arr4.min())
print(arr4.max())
print(arr4.sum())
print(arr4.min(axis=0))  #column wise min
print(arr4.min(axis=1))  #row wise min
print(arr4.max(axis=0))  #column wise max  
print(arr4.max(axis=1))  #row wise max
print(arr4.sum(axis=0))  #column wise sum
print(arr4.sum(axis=1))  #row wise sum  
print(arr4.mean())  #mean of all elements
print(arr4.mean(axis=0)) #column wise mean  
print(arr4.mean(axis=1)) #row wise mean
print(np.sqrt(arr4))  #square root of each element
print(np.std(arr4))   #standard deviation