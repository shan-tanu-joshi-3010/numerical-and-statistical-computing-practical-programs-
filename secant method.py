def secant_method(f, x0, x1, tol, max_iter):
   
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-12:
            print("Denominator too small.")
            return None
        
        # Compute the next approximation
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        # Check for convergence
        if abs(x2 - x1) < tol:
            print(f"Converged in {i + 1} iterations.")
            return x2
        
        # Update guesses
        x0, x1 = x1, x2
    
    print("Did not converge within the maximum number of iterations.")
    return None

# Example usage
if __name__ == "__main__":
    import math

    # Define the function
    def f(x):
        return x**2 - 4

    # Call secant_method
    root = secant_method(f, 1, 2, 1e-6, 100)
    if root is not None:
        print(f"Root: {root}")
