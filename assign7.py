#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plot

ti = 0  # Starting value of vector t
tf = 2 * np.pi  # Ending value of vector t
tn = 75  # Number of elements we want
vector_t = np.array(np.linspace(ti, tf, tn))  # Creating a numpy array
vector_v = np.sin(vector_t)  # creating a vector v from the sign of vector t values

line, = plot.plot(vector_t, vector_v)  # Plotting the vectors

plot.show()  

a_matrix = np.array([[3, 5, 2], [2, 3, -1], [1, -2, -3]])
b_matrix = [8, 1, -1]
x_matrix = np.linalg.solve(a_matrix, b_matrix)

print("Matrix a:")
print(a_matrix)
print("Matrix b:")
print(b_matrix)
print("Matrix x:")
print(x_matrix)


