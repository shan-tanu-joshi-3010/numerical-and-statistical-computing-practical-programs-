import numpy as np

def lu_decomposition_solve(A, b):
    n = len(A)
    L = np.zeros_like(A, dtype=np.float64)
    U = np.zeros_like(A, dtype=np.float64)
    
    # LU Decomposition
    for i in range(n):
        # Compute U (upper triangular matrix)
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        
        # Compute L (lower triangular matrix)
        for j in range(i, n):
            if i == j:
                L[i, j] = 1  # Diagonal elements of L are 1
            else:
                L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    
    # Forward substitution: Solve L * y = b
    y = np.zeros_like(b, dtype=np.float64)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i]))
    
    # Backward substitution: Solve U * x = y
    x = np.zeros_like(b, dtype=np.float64)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x

# Example usage
if __name__ == "__main__":
    # Define matrix A and vector b
    A = np.array([[4, 3, 0],
                  [3, 4, -1],
                  [0, -1, 4]], dtype=np.float64)
    b = np.array([24, 30, -24], dtype=np.float64)
    
    # Solve the system using LU decomposition
    solution = lu_decomposition_solve(A, b)
    print("Solution vector x:")
    print(solution)
