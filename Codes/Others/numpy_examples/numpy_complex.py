# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'a' containing various types of numbers (complex, real, scalar)
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

# Printing the original array 'a'
print("Original array")
print(a)

# Checking the given array 'a' element-wise for complex numbers and printing the result
print("Checking for complex number:")
print(np.iscomplex(a))

# Checking the given array 'a' element-wise for real numbers and printing the result
print("Checking for real number:")
print(np.isreal(a))

# Checking if a value is a scalar or not (in this case, checking if 3.1 is a scalar)
print("Checking for scalar type:")
print(np.isscalar(3.1))
# True

# Checking if a list ([3.1]) is a scalar or not (in this case, it's not a scalar)
print(np.isscalar([3.1])) 
# False

# Original array
# [ 1.0+1.j  1.0+0.j  4.5+0.j  3.0+0.j  2.0+0.j  0.0+2.j]
# Checking for complex number:
# [ True False False False False  True]
# Checking for real number:
# [False  True  True  True  True False]
# Checking for scalar type:
# True
# False      