import numpy as np

def lu_decomposition(A):
    N = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    for i in range(N):
        L[i, i] = 1
        for j in range(i, N):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i + 1, N):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    return L, U

def solve_lu(A, b):
    L, U = lu_decomposition(A)

    N = len(b)
    y = np.zeros(N)
    for i in range(N):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    x = np.zeros(N)
    for i in range(N-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    residuum = np.linalg.norm(np.dot(A, x) - b)
    return x, residuum
