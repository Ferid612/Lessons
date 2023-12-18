# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating an array of 10 zeros using np.zeros()
array = np.zeros(10)

# Printing a message indicating an array of 10 zeros
print("An array of 10 zeros:")

# Printing the array of 10 zeros
print(array)

# Creating an array of 10 ones using np.ones()
array = np.ones(10)


# Printing a message indicating an array of 10 ones
print("An array of 10 ones:")

# Printing the array of 10 ones
print(array)

# Creating an array of 10 fives by multiplying an array of 10 ones by 5
array = np.ones(10) * 5

# Printing a message indicating an array of 10 fives
print("An array of 10 fives:")

# Printing the array of 10 fives
print(array) 



#! Interesting 

# # Importing the NumPy library with an alias 'np'
# import numpy as np

# # Creating a 10x10 matrix filled with ones using np.ones()
# x = np.ones((10, 10))

# # Setting the inner values of the matrix 'x' (excluding the borders) to 0 using slicing
# x[1:-1, 1:-1] = 0

# # Printing the modified matrix 'x'
# print(x) 
