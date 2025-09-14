#creating numpy/n-d arrays
import numpy as np

#1-d array
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))

# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)
# print(type(arr2))

#tuple to array
# arr3 = np.zeros((2,3))
# print(arr3)

# arr4 = np.ones((3,4))
# print(arr4)

# arr5 = np.identity(4)
# print(arr5)

# arr6 = np.arange(1,10,2)
# print(arr6)

arr7 = np.linspace(1,10,5)
print(arr7)

arr8 = arr7.copy()
print(arr8)