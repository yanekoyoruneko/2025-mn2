import matplotlib.pyplot as plt
import numpy as np
from jacobi import solve_Jacobi
from gauss_seidel import solve_Gauss_Seidel
from generate_matrix import generate_matrix
from lu import solve_lu
import time

A, b = generate_matrix(1262, 'C')
x_jacobi, r_norm_jacobi, iter_jacobi = solve_Jacobi(A, b, plot=True)
x_gs, r_norm_gs, iter_gs = solve_Gauss_Seidel(A, b, plot=True)
