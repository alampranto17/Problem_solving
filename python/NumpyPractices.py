import random

import numpy as np
from numpy.ma.core import ravel, concatenate

# # 2d array
# arr=np.array([[1,2,3,4],[3,4,5,6]],dtype=float)
# # complex array
# arr1=np.array([1+2j,2,3,4,5],dtype=complex)
# # bool array
# arr2=np.array([0,1,1,0,1],dtype=bool)

# print(arr)
# print(arr1)
# print(arr2)

# arange
# arr3=np.arange(1,13)
# print(arr3)
#
# arr4=np.arange(1,11,3)
# print(arr4)



# # 3d array convert
# arr3=arr3.reshape(2,2,3)
# print(arr3)

#-------------------- ones ,zeros,identity,random,linespaces-------------------
#
# arr= np.ones((3,3))
# print(arr)
#
# arr6=np.zeros((3,3))
# #
# print(arr6)
#
# arr5=np.random.random((2,3))*100
# print(arr5)
#
# arr4=np.random.randint(0,5,size=(2,3))
#
# print(arr4)
#
# arr3 = np.full((3, 3), 8)
#
# # print(arr)
#
# arr2=np.identity(3, dtype=int)
# print(arr2)
#
# arr1=np.eye(8,3,dtype=int)
# print(arr1)


# Numpy attributes

# dimention
# print(arr3.ndim)
#
# print(arr2.shape)
#
# print(arr3.size)
#
# print(arr3.itemsize)
#
# print(arr3.dtype)
#
# # data type change
#
# arr3=arr3.astype(np.int32)
# print(arr3.dtype)




# if i want to chanage just one coloum value then used this

# data = np.array([(1, 2.5), (3, 4.5)])

# print(f"Original\n {data}")
#
# print(data.ndim)
#
# print(data.shape)
#
# print(data.itemsize)
# print(data.dtype)
# new_datatype=[('col1','float'),('col2','int')]
# data=data.astype(new_datatype)
# # print(data)
# print(data.ndim)

# -----------------arithmethic and indexing and sciling --------------
# data=np.random.randint(0,100,size=(3,3))
# print(f"original\n {data}")
# print(data*2)
# print(data/2)
# print(f"data : {data[:,2]}")
# print(data[:,2]*3)

# -------------------------------vactor-----------------
# data= np.random.rand(2,4)*100
# data1= np.random.rand(2,4)*100

# print("data ", data)


# data=data.astype(np.int32)
# data1=data1.astype(np.int16)
# print(data)
# print(data1)

# data=data/data1
# print(data)
# # ----relational-----
# # data=data>1
# # print(data)
#
# data= data[data<1]
# print (data)

# -------------sum/min/max/meen/prod/medim/std/var--------------

# print("Sum : ",np.sum(data))
# print("Min : ",np.min(data))
# print("Max : ",np.max(data))
# print("Mean : ",np.mean(data))
# print("Product : ",np.prod(data))
# print("medim : ",np.median(data))
# print("std : ",np.std(data))
# print("var : ",np.var(data))

# --------axis----------------(column =0,row=1)
# print("Sum of column 0 : ",np.sum(data,axis=0))
#
# print("Sum of row 1 : ",np.sum(data,axis=1))
#
# print("Min of column 0 : ",np.min(data,axis=0))
# print("Min of row 1 : ",np.min(data,axis=1))
#
#
# print("Max of column 0 : ",np.max(data,axis=0))
# print("Max of row 1 : ",np.max(data,axis=1))
#
# print("Mean of column 0 : ",np.mean(data,axis=0))
# print("Mean of row 1 : ",np.mean(data,axis=1))


# ---------------indexing and slicing---------------
#
# a2=np.random.randint(1,100, size=(3,3))
# print(a2)
#
# # find row 3 and column 3 value
# print(a2[2,2])

# # 3d
# a3=np.random.randint(1,100, size=(2,3,3))
#
# print(a3)
#
# # find 1st matrix 2 row 2nd value
#
# print(a3[0,1,1])
#
# print(a3[1, 0::2, 0::2])

# a=np.arange(27).reshape(3,3,3)
# print(a)
#
# print(a[::2,0,0::2])
# j=0
# ----------iteration-----------

# for i in a:
#     j+=1
#     print(j,". 2d \n",i)
#
# for i in np.nditer(a):
#     if(i==np.size(a)-1):
#         print(i)
#         break
#
#     print(i,end=" , ")

# ---------------------reshape/transpose/ravel---------
# a1=np.ceil(np.random.random((3,2))*100)
# a1=a1.astype(np.int16)
# print("original : \n",a1)
# print()
# a2=a1.reshape(2,3)
# print(np.dot(a1,a2))
#
# print(np.transpose(a1))
#
# print(np.ravel(a1))

# ----------sigmoind/meanSquareError/-------------------

# def sigmoid(array):
#     return 1/(1+np.exp(-(array)))

# a=np.arange(-10,11)
# sigmoid_output = sigmoid(a)
#
# # Boolean রূপান্তর
# bool_output = sigmoid_output >= 0.5
#
# print("Sigmoid Output:\n", sigmoid_output)
# print("\nBoolean Output:\n", bool_output)


# ----

# def meanSquareError(a1,a2):
#     difference=(a1-a2)**2
#
#
#
#     totalDifference=np.sum(difference)
#     return (totalDifference)/np.size(a1)
# a1=np.random.randint(1,50,25)
# a2=np.random.randint(1,50,25)
# print("Value of actual : ",a1)
# print("Value of prediction : ",a2)
#
# mse=meanSquareError(a1,a2)
#
# print("value of mase : ",mse )

#-------------stack and slipt-------------------

# a=np.random.randint(1,100,(5,2))
# # print(a)
#
# b=np.random.randint(1,100,(5,2))
# #
# # print(b)
#
# # c=np.hstack((a,2))
# # print(c)
# c,d=np.hsplit(a,2)
# print(c)
# print(d)



# b = np.random.randint(1, 100, (6, 3))
# print("Original array:\n", b)
#
# f, e = np.vsplit(b, 2)
#
# print("\nFirst part (c):\n", f)
# print("\nSecond part (d):\n", e)


# _____________________________-advance part__________________________
# ---missing value handle
# a=np.array([1,2,3,4,np.nan,5,6],dtype=float)
# print(a)
# # print(a[~np.isnan(a)])
# a[np.isnan(a)]=0
# print(a)

# --------------graph----------------
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Agg')  # For non-GUI environments
#
#
# x=np.linspace(-10,10,10)
# y=sigmoid(x)
# plt.plot(x,y)
# plt.savefig("sigmoid_plot.png")

# -----------------------------------------------numpy tricks----------------
#----------sort------
# a=np.array([8,5,7,8,9])
# b=np.random.randint(1,10 ,size=(3,3))
#
# print("Original array : ",a,"\n")
# print("Original 2D array : \n",b,"\n")


# print("Acending order ",np.sort(a))
# print("decending  order ",np.sort(a)[::-1])
# print("2d short by row : \n",np.sort(b,axis=1))

#-----append--------
## shape must be same.
# print(np.append(a,200))
# print(np.append(b,np.full((3,1),8),axis=1)) #column add 8
#
# print(np.append(b,np.array([1,1,1]).reshape(1,3),axis=0)) #row add 1



# ----------------concatenate----------------
# c=np.arange(0,9).reshape(3,3)
#
#
#
#
# print(np.concatenate((b,c),axis=0))

# --------unique------

# print(np.unique(b))
#
# #----where------
# # sql er moto kaj kore condition niye kaj kore
# # print(np.where(a>5))
# print(np.where((a>5),a,0))
# print(np.where((b>5),b,0))


# -----------cumsum() cumprod()------------
# print(np.cumsum(a))
#
# print(np.cumprod(a))
#
# print(np.cumsum(b,axis=0))
#
# print(np.cumsum(b,axis=1))

#---------percentile--------

# print(np.percentile(a,50))



#---------histogram----------as numpy

# a=np.random.randint(1,100,50)
#
# print(a)
#
# print(np.histogram(a,bins=[0,20,40,60,80,100]))

# ------showing as matplot------
# import matplotlib.pyplot as plt
#
# plt.hist(a,bins=[0,20,40,60,80,100],edgecolor="Blue")
#
# plt.title("Randow data show as histogram")
# plt.xlabel("Bins")
# plt.ylabel("Counts ")
# plt.savefig("histogram.png")

# ------problem solve numpy-----------------



# quenstion 1


a=np.arange(0,12).reshape(3,4)
print(a)

print("shape : ",np.shape(a))
print("Size of : ",np.size(a))
print("Dimention ",np.ndim(a))
print(a.dtype)

# quenstion 2

print(a[1,:],"\n")

print(a[::,0:3:2],"\n")

print(a[1::,1:3:],"\n")

#question 3

b=np.random.randint(1,100,50)

print(b)

print(np.where(b>50))
print(b[b>50])

# question 4

c=np.arange(25).reshape(5,5)

print(c,"\n")

print(c[[0,2,4]],"\n")
print(c[:,[1,3]],"\n")
print(c[[0,2,4]][:,[1,3]],"\n")

# ------------bonus---------
# complex using try this
# bouns
# print(c[np.ix_([0,2,4],[1,3])])

# question 5

add=c+5
print(add,"\n")

print(c*2,"\n")

print(c**2,"\n")

# question 6

print(np.sum(c))
print(np.cumsum(c))
print(np.max(c,axis=0))
print(np.mean(c,axis=1))

# question 7


d=np.random.randint(1,16,16)
print(d)
d=np.reshape(d,(4,4))
print(d)

# question 8

e=np.arange(1,10).reshape(3,3)
f=np.arange(11,20).reshape(3,3)

print(e)
print(f)

print(np.vstack((e,f)))

print(np.hstack((e,f)))

q=np.hstack((e,f))

print(np.hsplit(q,2))

# question 9

a=np.array([1,2,3])

h=e+a
print(h)

# question 10

ra=np.random.randint(1,101,100)

print(np.percentile(ra,25))
print(np.percentile(ra,50))
print(np.percentile(ra,75))

print(np.histogram(ra,bins=[0,25,50,75,100]))









