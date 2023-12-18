# Importing the NumPy library with an alias 'np'
import numpy as np

# Importing the 'os' module for operating system-dependent functionality
import os

# Creating a NumPy array 'a' with integers from 0 to 19 using np.arange()
a = np.arange(20)

# Saving the NumPy array 'a' as a file named 'temp_arra.npy' using np.save()
np.save('temp_arra.npy', a)

# Printing a message checking if the file 'temp_arra.npy' exists or not
print("Check if 'temp_arra.npy' exists or not?")

# Checking if the file 'temp_arra.npy' exists using os.path.exists()
if os.path.exists('temp_arra.npy'):
    # Loading the data from 'temp_arra.npy' into 'x2' using np.load()
    x2 = np.load('temp_arra.npy')
    
    # Checking if the loaded array 'x2' is equal to the original array 'a' using np.array_equal()
    print(np.array_equal(a, x2)) 
