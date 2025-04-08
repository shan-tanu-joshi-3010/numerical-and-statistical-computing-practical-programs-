import numpy as np

def jacobi_method(A, b, tol, max_iter):
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)  # Initial guess
    x_new = np.zeros_like(x, dtype=np.float64)

    for it in range(max_iter):
        for i in range(n):
            sum_ = np.dot(A[i, :], x) - A[i, i] * x[i]  # Sum excluding A[i, i] * x[i]
            x_new[i] = (b[i] - sum_) / A[i, i]
        
        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Converged in {it + 1} iterations.")
            return x_new
        
        x = np.copy(x_new)
    
    print("Did not converge within the maximum number of iterations.")
    return None

# Example usage
if __name__ == "__main__":
    # Define the matrix and the right-hand side vector
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=np.float64)
    b = np.array([15, 10, 10, 10], dtype=np.float64)

    # Call jacobi_method
    solution = jacobi_method(A, b, tol=1e-6, max_iter=100)
    if solution is not None:
        print(f"Solution: {solution}")
