# Importing the NumPy library with an alias 'np'
import numpy as np  

# Creating a NumPy array 'nums' containing values in a 3x3 matrix
nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 4.38, 6.99],
              [1.54, 2.39, 9.29]])

# Printing a message indicating the original array
print("Original array:")
print(nums)

# Sorting the array 'nums' by rows in ascending order and displaying the sorted result
print("\nSort the said array by row in ascending order:")
print(np.sort(nums))

# Sorting the array 'nums' by columns in ascending order and displaying the sorted result
print("\nSort the said array by column in ascending order:")
print(np.sort(nums, axis=0)) 
