import numpy as np
import matplotlib.pyplot as plt

def solve_Gauss_Seidel(A, b, tol=1e-9, max_iter=1000, plot=False):
    N = len(A)
    x = np.ones(N)
    r_norm = []

    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    residuum = np.linalg.norm(A @ x - b)
    r_norm.append(residuum)

    iteration_count = 0

    while residuum > tol and iteration_count < max_iter:
        x = np.linalg.solve(D + L, b - U @ x)
        residuum = np.linalg.norm(A @ x - b)
        r_norm.append(residuum)
        iteration_count += 1

    if plot:
        plt.figure()
        plt.semilogy(range(iteration_count + 1), r_norm)
        plt.xlabel('Iteration Count')
        plt.ylabel('Residuum Norm')
        plt.title('Convergence of Gauss-Seidel Method')
        plt.savefig(str(N) + 'gauss_seidel_convergence.png')
        plt.show()

    return x, r_norm, iteration_count

# x_gs, r_norm_gs, iter_gs = solve_Gauss_Seidel(A, b)
