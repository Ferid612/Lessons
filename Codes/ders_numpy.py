# pip install numpy
import numpy as np

# print(np.__version__)

# arr = np.array([1, 2, 3, 4, 5])

#  1,2,3,4,5
# Array 
#  1 INDEX, 2,3,4,5
# List


# print(arr)
# print(type(arr))



# arr = np.array(42)
# print(arr)
# print(type(arr))




# 2D array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)


# # 3D array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)





# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
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



# arr = np.array([[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]],  [[1,2,3,4,5], [6,7,8,9,123],[11,12,13,14,15]]  ,[[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]]])

# print(   arr[1,1,4]   )

#3D Index

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

# minus index
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])



# slice

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, ::1])   # [7 8 9]




# arr = np.array(['a', '2', '3'], dtype='i')
# arr_2 = np.array(['1', '2', '3'], dtype='i4')
# # print(arr.dtype)  
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
# # x = arr
# x[0] = 42

# print(arr)  # [42  2  3  4  5]
# print(x)    # [1, 2, 3, 4, 5]


#View

# arr = np.array([1, 2, 3, 4, 0], dtype='bool')
# x = arr.view()
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


#! shape !BURDA QALDIQ F1 QRUPU
# arr = np.array([[1, 2, 3, 4,5], [5, 6, 7, 8,10], [5, 6, 7, 8, 10], [5, 6, 7, 8,10], [5, 6, 7, 8,10], [5, 6, 7, 8,10]])
# print(arr) 
# print(arr.shape) 


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 7)
# print(newarr)

# a* b* c  

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
newarr = arr.reshape(12, 2)
print(newarr)

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



#! It is view 
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# print(arr.reshape(2, 4).base)  # [1 2 3 4 5 6 7 8]


#! Arrayleri birlesdirmek
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.array([7, 8, 9])

# arr = np.vstack((arr1, arr2, arr3))

    # arr = np.dstack((arr1, arr2, arr3))

    # print(arr)

# [[1 2 3]
#  [4 5 6]]


#! Flatten
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newarr = arr.reshape(-1)

# print(newarr)  # [1 2 3 4 5 6]



#! nditer
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)


#! Enumurate
# import numpy as np

# arr = np.array([[1, 2], [3, 4]])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# (0, 0) 1
# (0, 1) 2
# (1, 0) 3
# (1, 1) 4