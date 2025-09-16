import numpy as np
# Reshape Numpy Arrays
arr3=np.arange(6).reshape(2,3)
arr4=np.arange(6,12).reshape(3,2)

print(arr3)
#print(arr4)

#print(arr4.ndim)

arr5 = np.arange(12,18).reshape(2,3)
# print(arr5)

ans = np.hstack((arr3,arr5))  #horizontal stacking
# print(ans)

ans2 = np.vstack((arr3,arr5))  #vertical stacking
# print(ans2)


#splitting of numpy arrays horizontally and vertically
arr6 = np.hsplit(arr3,3)  #horizontal splitting
print(arr6)

arr7 = np.vsplit(arr3,2)  #vertical splitting
print(arr7)