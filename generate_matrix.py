import numpy as np

def generate_matrix(N, task='A'):
    e = 5
    f = 7
    if task == 'A':
        a1 = 5 + e
        a2 = a3 = -1
    elif task == 'C':
        a1 = 3
        a2 = a3 = -1
    else:
        raise ValueError("Invalid task. Use 'A' or 'C'.")

    A = np.diag(np.ones(N) * a1) + np.diag(np.full(N - 1, a2), 1) + np.diag(np.full(N - 1, a2), -1)
    A += np.diag(np.full(N - 2, a3), 2)
    A += np.diag(np.full(N - 2, a3), -2)

    b = np.sin(np.arange(1, N + 1) * (f + 1))

    return A, b
