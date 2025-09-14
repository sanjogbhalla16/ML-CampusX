#List vs Array
import sys
import numpy as np
import time

lista = range(100)
arr11 = np.arange(100)

print(sys.getsizeof(5)*len(lista))  #size of list
print(arr11.size*arr11.itemsize)    #size of array

#time taken by list
x=range(10000000) #both have 100000 elements
y=range(10000000,20000000)

#now we zip each element of both list and add them
start_time = time.time()

c=[(a+b) for a,b in zip(x,y)]

print("Time taken by list: ",(time.time()-start_time))

#time taken by array
x1 = np.arange(10000000)
y1 = np.arange(10000000,20000000)

start_time = time.time()
c1 = x1+y1
print("Time taken by array: ",(time.time()-start_time))