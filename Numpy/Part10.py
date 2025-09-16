import numpy as np

arr1 = np.random.randint(low=1,high=100,size=20).reshape(4,5)
print(arr1)

print(arr1>50) #boolean array

#indexing with boolean array
print(arr1[(arr1>50) & (arr1%2!=0)])  #odd numbers greater than 50