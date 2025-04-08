def newton_raphson(f, df, x0, tol, max_iter):
    for i in range(max_iter):
        # Compute the next approximation
        x1 = x0 - f(x0) / df(x0)
        
        # Check for convergence
        if abs(x1 - x0) < tol:
            print(f"Converged in {i + 1} iterations.")
            return x1
        
        # Update the current approximation
        x0 = x1
    
    print("Did not converge within the maximum number of iterations.")
    return None

# Example usage
if __name__ == "__main__":
    # Define the function and its derivative
    def f(x):
        return x**2 - 4

    def df(x):
        return 2 * x

    # Call newton_raphson
    root = newton_raphson(f, df, x0=1.0, tol=1e-6, max_iter=100)
    if root is not None:
        print(f"Root: {root}")
