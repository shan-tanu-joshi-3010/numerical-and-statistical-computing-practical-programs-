
def f(x):
    # Define your function here
    return x**3 - x - 2

def secant_method(x0, x1, tol, max_iter):
    print(f"Iter\t x0\t\t x1\t\t x2\t\t f(x2)")
    for i in range(max_iter):
        # Calculate the next approximation
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Division by zero error!")
            return None
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        f_x2 = f(x2)
        
        # Print iteration details
        print(f"{i+1}\t {x0:.6f}\t {x1:.6f}\t {x2:.6f}\t {f_x2:.6f}")
        
        # Check for convergence
        if abs(f_x2) < tol:
            print(f"Root found: {x2:.6f}")
            return x2
        
        # Update variables for next iteration
        x0, x1 = x1, x2
    
    print("Maximum iterations reached without convergence.")
    return None

# Example usage
x0 = 1.0  # Initial guess 1
x1 = 2.0  # Initial guess 2
tolerance = 1e-6
max_iterations = 100

root = secant_method(x0, x1, tolerance, max_iterations)