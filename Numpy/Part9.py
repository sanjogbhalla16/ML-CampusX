import numpy as np

arr1 = np.arange(24).reshape(6,4)
print(arr1)

print(arr1[[0,2,4]])  #selecting specific rows
print(arr1[:,[1,2]])  #selecting specific rows and columns