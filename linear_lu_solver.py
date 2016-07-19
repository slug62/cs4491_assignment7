#!/usr/bin/python3
"""
    Program:        linear_lu_solver.py
    Author:         Peter Southwick
    Date:           07/16/16
    Description:    A Short program that solves the following linear equation using LU decomposition:
                    3x1 +5x2 +2x3 = 8
                    2x1 +3x2 −x3  = 1
                    x1  −2x2 −3x3 = −1

"""

import numpy as np

a_matrix = np.array([[3, 5, 2], [2, 3, -1], [1, -2, -3]])
b_matrix = [8, 1, -1]
x_matrix = np.linalg.solve(a_matrix, b_matrix)

print("Matrix a:")
print(a_matrix)
print("Matrix b:")
print(b_matrix)
print("Matrix x:")
print(x_matrix)


