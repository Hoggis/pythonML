
import numpy as np

#generate array of zeros
np.zeros(10)


#same for ones
np.ones(10)

#array with ten fives
arrOfFives = np.arange(10)
arrOfFives[:] = 5
arrOfFives


#array with int from 10 to 50
np.arange(10,51)

#array with int from 10 to 50, but only even numbers
np.arange(10,51,2)

# 3x3 matrix with values from 0 to 8
np.arange(9).reshape(3,3)

# 3x3 identity matrix
np.eye(3)

# random number between 0 and 1
np.random.rand(1)

# Generates 25 random numbers from a standard normal distribution
np.random.rand(25)


#experimentation with linspace
np.linspace(0,1,101)

# array with 20 numbers between 0 and 1
np.linspace(0,1,20)

mat = np.arange(1,26).reshape(5,5)

mat


#experimentation with selection
mat[2:,1:]
mat[3,4]
mat[:3,1:2]
mat[4:,0:5]
mat[3:,0:5]

# sum of mat
mat.sum()

# standard deviation of mat
mat.std()

# sum all columns of mat
mat.sum(axis=0)