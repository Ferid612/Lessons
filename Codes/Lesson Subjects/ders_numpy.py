# pip install numpy
import numpy as np

# list, tupple ,set, dict 

# print(np.__version__)

# arr = np.array([1, 2, 3, 4, 5])


# index 
# type
# print(arr)
# print(arr[0])
# print(arr[-1])
# print(arr[2:])

# print(type(arr))




# arr = np.array(42)
# print(arr)
# print(type(arr))


# arr = np.array(2)
# arr = np.array([1, 2, 3, 4, 5])
# arr = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
# arr = np.array([[[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]])


# 2D array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print()


# # 3D array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)





# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3, 4], [4, 5, 6, 8]])
# d = np.array([[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]],[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]])

# print(a.ndim)  # 0
# print(b.ndim)  # 1
# print(c.ndim)  # 2
# print(d.ndim)  # 3



# Coxlu D
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)                         # [[[[[1 2 3 4]]]]]
# print('Boyut sayısı:', arr.ndim)   # 5


# index
# arr = np.array([1, 2, 3, 4])
# print(arr[0])  # 1


# arr = np.array([[1, 2, 3, 4], [4, 5, 6, 8]])
# print(arr[0,2])



# arr = np.array([[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]], 
#                 [[1,2,3,4,5], [6,7,8,9,123],[11,12,13,14,15]]
#                 ,[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]]])
# print(   arr[1,1,4]   )

#3D Index


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

# minus index
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])



# slice

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, ::])   # [7 8 9]


#! Data Types in NumPy

# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer i4 
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )




# arr = np.array(['1', '2', '3'], dtype='i2')
# arr_2 = np.array(['1', '2', '3'], dtype='i4')
# print(arr)  
# print(arr.dtype)  
# print(arr_2)  
# print(arr_2.dtype)  

# 4 BYTE 32 BIT 32 FERQLI QUTU HER QUTU 0 VE 1


# arr = np.array([1.1, 2.1, 0])
# newarr = arr.astype('str')
# print(newarr)        # [1 2 3]

# newarr = arr.astype('i')
# print(newarr)        # [1 2 3]

# newarr = arr.astype('f')
# print(newarr)        # [1 2 3]

# newarr = arr.astype('bool')
# print(newarr)        # [1 2 3]

# print(newarr.dtype)  # int32



#Copy 
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# x = arr

# x[0] = 42

# print(arr)  # [42  2  3  4  5]
# print(x)    # [1, 2, 3, 4, 5]


#View

arr = np.array([1, 2, 3, 4, 0])

# x = arr.view()
# x = arr

# arr[0] = 42

# print(arr)  # [42  2  3  4  5]
# print(x)    # [42  2  3  4  5]



#! Yapılandırılmış bir dizi oluşturma

# data_type = [('i4', 'U10'), ('yas', 'f4'), ('boy', 'f4')]
# veriler = np.array([('Ali', 31, 1.75), ('Veli', 28, 1.80), ('Veli', 28, 1.80)], dtype=data_type)

# print(veriler)


#! view copy
# a = np.array([1, 2, 3, 4, 5])
# b = a[1:3]  # b, a'nın bir görünümüdür

# b[0]=10

# print(a)
# print(b.base is a)  # True döner, çünkü b, a'nın verilerini paylaşır


#! shape 
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# new_arr = arr.reshape(2,4,2)

# print(new_arr)
# print(arr)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8,10], [5, 6, 7, 8,10], [5, 6, 7, 8,10], [5, 6, 7, 8,10], [5, 6, 7, 8,10]])
# newarr = arr.reshape(4, 3)
# print(arr)  # (2, 4)




# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 7)
# print(newarr)

# a* b* c  

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
# newarr = arr.reshape(12, 2)
# print(newarr)

# [[[ 1  2  3  4]
#   [ 5  6  7  8]
#   [ 9 10 11 12]]

#  [[13 14 15 16]
#   [17 18 19 20]
#   [21 22 23 24]]]



# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)

# [[[ 1  2]
#  [ 3  4]
#  [ 5  6]]

# [[ 7  8]
#  [ 9 10]
#  [11 12]]]








#! Diqqet
#! It is view 
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# new_arr = arr.reshape(2, 4).base  # [1 2 3 4 5 6 7 8]


# a = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# b = a[1:5]  # b, a'nın bir görünümüdür
# c = b[1:2]

# b[2] = 10
# print(b.base)
# print(a)

# print(b.base is a)  
# print(c.base is a)  



#! Arrayleri sütuna uyğun birlesdirmek
# [1, 2, 3]  [4, 5, 6]  [7, 8, 9]


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.array([7, 8, 9])

# arr = np.vstack((arr1, arr2))
# [[1 2 3]
#  [4 5 6]]

# arr = np.dstack((arr1, arr2, arr3))
# print(arr)





# arr1 = np.array([[1, 2],[3,4]])
# arr2 = np.array([[4, 5], [6,7]])

# arr = np.concatenate((arr1, arr2), axis = 1)

# print(arr)

# [1 2 3 4 5 6]



# axis - 0 sətir boyunca birləşdirmə yəni dik birləşdirmə
# axis - 1 sütun boyunca birləşdirmə yəni üfüqi birləşdirmə

# 1 2     5  6  3 4     7  8 

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)


# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)
# Hər sətirin birincisi ilə birincisi
# Hər sətirin ikincisi ilə ikincisi

# arr =  np.concatenate(np.concatenate((arr1, arr2), axis=0))
# print(arr)


# [[1 2 5 6]
#  [3 4 7 8]]




# arr1 = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
# arr2 = np.array([[[9, 10], [11, 12]],[[13, 14], [15, 16]]])

# arr = np.concatenate((arr1, arr2), axis=2)
# print(arr)



# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1, arr2))
# arr = np.vstack((arr1, arr2))

# print(arr)


#! Flatten - Düzləşdirmə
# arr = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]])
# newarr = arr.reshape(2,6)
# print(newarr)  
# print(arr.ndim)


# newarr = arr.reshape(-1)
# print(newarr)  
# print(newarr.ndim)




#! Enumurate
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   print(x)


# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z, end=" ")
    
# print()





#! nditer - F2 Qrupu 25 Dekabr Burada qaldi
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)



# a = np.arange(6).reshape(2,3)
# for x in np.nditer(a.T):
#     print(x, end=' ')

# print()

# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['float']):
#   print(x)
  
  
  
#! Empty array
# c = np.empty(3, dtype=int)
# print(c)
# c[0] = 10
# c[1] = 11
# c[2] = 12
# print(c)


  
  
#! ... 
# a = np.array([1, 2, 3])
# a[...]  = 5
# a[...]  = [item for item in range(3,6)]
# print(a)
  
  
  
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.empty(3, dtype=int)

# with np.nditer([a, b, c], [], [['readonly'], ['readonly'], ['writeonly']]) as it:
#     for x, y, z in it:
#         print(x, y, z)
#         z[...] = x + y
# print(c)


# arr = np.array([[1, 2], [3, 4]])
# with np.nditer(arr, flags=['multi_index']) as it:
#     for x in it:
#         print(f"Value: {x}, Index: {it.multi_index}")



#! Split
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr)

#! https://www.w3schools.com/python/numpy/numpy_array_split.asp
# 5  6  7  8

# arr1 = np.array([[1, 2] ,[3,4]])

# arr2 = np.array([[5, 6],[7,8]])

# new_arr_1 = np.hstack((arr1, arr2))
# new_arr_4 = np.concatenate((arr1, arr2),axis=1)

# new_arr_2 = np.vstack((arr1, arr2))
# new_arr_3 = np.concatenate((arr1, arr2),axis=0)
# print("hstack")
# print(new_arr_1)
# print("concatenate 2")
# print(new_arr_4)

# print("vstack")
# print(new_arr_2)
# print("concatenate")
# print(new_arr_3)


#! Search
# arr = np.array([1, 2, 3, 4, 5, 2,2,2,4, 4])

# x = np.where(arr % 2 == 1)
# print(x)




# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)

# Hara elave ede
# arr = np.array([6, 7, 8, 9,10])
# x = np.searchsorted(arr)
# print(x)



# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x)



#! Sorting
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))


#! Alphabetik
# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))


#! Boolean
# arr = np.array([True, False, True])
# print(np.sort(arr))



#! Filter Array

# arr = np.array([41, 42, 43, 44])
# x = arr[[True, False, True, False]]
# print(x)

# indexes = np.where(arr>3)
# new_arr = [arr[item] for item in indexes]
# print(new_arr)

# try catch
# pip packet manager
# virtual environment
# JSON
# PANDAS

#! Ferqli situsiyalar ucun
# arr = np.array([41, 42, 43, 44])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#   # if the element is higher than 42, set the value to True, otherwise False:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)



#! Direkt
# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


#! Random Numpy
from numpy import random

# x = random.randint(100)

# print(x)


# x = random.rand()

# print(x)

# x = random.rand(5)
# print(x)


#! Random 2D 
# x = random.rand(3, 5)
# print(x)


#! Random Array
# x=random.randint(100, size=(5))
# print(x)


#Random 2d Array
# x = random.randint(100, size=(3, 5))

#Random 3d Array
# x = random.randint(100, size=(3, 5, 2))

# print(x)



# Verilənlərdən rastgələ  array
# x = random.choice([3, 5, 7, 9])
# print(x)



# x = random.choice([3, 5, 7, 9], size=(3, 5))
# print(x)


#! ZIP in list
# y = [4, 5, 6, 7]
# x = [0,1,2,3]
# z = []

# for i, j in zip(x, y):
#     print(i,j)
#     z.append(i + j)
# print(z)




#! UFUNC SEARCH
# def myadd(x, y):
#   return x+y

# myadd = np.frompyfunc(myadd, 2, 1)

# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


#! Addition
# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = np.add(x, y)

# print(z)


#! Subtraction
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])

# newarr = np.subtract(arr1, arr2)

# print(newarr)   # [-10  -1   8  17  26  35]



#!  Multiplication
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])

# newarr = np.multiply(arr1, arr2)

# print(newarr)   # [200 420 660 920 1200 1500]


#!  (Division)
# newarr = np.divide(arr1, arr2)





#! POW
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([31, 5, 6, 8, 2, 33])

# newarr = np.power(arr1, arr2)

# print(newarr)   # [1000 3200000 729000000 -520093696 2500 0]


#! 
# arr1 = np.array([10, 20, 30, 40, 50, 60], dtype=float)
# arr2 = np.array([3, 5, 6, 8, 2, 33], dtype=float)

# newarr = np.power(arr1, arr2)

# print(newarr)   # [1.00000000e+03 3.20000000e+06 7.29000000e+08 6.55360000e+12 2.50000000e+03 4.77519667e+58]



#! MOD - Qalıq
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.mod(arr1, arr2)
# print(newarr)

#* Ve ya
# newarr = np.remainder(arr1, arr2)


# print(newarr)   # [1  6  3  0  0 27]



#! Division and MOD    Bölmə və qalıq
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.divmod(arr1, arr2)

# print(newarr)   # (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))


#! ABS 
# arr = np.array([-1, -2, 1, 2, 3, -4])

# newarr = np.absolute(arr)

# print(newarr)   # [1 2 1 2 3 4]



#! Yuvarlaqlaşdırma
# arr1 = np.trunc([-3.1666, 3.06667])
# arr2 = np.fix([-3.7666, 3.9667])

# print(arr1)  
# print(arr2)  



#! True Rounding
# arr = np.around(3.1566, 1)

# print(arr)   # 3.17



#! Floor
# arr = np.floor([-3.1666, 3.6667])
# print(arr)   # [-4.  3.]



#! Ceil
# arr = np.ceil([-3.1666, 3.6667])

# print(arr)   # [-3.  4.]



#! Logaritmini tapmaq

# arr = np.arange(1, 5)
# print(np.log2(arr))   # [0. 1. 1.5849625 2.]


#! Log10
# arr = np.arange(1, 5)
# print(np.log10(arr))   # [0. 0.30103 0.47712125 0.60205999]


#! Log e
# arr = np.arange(1, 10)
# print(np.log(arr))   # [0. 0.69314718 1.09861229 1.38629436]



#! Log n
# from math import log
# import numpy as np

# nplog = np.frompyfunc(log, 2, 1)

# print(nplog(100, 15))   # 1.7005483074552052



#! SUM 
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])

# newarr = np.add(arr1, arr2)   # [2 4 6]
# newarr = np.sum(arr1, arr2)   # 12

# print(newarr) 