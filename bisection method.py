def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None
    
    iter_count = 0
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2.0
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iter_count += 1
    
    return (a + b) / 2.0

# Example usage:
def example_function(x):
    return x**3 - x - 2

root = bisection_method(example_function, 1, 2)
print("The root is:", root)