#!/usr/bin/python3
"""
    Program:        sin_vector.py
    Author:         Peter Southwick
    Date:           07/15/16
    Description:    A Short program that creates a vector of values 0 through 2pi, and then
                    creates another vector of values by taking the sin() of the original vector, then plots
                    the values on a graph.
"""

import numpy as np
import matplotlib.pyplot as plot

ti = 0  # Starting value of vector t
tf = 2 * np.pi  # Ending value of vector t
tn = 75  # Number of elements we want
vector_t = np.array(np.linspace(ti, tf, tn))  # Creating a numpy array
vector_v = np.sin(vector_t)  # creating a vector v from the sign of vector t values

line, = plot.plot(vector_t, vector_v)  # Plotting the vectors

plot.show()