def regula_falsi(f, a, b, tol, max_iter):
    """
    Regula Falsi Method for finding the root of a function f(x)
    
    Parameters:
        f: The function for which the root is being calculated
        a, b: Initial guesses (must enclose the root, f(a) * f(b) < 0)
        tol: Tolerance level for stopping
        max_iter: Maximum number of iterations allowed
        
    Returns:
        A root of the function or None if not converging
    """
    if f(a) * f(b) >= 0:
        print("The function must have opposite signs at a and b.")
        return None

    for i in range(max_iter):
        # Calculate the point of intersection (c)
        c = b - f(b) * (b - a) / (f(b) - f(a))
        
        # Check for convergence
        if abs(f(c)) < tol:
            print(f"Converged in {i + 1} iterations.")
            return c
        
        # Update bounds
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    print("Did not converge within the maximum number of iterations.")
    return None

# Example usage
if __name__ == "__main__":
    # Define the function
    def f(x):
        return x**2 - 4

    # Call regula_falsi
    root = regula_falsi(f, 0, 3, tol=1e-6, max_iter=100)
    if root is not None:
        print(f"Root: {root}")
