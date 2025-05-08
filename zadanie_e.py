import matplotlib.pyplot as plt
import numpy as np
from jacobi import solve_Jacobi
from gauss_seidel import solve_Gauss_Seidel
from generate_matrix import generate_matrix
from lu import solve_lu
import time

N_values = [100, 500, 1000, 2000, 3000, 4000]

times_lu = []
times_jacobi = []
times_gs = []

for N in N_values:
    print(f"Processing N = {N}...")

    A, b = generate_matrix(N, 'A')

    start = time.time()
    x_lu, r_norm_lu = solve_lu(A, b)
    times_lu.append(time.time() - start)

    start = time.time()
    x_jacobi, r_norm_jacobi, iter_jacobi = solve_Jacobi(A, b)
    times_jacobi.append(time.time() - start)

    start = time.time()
    x_gs, r_norm_gs, iter_gs = solve_Gauss_Seidel(A, b)
    times_gs.append(time.time() - start)

plt.figure(figsize=(12, 6))

# Plot 1
plt.subplot(1, 2, 1)
plt.plot(N_values, times_lu, 'o-', label='LU Decomposition')
plt.plot(N_values, times_jacobi, 's-', label='Jacobi')
plt.plot(N_values, times_gs, 'd-', label='Gauss-Seidel')
plt.xlabel('Number of unknowns (N)')
plt.ylabel('Time (seconds)')
plt.title('Solution Time Comparison (Linear Scale)')
plt.grid(True)
plt.legend()

# Plot 2
plt.subplot(1, 2, 2)
plt.plot(N_values, times_lu, 'o-', label='LU Decomposition')
plt.plot(N_values, times_jacobi, 's-', label='Jacobi')
plt.plot(N_values, times_gs, 'd-', label='Gauss-Seidel')
plt.xlabel('Number of unknowns (N)')
plt.ylabel('Time (seconds)')
plt.yscale('log')
plt.title('Solution Time Comparison (Log Scale)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('solution_time_comparison.png')
plt.show()

print("\nTimes:")
print(f"{'N':<8}{'LU (s)':<12}{'Jacobi (s)':<12}{'Gauss-Seidel (s)':<12}")
for i, N in enumerate(N_values):
    print(f"{N:<8}{times_lu[i]:<12.4f}{times_jacobi[i]:<12.4f}{times_gs[i]:<12.4f}")
