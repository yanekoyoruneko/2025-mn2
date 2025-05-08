import matplotlib.pyplot as plt
import numpy as np
from jacobi import solve_Jacobi
from gauss_seidel import solve_Gauss_Seidel
from generate_matrix import generate_matrix
from lu import solve_lu
import time

A, b = generate_matrix(1262, 'C')
x_lu, r_norm_lu = solve_lu(A, b)
print(x_lu, r_norm_lu)
